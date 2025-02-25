import sys
import random
import time
import winsound
from qs import (Example_questions_form, 
    HEM, MGN, HP_TBL_diving, HA, GPT, pharm, 
    HA4mid, HA4mid_prac, CCM, GPT_mid, MIM_mid)
import json, os
from typing import Optional  # added for type hints

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QProgressBar, QMessageBox, QRadioButton, QButtonGroup,
    QTextBrowser, QGraphicsOpacityEffect, QTableWidget, QTableWidgetItem, QLineEdit, QInputDialog, QSlider, QHeaderView,
    QGridLayout, QSizePolicy, QSpacerItem # Import QGridLayout, QSizePolicy, QSpacerItem
)
from PySide6.QtGui import QFont, QPixmap, QIcon
from PySide6.QtCore import QTimer, Qt, QPropertyAnimation, QEasingCurve
 
# Import theme dictionaries and helper function
from styles import DARK_THEME, PINK_THEME, get_theme
from quiz import Quiz
from scoreboard import Scoreboard, ScoreboardWidget

# Define a constant for the preferences file path
PREFERENCES_FILE: str = "preferences.json"

def load_theme_preference() -> str:
    """Load the user's theme preference from the preferences file."""
    if os.path.exists(PREFERENCES_FILE):
        try:
            with open(PREFERENCES_FILE, "r") as file:
                prefs = json.load(file)
                return prefs.get("theme", "dark")
        except Exception as e:
            print(f"Error loading preferences: {e}")
            return "dark"
    return "dark"

def save_theme_preference(theme_name: str) -> None:
    """Save the user's theme preference to the preferences file."""
    try:
        with open(PREFERENCES_FILE, "w") as file:
            json.dump({"theme": theme_name}, file, indent=4)
    except Exception as e:
        print(f"Error saving preferences: {e}")

# Mapping of quiz names to question dictionaries; modify as needed.
quiz_mapping = {
    "Embryology": HEM,
    "Medical Genetics": MGN,
    "TBL Quiz": HP_TBL_diving,
    "HA4 Quiz 1": HA,
    "GPT prac": GPT,
    "GPT midterm": GPT_mid,
    "pharma": pharm,
    "HA 4 midterm": HA4mid,
    "HA 4 midterm prac": HA4mid_prac,
    "CCM": CCM,
    "MIM midterm": MIM_mid
}

