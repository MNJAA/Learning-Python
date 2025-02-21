import sys
import random
import time
import winsound
from qs import Example_questions_form, HEM, MGN, HP_TBL_diving, HA, GPT, pharm, HA4mid
import json, os

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QProgressBar, QMessageBox, QRadioButton, QButtonGroup,
    QTextBrowser, QGraphicsOpacityEffect, QTableWidget, QTableWidgetItem, QLineEdit, QInputDialog, QSlider, QHeaderView
)
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import QTimer, Qt, QPropertyAnimation, QEasingCurve

# Import theme dictionaries and helper function
from styles import DARK_THEME, PINK_THEME, get_theme

def load_theme_preference():
    pref_file = "preferences.json"
    if os.path.exists(pref_file):
        with open(pref_file, "r") as file:
            prefs = json.load(file)
            return prefs.get("theme", "dark")
    return "dark"

def save_theme_preference(theme_name):
    with open("preferences.json", "w") as file:
        json.dump({"theme": theme_name}, file, indent=4)

# Mapping of quiz names to question dictionaries; modify as needed.
quiz_mapping = {
    "Embryology": HEM,
    "Medical Genetics": MGN,
    "TBL Quiz": HP_TBL_diving,
    "HA4 Quiz 1": HA,
    "GPT prac Quiz": GPT,
    "pharma": pharm,
    "HA 4 midterm": HA4mid
}

