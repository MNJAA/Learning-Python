import sys
import random
import time
import winsound
from qs import Example_questions_form, HEM, MGN, HP_TBL_diving, HA, GPT, pharm, HA4mid, HA4mid_prac
import json, os
from typing import Optional  # added for type hints

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QProgressBar, QMessageBox, QRadioButton, QButtonGroup,
    QTextBrowser, QGraphicsOpacityEffect, QTableWidget, QTableWidgetItem, QLineEdit, QInputDialog, QSlider, QHeaderView
)
from PySide6.QtGui import QFont, QPixmap
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
    "GPT prac Quiz": GPT,
    "pharma": pharm,
    "HA 4 midterm": HA4mid,
    "HA 4 midterm prac": HA4mid_prac
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
        self.setWindowTitle("Quiz Menu")
        self.setWindowState(Qt.WindowMaximized)
        self.setStyleSheet(self.theme["MAIN_WINDOW_STYLE"])
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.setup_ui()

    def setup_ui(self):
        self.main_menu_widget = QWidget()
        self.main_menu_layout = QVBoxLayout(self.main_menu_widget)
        header = QLabel("Select a Quiz")
        header.setStyleSheet(self.theme["HEADER_LABEL_STYLE"])
        header.setAlignment(Qt.AlignCenter)
        self.main_menu_layout.addWidget(header)

        self.buttons_layout = QVBoxLayout()
        self.main_menu_layout.addLayout(self.buttons_layout)

        quizzes = [
            "Embryology",
            "Medical Genetics",
            "TBL Quiz",
            "HA4 Quiz 1",
            "GPT prac Quiz",
            "pharma",
            "HA 4 midterm",  # Added this line
            "HA 4 midterm prac"  # Added this line
        ]

        for quiz_name in quizzes:
            btn = QPushButton(quiz_name)
            btn.setStyleSheet(self.theme["MENU_BUTTON_STYLE"])
            btn.clicked.connect(lambda checked, q=quiz_name: self.launch_quiz(q))
            self.buttons_layout.addWidget(btn)

        self.time_limit_input = QLineEdit()
        self.time_limit_input.setPlaceholderText("set a timer, enter any number in minutes (optional)")
        self.time_limit_input.setStyleSheet(self.theme["TIME_LIMIT_INPUT_STYLE"])
        self.main_menu_layout.addWidget(self.time_limit_input)

        scoreboard_btn = QPushButton("View Scoreboard")
        scoreboard_btn.setStyleSheet(self.theme["SCOREBOARD_BUTTON_STYLE"])
        scoreboard_btn.clicked.connect(self.show_scoreboard)
        self.main_menu_layout.addWidget(scoreboard_btn)

        exit_btn = QPushButton("Exit")
        exit_btn.setStyleSheet(self.theme["EXIT_BUTTON_STYLE"])
        exit_btn.clicked.connect(self.confirm_exit)  # updated connection
        self.main_menu_layout.addWidget(exit_btn)
        
        # Add the Switch Theme button
        self.switch_theme_button = QPushButton("Switch Theme")
        self.switch_theme_button.setStyleSheet(self.theme["MENU_BUTTON_STYLE"])
        self.switch_theme_button.clicked.connect(self.switch_theme)
        self.main_menu_layout.addWidget(self.switch_theme_button)

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
        for i in range(self.buttons_layout.count()):
            button = self.buttons_layout.itemAt(i).widget()
            button.setStyleSheet(self.theme["MENU_BUTTON_STYLE"])
        # Update styles for scoreboard and exit buttons
        self.main_menu_layout.itemAt(self.main_menu_layout.count() - 3).widget().setStyleSheet(self.theme["SCOREBOARD_BUTTON_STYLE"])
        self.main_menu_layout.itemAt(self.main_menu_layout.count() - 2).widget().setStyleSheet(self.theme["EXIT_BUTTON_STYLE"])
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

    def launch_quiz(self, quiz_name: str):
        self.current_quiz_name = quiz_name
        questions = quiz_mapping.get(quiz_name, Example_questions_form)
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