class MainMenu(QMainWindow):
    """Main menu window for launching quizzes and managing themes."""
    def __init__(self, scoreboard):
        """
        Initialize the main menu with a scoreboard, load theme preference, and build the UI.
        """
        super().__init__()
        self.scoreboard = scoreboard
        self.current_quiz_name: Optional[str] = None
        # Load user preference and set theme dictionary accordingly
        self.current_theme = load_theme_preference()  # "dark" or "pink"
        self.theme = get_theme(self.current_theme)
        self.setWindowTitle("MedCQ")
        self.setWindowIcon(QIcon(r"Small_projects\Moudels\PySide6\MedCQ\images\icon3.png"))
        self.setWindowState(Qt.WindowMaximized)
        self.setStyleSheet(self.theme["MAIN_WINDOW_STYLE"])
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.setup_ui()

    def setup_ui(self):
        self.main_menu_widget = QWidget()
        self.main_menu_layout = QVBoxLayout(self.main_menu_widget)
        self.main_menu_layout.setSpacing(20)
        self.main_menu_layout.setContentsMargins(50, 30, 50, 30)

        # Logo
        logo_label = QLabel()
        logo_pixmap = QPixmap("Small_projects\Moudels\PySide6\MedCQ\images\icon3.png")  # adjust path if needed
        logo_pixmap = logo_pixmap.scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        self.main_menu_layout.addWidget(logo_label, alignment=Qt.AlignCenter)

        # Header
        header = QLabel("Welcome to MedCQ, Select a Quiz")
        header.setStyleSheet(self.theme["HEADER_LABEL_STYLE"])
        header.setAlignment(Qt.AlignCenter)
        header.setFixedHeight(45)
        header.setFont(QFont("Arial", 24, QFont.Bold))
        self.main_menu_layout.addWidget(header)

        # Year selection buttons
        year_container = QWidget()
        self.year_layout = QHBoxLayout(year_container)
        self.year_layout.setSpacing(10)  # Add spacing between year buttons
        
        self.year_buttons = {}
        for year in range(1, 7):
            btn = QPushButton(f"Year {year}")
            btn.setStyleSheet(self.theme["MENU_BUTTON_STYLE"])
            btn.clicked.connect(lambda checked, y=year: self.show_year_options(y))
            btn.setFixedSize(120, 50)  # Set fixed size for year buttons
            btn.setFont(QFont("Arial", 12))
            self.year_layout.addWidget(btn)
            self.year_buttons[year] = btn

        self.main_menu_layout.addWidget(year_container)
        
        # Add some spacing
        self.main_menu_layout.addSpacerItem(QSpacerItem(20, 20))

        # Quiz buttons container
        quiz_container = QWidget()
        quiz_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.quiz_buttons_layout = QGridLayout(quiz_container)
        self.quiz_buttons_layout.setSpacing(15)
        self.main_menu_layout.addWidget(quiz_container)

        # Timer input
        self.time_limit_input = QLineEdit()
        self.time_limit_input.setPlaceholderText("timer (minutes)")
        self.time_limit_input.setStyleSheet(self.theme["TIME_LIMIT_INPUT_STYLE"])
        self.time_limit_input.setFixedSize(200, 50)
        self.time_limit_input.setAlignment(Qt.AlignCenter)
        self.main_menu_layout.addWidget(self.time_limit_input, alignment=Qt.AlignCenter)

        # Bottom buttons container
        bottom_container = QWidget()
        bottom_layout = QHBoxLayout(bottom_container)
        bottom_layout.setSpacing(15)

        # Scoreboard button
        scoreboard_btn = QPushButton("Scoreboard")
        scoreboard_btn.setStyleSheet(self.theme["SCOREBOARD_BUTTON_STYLE"])
        scoreboard_btn.clicked.connect(self.show_scoreboard)
        scoreboard_btn.setFixedSize(150, 50)
        bottom_layout.addWidget(scoreboard_btn)

        # Switch Theme button
        self.switch_theme_button = QPushButton("Switch Theme")
        self.switch_theme_button.setStyleSheet(self.theme["MENU_BUTTON_STYLE"])
        self.switch_theme_button.clicked.connect(self.switch_theme)
        self.switch_theme_button.setFixedSize(150, 50)
        bottom_layout.addWidget(self.switch_theme_button)

        # Exit button
        exit_btn = QPushButton("Exit")
        exit_btn.setStyleSheet(self.theme["EXIT_BUTTON_STYLE"])
        exit_btn.clicked.connect(self.confirm_exit)
        exit_btn.setFixedSize(150, 50)
        bottom_layout.addWidget(exit_btn)

        self.main_menu_layout.addWidget(bottom_container, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.main_menu_widget)

    def confirm_exit(self):
        reply = QMessageBox.question(self, "Exit Confirmation", "Are you sure you want to exit?",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()

    def switch_theme(self):
        # Toggle current theme and update theme dictionary
        self.current_theme = "pink" if self.current_theme == "dark" else "dark"
        self.theme = get_theme(self.current_theme)
        self.setStyleSheet(self.theme["MAIN_WINDOW_STYLE"])
        self.main_menu_widget.setStyleSheet(self.theme["MAIN_WINDOW_STYLE"])
        # Reapply key element styles:
        self.main_menu_layout.itemAt(0).widget().setStyleSheet(self.theme["HEADER_LABEL_STYLE"])
        self.time_limit_input.setStyleSheet(self.theme["TIME_LIMIT_INPUT_STYLE"])
        self.switch_theme_button.setStyleSheet(self.theme["MENU_BUTTON_STYLE"])
        # Update styles for all buttons in the main menu
        for i in range(self.quiz_buttons_layout.count()):
            button = self.quiz_buttons_layout.itemAt(i).widget()
            button.setStyleSheet(self.theme["MENU_BUTTON_STYLE"])
        # Update styles for scoreboard and exit buttons
        self.main_menu_layout.itemAt(self.main_menu_layout.count() - 3).widget().setStyleSheet(self.theme["SCOREBOARD_BUTTON_STYLE"])
        self.main_menu_layout.itemAt(self.main_menu_layout.count() - 2).widget().setStyleSheet(self.theme["EXIT_BUTTON_STYLE"])
        
        # Update styles for year buttons
        for button in self.year_buttons.values():
            button.setStyleSheet(self.theme["MENU_BUTTON_STYLE"])

        # Iterate through all widgets in the main menu layout and reapply styles
        for i in range(self.main_menu_layout.count()):
            widget = self.main_menu_layout.itemAt(i).widget()
            if widget:
                if isinstance(widget, QPushButton):
                    widget.setStyleSheet(self.theme["MENU_BUTTON_STYLE"])
                elif isinstance(widget, QLineEdit):
                    widget.setStyleSheet(self.theme["TIME_LIMIT_INPUT_STYLE"])
                elif isinstance(widget, QLabel):
                    widget.setStyleSheet(self.theme["HEADER_LABEL_STYLE"])
        
        # Update styles for bottom buttons (Scoreboard and Exit)
        bottom_container = self.main_menu_layout.itemAt(self.main_menu_layout.count() - 1).widget()
        if bottom_container:
            bottom_layout = bottom_container.layout()
            for i in range(bottom_layout.count()):
                widget = bottom_layout.itemAt(i).widget()
                if isinstance(widget, QPushButton):
                    if widget.text() == "Scoreboard":
                        widget.setStyleSheet(self.theme["SCOREBOARD_BUTTON_STYLE"])
                    elif widget.text() == "Exit":
                        widget.setStyleSheet(self.theme["EXIT_BUTTON_STYLE"])
                    else:
                        widget.setStyleSheet(self.theme["MENU_BUTTON_STYLE"])

        # If a Quiz page is active, restart it
        if hasattr(self, "quiz_widget"):
            current_quiz = self.current_quiz_name
            time_limit = int(self.time_limit_input.text()) * 60 if self.time_limit_input.text().isdigit() else None
            self.main_layout.removeWidget(self.quiz_widget)
            self.quiz_widget.deleteLater()
            self.quiz_widget = Quiz(quiz_mapping.get(current_quiz, Example_questions_form), self, self.scoreboard, time_limit)
            self.main_layout.addWidget(self.quiz_widget)
        # If Scoreboard is active, restart (similar logic can be applied)
        if hasattr(self, "scoreboard_widget"):
            self.main_layout.removeWidget(self.scoreboard_widget)
            self.scoreboard_widget.deleteLater()
            self.scoreboard_widget = ScoreboardWidget(self, self.scoreboard)
            self.scoreboard_widget.update_scores()
            self.main_layout.addWidget(self.scoreboard_widget)
        save_theme_preference(self.current_theme)

    def show_year_options(self, year: int):
        """Show theory/practical options for all years."""
        # Clear existing buttons
        for i in reversed(range(self.quiz_buttons_layout.count())):
            widget = self.quiz_buttons_layout.itemAt(i).widget()
            self.quiz_buttons_layout.removeWidget(widget)
            widget.deleteLater()

        # Show Theory and Practical buttons for all years
        theory_btn = QPushButton("Theory")
        theory_btn.setStyleSheet(self.theme["MENU_BUTTON_STYLE"])
        theory_btn.setFixedSize(200, 50)
        theory_btn.setFont(QFont("Arial", 12))
        theory_btn.clicked.connect(lambda checked, y=year, m="theory": self.show_quiz_selection(m, y))
        
        practical_btn = QPushButton("Practical")
        practical_btn.setStyleSheet(self.theme["MENU_BUTTON_STYLE"])
        practical_btn.setFixedSize(200, 50)
        practical_btn.setFont(QFont("Arial", 12))
        practical_btn.clicked.connect(lambda checked, y=year, m="practical": self.show_quiz_selection(m, y))

        self.quiz_buttons_layout.addWidget(theory_btn, 0, 0)
        self.quiz_buttons_layout.addWidget(practical_btn, 0, 1)

    def show_quiz_selection(self, mode: str, year: int):
        """Display quiz selection buttons based on the selected mode and year."""
        # Clear existing buttons
        for i in reversed(range(self.quiz_buttons_layout.count())):
            widget = self.quiz_buttons_layout.itemAt(i).widget()
            self.quiz_buttons_layout.removeWidget(widget)
            widget.deleteLater()

        # Quiz selection buttons
        if year == 2:
            if mode == "theory":
                quizzes = [
                    "CCM",
                    "GPT midterm",
                    "MIM midterm"
                ]
            else:  # mode == "practical"
                quizzes = [
                    "HA 4 midterm prac",
                    "GPT prac"
                ]
        else:
            # Example quizzes for other years
            quizzes = [
                f"Year {year} Quiz 1",
                f"Year {year} Quiz 2",
                f"Year {year} Quiz 3",
                f"Year {year} Quiz 4"
            ]

        row, col = 0, 0
        for quiz_name in quizzes:
            btn = QPushButton(quiz_name)
            btn.setStyleSheet(self.theme["MENU_BUTTON_STYLE"])
            if year == 2:
                btn.clicked.connect(lambda checked, q=quiz_name: self.launch_quiz(q))
            else:
                # Use Example_questions_form for other years
                btn.clicked.connect(lambda checked, q=quiz_name: self.launch_quiz(q, use_example=True))
            btn.setFixedSize(200, 50)
            btn.setFont(QFont("Arial", 11))
            self.quiz_buttons_layout.addWidget(btn, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1

    def launch_quiz(self, quiz_name: str, use_example: bool = False):
        """Launch quiz with either actual questions or example questions."""
        self.current_quiz_name = quiz_name
        questions = Example_questions_form if use_example else quiz_mapping.get(quiz_name, Example_questions_form)
        time_limit = int(self.time_limit_input.text()) * 60 if self.time_limit_input.text().isdigit() else None
        self.quiz_widget = Quiz(questions, self, self.scoreboard, time_limit)
        self.main_layout.addWidget(self.quiz_widget)
        self.main_menu_widget.hide()
        self.quiz_widget.show()

    def show_scoreboard(self):
        self.scoreboard_widget = ScoreboardWidget(self, self.scoreboard)
        self.scoreboard_widget.update_scores()
        self.main_layout.addWidget(self.scoreboard_widget)
        self.main_menu_widget.hide()
        self.scoreboard_widget.show()

    def return_to_menu(self):
        if hasattr(self, 'quiz_widget'):
            self.quiz_widget.hide()
            self.main_layout.removeWidget(self.quiz_widget)
            self.quiz_widget.deleteLater()
            del self.quiz_widget
        if hasattr(self, 'scoreboard_widget'):
            self.scoreboard_widget.hide()
            self.main_layout.removeWidget(self.scoreboard_widget)
            self.scoreboard_widget.deleteLater()
            del self.scoreboard_widget
        self.main_menu_widget.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    scoreboard = Scoreboard()
    menu = MainMenu(scoreboard)
    menu.show()
    sys.exit(app.exec())