class Scoreboard:
    def __init__(self, filename="scores.json"):
        self.filename = filename
        self.scores = self.load_scores()

    def load_scores(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return {}

    def save_scores(self):
        with open(self.filename, "w") as file:
            json.dump(self.scores, file, indent=4)

    def update_score(self, quiz_name, score, total_questions, elapsed_seconds):
        percentage_score = (score / total_questions) * 100
        formatted_time = self.format_time(elapsed_seconds)
        if quiz_name not in self.scores:
            self.scores[quiz_name] = {
                "highest_score": percentage_score,
                "lowest_score": percentage_score,
                "latest_score": percentage_score,
                "latest_time": formatted_time,
                "min_time": formatted_time,
                "max_time": formatted_time
            }
        else:
            self.scores[quiz_name]["latest_score"] = percentage_score
            self.scores[quiz_name]["latest_time"] = formatted_time
            if percentage_score > self.scores[quiz_name]["highest_score"]:
                self.scores[quiz_name]["highest_score"] = percentage_score
            if percentage_score < self.scores[quiz_name]["lowest_score"]:
                self.scores[quiz_name]["lowest_score"] = percentage_score
            if elapsed_seconds < self.parse_time(self.scores[quiz_name]["min_time"]):
                self.scores[quiz_name]["min_time"] = formatted_time
            if elapsed_seconds > self.parse_time(self.scores[quiz_name]["max_time"]):
                self.scores[quiz_name]["max_time"] = formatted_time
        self.save_scores()

    def get_scores(self):
        return self.scores

    def format_time(self, seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def parse_time(self, time_str):
        hours, minutes, seconds = map(int, time_str.split(":"))
        return hours * 3600 + minutes * 60 + seconds

class Quiz(QMainWindow):
    def __init__(self, questions, main_menu, scoreboard, time_limit=None):
        super().__init__()
        self.main_menu = main_menu
        self.questions = questions
        self.scoreboard = scoreboard
        self.time_limit = time_limit  # Time limit in seconds
        random.shuffle(self.questions)
        self.current_question_index = 0
        self.score = 0
        self.answered_questions = 0
        self.total_questions = len(questions)
        self.incorrect_questions = []
        self.skipped_questions = []
        self.start_time = time.time()
        self.quiz_ended = False
        self.elapsed_seconds = 0
        self.answered_set = set()
        self.photo = None

        self.setWindowState(Qt.WindowMaximized)
        self.setWindowFlag(Qt.FramelessWindowHint, True)  # remove title bar
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("MCQ Quiz")
        # Apply current theme from main_menu
        self.setStyleSheet(self.main_menu.theme["MAIN_WINDOW_STYLE"])

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        self.setup_top_layout()
        self.setup_question_layout()
        self.setup_navigation_layout()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

        self.show_question()

    def setup_top_layout(self):
        self.top_layout = QHBoxLayout()
        self.main_layout.addLayout(self.top_layout)

        self.finish_button = QPushButton("End")
        self.finish_button.setStyleSheet(self.main_menu.theme["NAV_BUTTON_STYLE"])  # updated
        self.finish_button.clicked.connect(self.finish_quiz_early)
        self.top_layout.addWidget(self.finish_button)

        self.feedback_button = QPushButton("Feedback")
        self.feedback_button.setStyleSheet(self.main_menu.theme["NAV_BUTTON_STYLE"])
        self.feedback_button.clicked.connect(self.provide_feedback)
        self.top_layout.addWidget(self.feedback_button)

        self.return_button = QPushButton("Menu")
        self.return_button.setStyleSheet(self.main_menu.theme["RETURN_BUTTON_STYLE"])  # updated
        self.return_button.clicked.connect(self.return_to_menu)
        self.top_layout.addWidget(self.return_button)

        self.timer_label = QLabel("Time: 00:00:00")
        self.timer_label.setStyleSheet("font: 14pt 'Times New Roman'; color: white;")
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.top_layout.addWidget(self.timer_label, stretch=1)

        self.question_number_label = QLabel(f"Question {self.current_question_index + 1} of {self.total_questions}")
        self.question_number_label.setStyleSheet("font: 16pt 'Times New Roman'; color: white;")
        self.top_layout.addWidget(self.question_number_label)

    def setup_question_layout(self):
        self.question_label = QLabel("")
        self.question_label.setWordWrap(True)
        self.question_label.setStyleSheet(self.main_menu.theme["QUESTION_LABEL_STYLE"])
        self.question_label.setAlignment(Qt.AlignCenter)
        self.question_label.setFixedWidth(600)  # Changed from 150 to 600
        self.main_layout.addWidget(self.question_label, alignment=Qt.AlignCenter)  # Added alignment
        self.main_layout.addSpacing(50)

        self.image_label = QLabel("")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.image_label)

        self.answer_layout = QVBoxLayout()
        self.answer_layout.setAlignment(Qt.AlignCenter)
        self.answer_layout.setSpacing(20)  # Increased spacing between options
        self.answer_layout.setContentsMargins(30, 30, 30, 30)  # Increased margins around all options
        self.main_layout.addLayout(self.answer_layout)
        self.button_group = QButtonGroup()
        self.button_group.setExclusive(True)
        self.answer_buttons = []

    def setup_navigation_layout(self):
        self.nav_layout = QHBoxLayout()
        self.main_layout.addLayout(self.nav_layout)

        self.back_button = QPushButton("Back")
        self.back_button.setStyleSheet(self.main_menu.theme["NAV_BUTTON_STYLE"])  # updated
        self.back_button.clicked.connect(self.go_back)
        self.nav_layout.addWidget(self.back_button)

        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet(self.main_menu.theme["NAV_BUTTON_STYLE"])  # updated
        self.submit_button.clicked.connect(self.submit_answer)
        self.nav_layout.addWidget(self.submit_button)

        self.progress = QProgressBar()
        self.progress.setMaximum(self.total_questions)
        self.progress.setValue(self.current_question_index)
        self.progress.setStyleSheet(self.main_menu.theme["PROGRESS_BAR_STYLE"])  # updated
        self.main_layout.addWidget(self.progress)

    def show_question(self):
        for btn in self.answer_buttons:
            self.answer_layout.removeWidget(btn)
            btn.deleteLater()
        self.answer_buttons.clear()
        self.button_group = QButtonGroup()
        self.button_group.setExclusive(True)

        question_data = self.questions[self.current_question_index]
        self.question_label.setText(question_data["question"])

        if ("image" in question_data):
            try:
                pixmap = QPixmap(question_data["image"])
                if not pixmap.isNull():
                    pixmap = pixmap.scaled(400, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    self.image_label.setPixmap(pixmap)
                    self.image_label.show()
                else:
                    self.image_label.clear()
                    self.image_label.hide()
            except Exception:
                self.image_label.clear()
                self.image_label.hide()
        else:
            self.image_label.clear()
            self.image_label.hide()

        all_answers = [question_data["correct_answer"]] + question_data["wrong_answers"]
        random.shuffle(all_answers)
        for i, answer in enumerate(all_answers):
            rb = QRadioButton(answer)
            rb.setStyleSheet(self.main_menu.theme["ANSWER_BUTTON_STYLE"] + """
                color: black;
                font-size: 14pt;
                margin: 30px;  /* Increased from 10px to 30px */
                padding: 5px;
            """)
            self.answer_layout.addWidget(rb)
            self.button_group.addButton(rb, i)
            self.answer_buttons.append(rb)

        self.progress.setValue(self.current_question_index + 1)
        self.question_number_label.setText(f"Question {self.current_question_index + 1} of {self.total_questions}")

    def update_timer(self):
        if not self.quiz_ended:
            self.elapsed_seconds += 1
            if self.time_limit and self.elapsed_seconds >= self.time_limit:
                self.end_quiz()
                return
            remaining_time = self.time_limit - self.elapsed_seconds if self.time_limit else self.elapsed_seconds
            hours = remaining_time // 3600
            minutes = (remaining_time % 3600) // 60
            seconds = remaining_time % 60
            formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
            self.timer_label.setText(f"Time Remaining: {formatted_time}" if self.time_limit else f"Time Elapsed: {formatted_time}")

    def submit_answer(self):
        selected_button = self.button_group.checkedButton()
        selected_answer = selected_button.text() if selected_button else None
        question_data = self.questions[self.current_question_index]
        correct_answer = question_data["correct_answer"]

        # Remove the question from the skipped list if it was previously skipped
        self.skipped_questions = [q for q in self.skipped_questions if q["question_index"] != self.current_question_index]

        if not selected_answer:
            if self.current_question_index not in self.answered_set:
                self.skipped_questions.append({
                    "question": question_data["question"],
                    "correct_answer": correct_answer,
                    "question_index": self.current_question_index
                })
        else:
            if self.current_question_index not in self.answered_set:
                self.answered_set.add(self.current_question_index)
                self.answered_questions += 1
            if selected_answer == correct_answer:
                self.score += 1
                self.incorrect_questions = [q for q in self.incorrect_questions if q["question_index"] != self.current_question_index]
                self.provide_feedback_sound("correct")
            else:
                existing = next((q for q in self.incorrect_questions if q["question_index"] == self.current_question_index), None)
                if existing:
                    existing["selected_answer"] = selected_answer
                else:
                    self.incorrect_questions.append({
                        "question": question_data["question"],
                        "correct_answer": correct_answer,
                        "selected_answer": selected_answer,
                        "question_index": self.current_question_index
                    })
                self.provide_feedback_sound("incorrect")
        self.current_question_index += 1
        if self.current_question_index < self.total_questions:
            self.show_question()
        else:
            self.end_quiz()

    def provide_feedback_sound(self, result):
        if result == "correct":
            winsound.Beep(1000, 200)
        elif result == "incorrect":
            winsound.Beep(300, 200)

    def provide_feedback(self):
        question_data = self.questions[self.current_question_index]
        feedback, ok = QInputDialog.getText(self, "Provide Feedback", "Enter your feedback for this question:")
        if ok and feedback:
            self.save_feedback(question_data["question"], feedback)

    def save_feedback(self, question, feedback):
        feedback_data = {
            "question": question,
            "feedback": feedback,
            "timestamp": time.time()
        }
        feedback_file = "questions_feedback.json"
        if os.path.exists(feedback_file):
            with open(feedback_file, "r") as file:
                feedback_list = json.load(file)
        else:
            feedback_list = []
        feedback_list.append(feedback_data)
        with open(feedback_file, "w") as file:
            json.dump(feedback_list, file, indent=4)

    def fade_in_widget(self, widget):
        effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(effect)
        animation = QPropertyAnimation(effect, b"opacity", widget)
        animation.setDuration(500)
        animation.setStartValue(0)
        animation.setEndValue(1)
        animation.setEasingCurve(QEasingCurve.InOutQuad)
        animation.start(QPropertyAnimation.DeleteWhenStopped)

    def show_incorrect_list(self):
        if not self.incorrect_questions:
            html = "<p style='font-size:14pt; color:white;'>No Incorrect Answers.</p>"
        else:
            html = "<ol>"
            for q in self.incorrect_questions:
                html += "<li style='margin-bottom:10px;'>"
                html += f"<p style='font-size:16pt; color:white;'><b>Question:</b> {q['question']}</p>"
                html += f"<p style='font-size:16pt; color:yellow;'><b>Your Answer:</b> {q.get('selected_answer', 'No Answer')}</p>"
                html += f"<p style='font-size:16pt; color:#3fff00;'><b>Correct Answer:</b> {q['correct_answer']}</p>"
                html += "</li>"
            html += "</ol>"
        self.detail_browser.setHtml(html)
        self.fade_in_widget(self.detail_browser)

    def show_skipped_list(self):
        if not self.skipped_questions:
            html = "<p style='font-size:14pt; color:white;'>No Skipped Questions.</p>"
        else:
            html = "<ol>"
            for q in self.skipped_questions:
                html += "<li style='margin-bottom:10px;'>"
                html += f"<p style='font-size:16pt; color:white;'><b>Question:</b> {q['question']}</p>"
                html += f"<p style='font-size:16pt; color:#3fff00;'><b>Correct Answer:</b> {q['correct_answer']}</p>"
                html += "</li>"
            html += "</ol>"
        self.detail_browser.setHtml(html)
        self.fade_in_widget(self.detail_browser)

    def end_quiz(self):
        self.quiz_ended = True
        self.timer.stop()
        self.scoreboard.update_score(self.main_menu.current_quiz_name, self.score, self.total_questions, self.elapsed_seconds)
        hours = self.elapsed_seconds // 3600
        minutes = (self.elapsed_seconds % 3600) // 60
        seconds = (self.elapsed_seconds % 60)
        formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
        self.question_label.deleteLater()
        self.image_label.deleteLater()
        for btn in self.answer_buttons:
            btn.deleteLater()
        self.window().widget().deleteLater()
        
        self.results_widget = QWidget()
        self.results_layout = QVBoxLayout(self.results_widget)
        score_label = QLabel(f"Quiz Over! Your score: {self.score}/{self.answered_questions}")
        score_label.setStyleSheet(self.main_menu.theme["RESULTS_LABEL_STYLE"])  # updated
        self.results_layout.addWidget(score_label)
        time_label = QLabel(f"Time Taken: {formatted_time}")
        time_label.setStyleSheet("font: 14pt 'Times New Roman'; color: white;")
        self.results_layout.addWidget(time_label)
        btn_layout = QHBoxLayout()
        self.incorrect_btn = QPushButton("Show Incorrect Answers")
        self.skipped_btn = QPushButton("Show Skipped Questions")
        self.incorrect_btn.setStyleSheet(self.main_menu.theme["INCORRECT_BUTTON_STYLE"])  # updated
        self.skipped_btn.setStyleSheet(self.main_menu.theme["SKIPPED_BUTTON_STYLE"])  # updated
        self.incorrect_btn.clicked.connect(self.show_incorrect_list)
        self.skipped_btn.clicked.connect(self.show_skipped_list)
        btn_layout.addWidget(self.incorrect_btn)
        btn_layout.addWidget(self.skipped_btn)
        self.results_layout.addLayout(btn_layout)
        self.detail_browser = QTextBrowser()
        self.detail_browser.setStyleSheet("background-color: #2E3440; color: white; font: 14pt 'Times New Roman';")
        self.results_layout.addWidget(self.detail_browser)
        self.detail_browser.setHtml("<p style='color:white;'>Click a button above to view details.</p>")

        # Add feedback section
        self.feedback_input = QLineEdit()
        self.feedback_input.setStyleSheet(self.main_menu.theme["FEEDBACK_INPUT_STYLE"])  # updated
        self.feedback_input.setPlaceholderText("Write your feedback")
        self.results_layout.addWidget(self.feedback_input)

        self.submit_feedback_button = QPushButton("Submit Feedback")
        self.submit_feedback_button.setStyleSheet(self.main_menu.theme["SUBMIT_FEEDBACK_BUTTON_STYLE"])  # updated
        self.submit_feedback_button.clicked.connect(self.submit_feedback)
        self.results_layout.addWidget(self.submit_feedback_button)

        # Add Return to Main Menu button
        self.return_to_menu_btn = QPushButton("Menu")
        self.return_to_menu_btn.setStyleSheet(self.main_menu.theme["RETURN_BUTTON_STYLE"])  # updated
        self.return_to_menu_btn.clicked.connect(self.return_to_menu)
        self.results_layout.addWidget(self.return_to_menu_btn)
        
        self.main_layout.addWidget(self.results_widget)

    def submit_feedback(self):
        feedback = self.feedback_input.text()
        rating = self.rating_slider.value()
        feedback_data = {
            "quiz_name": self.main_menu.current_quiz_name,
            "feedback": feedback,
            "rating": rating,
            "timestamp": time.time()
        }
        feedback_file = "quiz_feedback.json"
        if os.path.exists(feedback_file):
            with open(feedback_file, "r") as file:
                feedback_list = json.load(file)
        else:
            feedback_list = []
        feedback_list.append(feedback_data)
        with open(feedback_file, "w") as file:
            json.dump(feedback_list, file, indent=4)
        QMessageBox.information(self, "Feedback Submitted", "Thank you for your feedback!")

    def finish_quiz_early(self):
        reply = QMessageBox.question(self, "Finish Quiz", "Are you sure you want to finish the quiz early?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.end_quiz()

    def go_back(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.show_question()

    def return_to_menu(self):
        self.hide()
        self.main_menu.main_layout.removeWidget(self)
        self.main_menu.main_menu_widget.show()
        self.deleteLater()

class ScoreboardWidget(QWidget):
    def __init__(self, main_menu, scoreboard, return_to_menu_callback):
        super().__init__()
        self.main_menu = main_menu  # store reference to main_menu
        self.scoreboard = scoreboard
        self.return_to_menu_callback = return_to_menu_callback
        self.setup_ui()

    def setup_ui(self):
        self.setLayout(QVBoxLayout())
        title = QLabel("Scoreboard")
        title.setStyleSheet("font: 20pt 'Times New Roman'; color: #88C0D0;")
        title.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(title)

        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["Subject", "Last", "Min", "High", "Latest Time", "Min Time", "High Time"])
        self.table.setAlternatingRowColors(True)
        self.table.setStyleSheet(self.main_menu.theme["SCOREBOARD_STYLE"])  # updated
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.layout().addWidget(self.table)

        self.return_to_menu_btn = QPushButton("Return to Main Menu")
        self.return_to_menu_btn.setStyleSheet(self.main_menu.theme["RETURN_BUTTON_STYLE"])  # updated
        self.return_to_menu_btn.clicked.connect(self.return_to_menu_callback)
        self.layout().addWidget(self.return_to_menu_btn)

    def update_scores(self):
        scores = self.scoreboard.get_scores()
        self.table.setRowCount(len(scores))
        for row, (quiz_name, score_data) in enumerate(scores.items()):
            self.table.setItem(row, 0, QTableWidgetItem(quiz_name))
            last_item = QTableWidgetItem(f"{score_data['latest_score']:.2f}%")
            last_item.setForeground(Qt.yellow)
            last_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row, 1, last_item)
            min_item = QTableWidgetItem(f"{score_data['lowest_score']:.2f}%")
            min_item.setForeground(Qt.red)
            min_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row, 2, min_item)
            high_item = QTableWidgetItem(f"{score_data['highest_score']:.2f}%")
            high_item.setForeground(Qt.green)
            high_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row, 3, high_item)
            latest_time_item = QTableWidgetItem(score_data["latest_time"])
            latest_time_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row, 4, latest_time_item)
            min_time_item = QTableWidgetItem(score_data["min_time"])
            min_time_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row, 5, min_time_item)
            max_time_item = QTableWidgetItem(score_data["max_time"])
            max_time_item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row, 6, max_time_item)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def return_to_menu_callback(self):
        self.hide()
        self.main_menu.main_layout.removeWidget(self)
        self.main_menu.show()
        self.deleteLater()

