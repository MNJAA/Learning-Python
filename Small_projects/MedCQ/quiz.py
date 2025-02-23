import sys
import random
import time
import winsound
import json, os
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QProgressBar, QMessageBox, QRadioButton, QButtonGroup,
    QTextBrowser, QGraphicsOpacityEffect, QTableWidget, QTableWidgetItem, QLineEdit, QInputDialog,
    QMenu, QFrame, QGridLayout, QScrollArea, QWidgetAction, QSlider
)
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import QTimer, Qt, QPropertyAnimation, QEasingCurve, QPoint  # Added QPoint

class QuestionNavigator(QMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(400, 600)
        
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_layout.setSpacing(4)  # Reduced spacing
        self.main_layout.setContentsMargins(10, 10, 10, 10)  # Reduced margins
        
        # Header setup
        header = QLabel("Question Navigator")
        header.setStyleSheet("""
            font: bold 14pt 'Segoe UI';
            color: white;
            background-color: #2E236C;
            padding: 8px;
            border-radius: 4px;
        """)
        header.setAlignment(Qt.AlignCenter)
        
        # Compact legend in a horizontal layout
        legend_layout = QHBoxLayout()
        legend_layout.setSpacing(15)  # Space between legend items
        legend_layout.setContentsMargins(5, 0, 5, 0)  # Minimal vertical space
        
        # Simplified legend items
        for text, color, symbol in [
            ("Not answered", "white", "○"),
            ("Answered", "#90EE90", "●"),
            ("Skipped", "#FFB6C6", "×")
        ]:
            item_layout = QHBoxLayout()
            item_layout.setSpacing(2)  # Minimal space between icon and text
            
            icon = QLabel(symbol)
            icon.setStyleSheet(f"color: {color}; font: bold 12pt;")  # Smaller icons
            
            label = QLabel(text)
            label.setStyleSheet(f"color: {color}; font: 9pt 'Segoe UI';")
            
            item_layout.addWidget(icon)
            item_layout.addWidget(label)
            
            container = QWidget()
            container.setLayout(item_layout)
            legend_layout.addWidget(container)
        
        legend_layout.addStretch()  # Push items to the left
        
        # Search box setup
        self.jump_input = QLineEdit()
        self.jump_input.setPlaceholderText("Jump to question...")
        self.jump_input.setStyleSheet("""
            QLineEdit {
                background-color: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 4px;
                color: white;
                padding: 5px 8px;
                font: 11pt 'Segoe UI';
                min-height: 25px;
            }
        """)
        self.jump_input.returnPressed.connect(self.jump_to_question)
        
        # Scrollable grid setup
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setStyleSheet("""
            QScrollArea { 
                border: none;
                background-color: transparent;
            }
            QScrollBar:vertical {
                border: none;
                background: rgba(255, 255, 255, 0.1);
                width: 8px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background: rgba(255, 255, 255, 0.3);
                border-radius: 4px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
        """)
        
        container = QWidget()
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(4)  # Reduced from 6 to 4
        self.grid_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        container.setLayout(self.grid_layout)
        scroll.setWidget(container)
        
        # Add widgets to main layout with minimal spacing
        self.main_layout.addWidget(header)
        self.main_layout.addSpacing(2)
        self.main_layout.addLayout(legend_layout)
        self.main_layout.addSpacing(2)
        self.main_layout.addWidget(self.jump_input)
        self.main_layout.addSpacing(2)
        self.main_layout.addWidget(scroll, 1)
        
        # Add main_widget to the menu using QWidgetAction
        widget_action = QWidgetAction(self)
        widget_action.setDefaultWidget(self.main_widget)
        self.addAction(widget_action)
        
        self.setFocusPolicy(Qt.StrongFocus)

    def jump_to_question(self):
        try:
            question_num = int(self.jump_input.text())
            if 1 <= question_num <= self.total_questions:
                self.on_question_selected(question_num - 1)
                self.hide()
        except ValueError:
            pass
        self.jump_input.clear()

    def update_questions(self, total_questions, answered_set, skipped_indices, current_index, on_question_selected):
        self.total_questions = total_questions
        self.on_question_selected = on_question_selected
        
        # Clear existing buttons
        while self.grid_layout.count():
            item = self.grid_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Create new grid of question buttons
        for i in range(total_questions):
            btn = QPushButton(str(i + 1))
            btn.setFixedSize(35, 35)  # Reduced from 40x40 to 35x35
            
            # Set color and style based on question state
            if i in answered_set:
                status = "answered"
                color = "#90EE90"
                hover_color = "#70CE70"
                tooltip = "Answered"
            elif i in skipped_indices:
                status = "skipped"
                color = "#FFB6C6"
                hover_color = "#FFB6B6"
                tooltip = "Skipped"
            else:
                status = "unanswered"
                color = "white"
                hover_color = "#CCCCCC"
                tooltip = "Not answered yet"
            
            # Highlight current question
            border = "2px solid #FFF700" if i == current_index else "1px solid rgba(255, 255, 255, 0.2)"
            
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    border: {border};
                    border-radius: 5px;
                    font: bold 10pt 'Segoe UI';
                    color: black;
                }}
                QPushButton:hover {{
                    background-color: {hover_color};
                    border: 2px solid white;
                }}
            """)
            
            btn.setToolTip(f"Question {i+1}: {tooltip}")
            btn.clicked.connect(lambda checked, idx=i: on_question_selected(idx))
            self.grid_layout.addWidget(btn, i // 8, i % 8)  # Changed from 5 columns to 8 columns

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.hide()
        elif event.key() in (Qt.Key_Return, Qt.Key_Enter):
            if self.jump_input.hasFocus():
                self.jump_to_question()
        super().keyPressEvent(event)

class Quiz(QMainWindow):
    def __init__(self, questions, main_menu, scoreboard, time_limit=None):
        super().__init__()
        # Initialize basic attributes
        self.questions = questions
        self.main_menu = main_menu
        self.scoreboard = scoreboard
        self.time_limit = time_limit
        self.total_questions = len(questions)
        self.current_question_index = 0
        self.score = 0
        self.answered_questions = 0
        self.elapsed_seconds = 0
        self.quiz_ended = False
        
        # Initialize collections for tracking
        self.answer_buttons = []  # for radio buttons
        self.answer_widgets = []  # add this list for container widgets
        self.incorrect_questions = []
        self.skipped_questions = []
        self.answered_set = set()
        
        # Window setup
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowFlag(Qt.FramelessWindowHint, True)
        
        # Initialize UI components that will be set up later
        self.central_widget = None
        self.main_layout = None
        self.question_label = None
        self.image_label = None
        self.answer_layout = None
        self.button_group = None
        self.progress = None
        self.question_number_label = None
        self.timer_label = None
        self.detail_browser = None
        
        # Set up the UI
        self.setup_ui()
        
        # Start timer if time limit is set
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)  # Start timer immediately

    def setup_ui(self):
        self.setWindowTitle("MCQ Quiz")
        self.setStyleSheet(self.main_menu.theme["MAIN_WINDOW_STYLE"])

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        self.setup_top_layout()
        self.setup_question_layout()
        self.setup_navigation_layout()  # Ensure this method is defined

        self.show_question()

    def setup_top_layout(self):
        self.top_layout = QHBoxLayout()
        self.main_layout.addLayout(self.top_layout)

        # Left side buttons
        self.finish_button = QPushButton("End")
        self.finish_button.setStyleSheet(self.main_menu.theme["NAV_BUTTON_STYLE"])
        self.finish_button.clicked.connect(self.finish_quiz_early)
        self.top_layout.addWidget(self.finish_button)

        self.feedback_button = QPushButton("Feedback")
        self.feedback_button.setStyleSheet(self.main_menu.theme["NAV_BUTTON_STYLE"])
        self.feedback_button.clicked.connect(self.provide_feedback)
        self.top_layout.addWidget(self.feedback_button)

        self.return_button = QPushButton("Menu")
        self.return_button.setStyleSheet(self.main_menu.theme["RETURN_BUTTON_STYLE"])
        self.return_button.clicked.connect(self.return_to_menu)
        self.top_layout.addWidget(self.return_button)

        # Center timer with stretch
        self.timer_label = QLabel("Time: 00:00:00")
        self.timer_label.setStyleSheet("font: 14pt 'Times New Roman'; color: white;")
        self.timer_label.setAlignment(Qt.AlignCenter)
        self.top_layout.addWidget(self.timer_label, stretch=1)

        # Question tracking container (moved navigation button to the left)
        question_tracking_container = QHBoxLayout()
        question_tracking_container.setSpacing(5)  # Small gap between button and label

        # Add navigation dropdown button before question number
        self.nav_dropdown_btn = QPushButton("☰")
        self.nav_dropdown_btn.setFixedSize(30, 30)
        self.nav_dropdown_btn.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                background-color: #433D8B;
                color: #ECDBBA;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2E236C;
            }
        """)
        self.nav_dropdown_btn.clicked.connect(self.show_question_navigator)
        question_tracking_container.addWidget(self.nav_dropdown_btn)

        self.question_number_label = QLabel(f"Question {self.current_question_index + 1} of {self.total_questions}")
        self.question_number_label.setStyleSheet("font: 16pt 'Times New Roman'; color: white;")
        question_tracking_container.addWidget(self.question_number_label)

        # Add the question tracking container to the main layout
        self.top_layout.addLayout(question_tracking_container)

        # Create question navigator menu
        self.question_navigator = QuestionNavigator(self)

    def show_question_navigator(self):
        # Get current skipped question indices
        skipped_indices = {q["question_index"] for q in self.skipped_questions}
        
        # Update navigator and show it
        self.question_navigator.update_questions(
            self.total_questions,
            self.answered_set,
            skipped_indices,
            self.current_question_index,
            self.navigate_to_question
        )
        
        # Position menu to the left of the button
        button_pos = self.nav_dropdown_btn.mapToGlobal(self.nav_dropdown_btn.rect().topLeft())
        menu_x = button_pos.x() - self.question_navigator.width()  # Position to the left
        menu_y = button_pos.y()  # Align with top of button
        self.question_navigator.popup(QPoint(menu_x, menu_y))  # Using QPoint directly

    def navigate_to_question(self, index):
        if 0 <= index < self.total_questions:
            self.current_question_index = index
            self.show_question()
            self.question_navigator.hide()

    def setup_question_layout(self):
        # Create main content layout with spacing and margins
        self.content_layout = QHBoxLayout()
        self.content_layout.setSpacing(20)
        self.content_layout.setContentsMargins(20, 20, 20, 20)

        # Create scrollable image container
        self.image_container = QScrollArea()
        self.image_container.setWidgetResizable(True)
        self.image_container.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.image_container.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.image_container.setMinimumWidth(600)  # Set minimum width
        self.image_container.setMaximumWidth(800)  # Set maximum width
        
        image_widget = QWidget()
        self.image_layout = QVBoxLayout(image_widget)
        self.image_layout.setAlignment(Qt.AlignCenter)
        
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setMinimumSize(580, 580)  # Slightly smaller than container
        self.image_label.setScaledContents(False)  # Don't scale contents automatically
        
        self.image_layout.addWidget(self.image_label)
        self.image_container.setWidget(image_widget)

        # Create question and answers container
        self.qa_container = QWidget()
        self.qa_layout = QVBoxLayout(self.qa_container)
        self.qa_layout.setAlignment(Qt.AlignTop)  # Align to top
        self.qa_layout.setSpacing(30)  # Increased spacing between elements

        # Question label setup
        self.question_label = QLabel()
        self.question_label.setWordWrap(True)
        self.question_label.setStyleSheet(self.main_menu.theme["QUESTION_LABEL_STYLE"])
        self.question_label.setAlignment(Qt.AlignCenter)
        self.question_label.setMinimumWidth(800)  # Set minimum width
        self.qa_layout.addWidget(self.question_label)

        # Answer options container
        self.answer_container = QWidget()
        self.answer_layout = QVBoxLayout(self.answer_container)
        self.answer_layout.setAlignment(Qt.AlignTop)  # Align to top
        self.answer_layout.setSpacing(15)
        self.answer_layout.setContentsMargins(20, 20, 20, 20)

        # Create a fixed-width container for answers
        answer_width_container = QWidget()
        answer_width_container.setMinimumWidth(800)  # Set minimum width
        answer_width_container.setMaximumWidth(1200)  # Set maximum width
        answer_width_container.setLayout(self.answer_layout)

        self.qa_layout.addWidget(answer_width_container, alignment=Qt.AlignHCenter)

        # Add containers to content layout
        self.content_layout.addWidget(self.image_container)
        self.content_layout.addWidget(self.qa_container, stretch=1)

        # Add content layout to main layout
        self.main_layout.addLayout(self.content_layout)
        self.main_layout.addSpacing(30)

        # Initialize button group and answer buttons list
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
        # Clear previous answer option containers
        for widget in self.answer_widgets:
            self.answer_layout.removeWidget(widget)
            widget.deleteLater()
        self.answer_widgets.clear()
        self.answer_buttons.clear()
        self.button_group = QButtonGroup()
        self.button_group.setExclusive(True)

        question_data = self.questions[self.current_question_index]
        self.question_label.setText(question_data["question"])

        # Handle image
        if "image" in question_data:
            image_path = question_data["image"]
            if os.path.exists(image_path):
                try:
                    pixmap = QPixmap(image_path)
                    if not pixmap.isNull():
                        # Calculate scaling while preserving aspect ratio
                        available_width = self.image_label.width() - 20  # Subtract padding
                        available_height = self.image_label.height() - 20  # Subtract padding
                        
                        # Scale pixmap while maintaining aspect ratio
                        scaled_pixmap = pixmap.scaled(
                            available_width,
                            available_height,
                            Qt.KeepAspectRatio,
                            Qt.SmoothTransformation
                        )
                        
                        self.image_label.setPixmap(scaled_pixmap)
                        self.image_container.show()
                    else:
                        self.image_label.clear()
                        self.image_container.hide()
                except Exception as e:
                    print(f"Error loading image: {e}")
                    self.image_label.clear()
                    self.image_container.hide()
            else:
                print(f"Image not found: {image_path}")
                self.image_label.clear()
                self.image_container.hide()
        else:
            self.image_label.clear()
            self.image_container.hide()

        # Handle answers
        all_answers = [question_data["correct_answer"]] + question_data["wrong_answers"]
        random.shuffle(all_answers)
        for i, answer in enumerate(all_answers):
            if isinstance(answer, list):
                answer = " ".join(str(item) for item in answer)

            # Create container for the radio button to handle wrapping
            container = QWidget()
            container_layout = QHBoxLayout(container)
            container_layout.setContentsMargins(0, 0, 0, 0)

            rb = QRadioButton()
            rb.setText(str(answer))
            rb.setStyleSheet(self.main_menu.theme["ANSWER_BUTTON_STYLE"] + """
                QRadioButton {
                    padding: 15px 20px;
                    margin: 5px;
                    font-size: 14pt;
                    min-width: 500px;
                    max-width: 1000px;
                }
                QRadioButton::indicator {
                    width: 20px;
                    height: 20px;
                    margin-right: 10px;
                }
            """)
            container.setFixedWidth(1200)  # Fixed width for container
            container_layout.addWidget(rb, alignment=Qt.AlignLeft)

            self.answer_layout.addWidget(container, alignment=Qt.AlignCenter)
            self.button_group.addButton(rb, i)
            self.answer_buttons.append(rb)
            self.answer_widgets.append(container)

        self.progress.setValue(self.current_question_index + 1)
        self.question_number_label.setText(f"Question {self.current_question_index + 1} of {self.total_questions}")

    def update_timer(self):
        if not self.quiz_ended:
            self.elapsed_seconds += 1
            if self.time_limit and self.elapsed_seconds >= self.time_limit:
                self.end_quiz()
                return
            
            if self.time_limit:
                remaining_time = self.time_limit - self.elapsed_seconds
                hours = remaining_time // 3600
                minutes = (remaining_time % 3600) // 60
                seconds = remaining_time % 60
                formatted_time = f"Time Remaining: {hours:02}:{minutes:02}:{seconds:02}"
            else:
                hours = self.elapsed_seconds // 3600
                minutes = (self.elapsed_seconds % 3600) // 60
                seconds = self.elapsed_seconds % 60
                formatted_time = f"Time Elapsed: {hours:02}:{minutes:02}:{seconds:02}"
                
            self.timer_label.setText(formatted_time)

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

        # Remove quiz widgets
        self.central_widget.deleteLater()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

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

        # Feedback section
        self.feedback_input = QLineEdit()
        self.feedback_input.setStyleSheet(self.main_menu.theme["FEEDBACK_INPUT_STYLE"])  # updated
        self.feedback_input.setPlaceholderText("Write your feedback")
        self.results_layout.addWidget(self.feedback_input)

        self.submit_feedback_button = QPushButton("Submit Feedback")
        self.submit_feedback_button.setStyleSheet(self.main_menu.theme["SUBMIT_FEEDBACK_BUTTON_STYLE"])
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
        feedback_data = {
            "quiz_name": self.main_menu.current_quiz_name,
            "feedback": feedback,
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
