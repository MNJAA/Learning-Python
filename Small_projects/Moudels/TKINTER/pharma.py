import sys
import random
import time
import winsound  # For playing sounds on Windows
from qs import pharm, Example_questions_form  # Import your questions from qs.py

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QProgressBar, QMessageBox, QRadioButton, QButtonGroup,
    QTextBrowser, QGraphicsOpacityEffect
)
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import QTimer, Qt, QPropertyAnimation, QEasingCurve

class Quiz(QMainWindow):
    def __init__(self, questions):
        super().__init__()
        self.questions = questions
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
        self.photo = None  # To hold QPixmap reference

        self.setWindowTitle("MCQ Quiz")
        self.resize(1100, 600)
        self.setStyleSheet("background-color: #2E3440;")

        # Central widget and main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # ------------------- Top Layout -------------------
        self.top_layout = QHBoxLayout()
        self.main_layout.addLayout(self.top_layout)

        # Finish Early button
        self.finish_button = QPushButton("Finish Early")
        self.finish_button.setStyleSheet("background-color: #5E81AC; color: black; font: 16pt 'Times New Roman';")
        self.finish_button.clicked.connect(self.finish_quiz_early)
        self.top_layout.addWidget(self.finish_button)

        # Timer label
        self.timer_label = QLabel("Time: 00:00:00")
        self.timer_label.setStyleSheet("font: 14pt 'Times New Roman'; color: white;")
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.top_layout.addWidget(self.timer_label, stretch=1)

        # Question number label
        self.question_number_label = QLabel(f"Question {self.current_question_index + 1} of {self.total_questions}")
        self.question_number_label.setStyleSheet("font: 16pt 'Times New Roman'; color: white;")
        self.top_layout.addWidget(self.question_number_label)

        # ------------------- Question & Image -------------------
        self.question_label = QLabel("")
        self.question_label.setWordWrap(True)
        self.question_label.setStyleSheet("font: 16pt 'Times New Roman'; color: white;")
        self.question_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.question_label)

        self.image_label = QLabel("")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.image_label)

        # ------------------- Answer Options -------------------
        self.answer_layout = QVBoxLayout()
        self.answer_layout.setAlignment(Qt.AlignCenter)  # Center the choices under the question
        self.main_layout.addLayout(self.answer_layout)
        self.button_group = QButtonGroup()
        self.button_group.setExclusive(True)
        self.answer_buttons = []

        # ------------------- Bottom Layout (Navigation & Progress) -------------------
        self.bottom_layout = QVBoxLayout()
        self.main_layout.addLayout(self.bottom_layout)

        # Navigation buttons
        self.nav_layout = QHBoxLayout()
        self.bottom_layout.addLayout(self.nav_layout)

        self.back_button = QPushButton("Back")
        self.back_button.setStyleSheet("background-color: #5E81AC; color: black; font: 16pt 'Times New Roman';")
        self.back_button.clicked.connect(self.go_back)
        self.nav_layout.addWidget(self.back_button)

        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet("background-color: #5E81AC; color: black; font: 16pt 'Times New Roman';")
        self.submit_button.clicked.connect(self.submit_answer)
        self.nav_layout.addWidget(self.submit_button)

        # Progress bar
        self.progress = QProgressBar()
        self.progress.setMaximum(self.total_questions)
        self.progress.setValue(self.current_question_index)
        self.progress.setStyleSheet("QProgressBar { background-color: #3B4252; color: white; }")
        self.bottom_layout.addWidget(self.progress)

        # ------------------- Timer -------------------
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

        # Display the first question
        self.show_question()

    def show_question(self):
        # Clear previous answer options
        for btn in self.answer_buttons:
            self.answer_layout.removeWidget(btn)
            btn.deleteLater()
        self.answer_buttons.clear()
        self.button_group = QButtonGroup()
        self.button_group.setExclusive(True)

        question_data = self.questions[self.current_question_index]
        self.question_label.setText(question_data["question"])

        # Check for an image
        if "image" in question_data:
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
            rb.setStyleSheet("font: 16pt 'Times New Roman'; color: white; background-color: #2E3440;")
            self.answer_layout.addWidget(rb)
            self.button_group.addButton(rb, i)
            self.answer_buttons.append(rb)

        self.progress.setValue(self.current_question_index + 1)
        self.question_number_label.setText(f"Question {self.current_question_index + 1} of {self.total_questions}")

    def update_timer(self):
        if not self.quiz_ended:
            self.elapsed_seconds += 1
            hours = self.elapsed_seconds // 3600
            minutes = (self.elapsed_seconds % 3600) // 60
            seconds = self.elapsed_seconds % 60
            formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
            self.timer_label.setText(f"Time Elapsed: {formatted_time}")

    def submit_answer(self):
        selected_button = self.button_group.checkedButton()
        selected_answer = selected_button.text() if selected_button else None

        question_data = self.questions[self.current_question_index]
        correct_answer = question_data["correct_answer"]

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
                self.incorrect_questions = [
                    q for q in self.incorrect_questions
                    if q["question_index"] != self.current_question_index
                ]
                self.provide_feedback("correct")
            else:
                existing = next(
                    (q for q in self.incorrect_questions if q["question_index"] == self.current_question_index),
                    None
                )
                if existing:
                    existing["selected_answer"] = selected_answer
                else:
                    self.incorrect_questions.append({
                        "question": question_data["question"],
                        "correct_answer": correct_answer,
                        "selected_answer": selected_answer,
                        "question_index": self.current_question_index
                    })
                self.provide_feedback("incorrect")

        self.current_question_index += 1
        if self.current_question_index < self.total_questions:
            self.show_question()
        else:
            self.end_quiz()

    def provide_feedback(self, result):
        # Play a high-pitched beep for correct and a low-pitched beep for incorrect answers
        if result == "correct":
            winsound.Beep(1000, 200)  # High pitch (1000 Hz) for 200ms
        elif result == "incorrect":
            winsound.Beep(300, 200)   # Low pitch (300 Hz) for 200ms

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
        hours = self.elapsed_seconds // 3600
        minutes = (self.elapsed_seconds % 3600) // 60
        seconds = self.elapsed_seconds % 60
        formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"

        # Remove/destroy quiz widgets
        self.question_label.deleteLater()
        self.image_label.deleteLater()
        for btn in self.answer_buttons:
            btn.deleteLater()
        self.submit_button.deleteLater()
        self.back_button.deleteLater()
        self.finish_button.deleteLater()
        self.progress.deleteLater()

        # Create a new results widget
        self.results_widget = QWidget()
        self.results_layout = QVBoxLayout(self.results_widget)
        score_label = QLabel(f"Quiz Over! Your score: {self.score}/{self.answered_questions}")
        score_label.setStyleSheet("font: 18pt 'Times New Roman'; color: white;")
        self.results_layout.addWidget(score_label)
        time_label = QLabel(f"Time Elapsed: {formatted_time}")
        time_label.setStyleSheet("font: 14pt 'Times New Roman'; color: white;")
        self.results_layout.addWidget(time_label)

        # Buttons to switch between Incorrect and Skipped question views
        btn_layout = QHBoxLayout()
        self.incorrect_btn = QPushButton("Show Incorrect Answers")
        self.skipped_btn = QPushButton("Show Skipped Questions")
        self.incorrect_btn.setStyleSheet("font: 14pt 'Times New Roman'; color: red; background-color: #5E81AC;")
        self.skipped_btn.setStyleSheet("font: 14pt 'Times New Roman'; color: orange; background-color: #5E81AC;")
        self.incorrect_btn.clicked.connect(self.show_incorrect_list)
        self.skipped_btn.clicked.connect(self.show_skipped_list)
        btn_layout.addWidget(self.incorrect_btn)
        btn_layout.addWidget(self.skipped_btn)
        self.results_layout.addLayout(btn_layout)

        # Create a scrollable, read-only text browser for displaying details
        self.detail_browser = QTextBrowser()
        self.detail_browser.setStyleSheet("background-color: #2E3440; color: white; font: 14pt 'Times New Roman';")
        self.results_layout.addWidget(self.detail_browser)
        # Set an initial message
        self.detail_browser.setHtml("<p style='color:white;'>Click a button above to view details.</p>")

        self.main_layout.addWidget(self.results_widget)

    def finish_quiz_early(self):
        reply = QMessageBox.question(
            self, "Finish Quiz",
            "Are you sure you want to finish the quiz early?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.end_quiz()

    def go_back(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.show_question()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    exam_questions = pharm
    quiz = Quiz(exam_questions)
    quiz.show()
    sys.exit(app.exec())