class MainMenu(QMainWindow):
    def __init__(self, scoreboard):
        super().__init__()
        self.scoreboard = scoreboard
        self.current_quiz_name = None
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
            "HA 4 midterm"  # Added this line
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
        exit_btn.clicked.connect(self.close)
        self.main_menu_layout.addWidget(exit_btn)
        
        # Add the Switch Theme button
        self.switch_theme_button = QPushButton("Switch Theme")
        self.switch_theme_button.setStyleSheet(self.theme["MENU_BUTTON_STYLE"])
        self.switch_theme_button.clicked.connect(self.switch_theme)
        self.main_menu_layout.addWidget(self.switch_theme_button)

        self.main_layout.addWidget(self.main_menu_widget)

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
            self.scoreboard_widget = ScoreboardWidget(self.scoreboard, self.return_to_menu)
            self.scoreboard_widget.update_scores()
            self.main_layout.addWidget(self.scoreboard_widget)
        save_theme_preference(self.current_theme)

    def launch_quiz(self, quiz_name):
        self.current_quiz_name = quiz_name
        questions = quiz_mapping.get(quiz_name, Example_questions_form)
        time_limit = int(self.time_limit_input.text()) * 60 if self.time_limit_input.text().isdigit() else None
        self.quiz_widget = Quiz(questions, self, self.scoreboard, time_limit)
        self.main_layout.addWidget(self.quiz_widget)
        self.main_menu_widget.hide()
        self.quiz_widget.show()

    def show_scoreboard(self):
        self.scoreboard_widget = ScoreboardWidget(self, self.scoreboard, self.return_to_menu)  # pass self (main_menu)
        self.scoreboard_widget.update_scores()
        self.main_layout.addWidget(self.scoreboard_widget)
        self.main_menu_widget.hide()
        self.scoreboard_widget.show()

    def return_to_menu(self):
        if hasattr(self, 'quiz_widget'):
            self.main_layout.removeWidget(self.quiz_widget)
            self.quiz_widget.deleteLater()
            del self.quiz_widget
        if hasattr(self, 'scoreboard_widget'):
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
