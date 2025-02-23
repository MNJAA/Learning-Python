import json
import os
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton, QHeaderView
)
from PySide6.QtCore import Qt

class Scoreboard:
    def __init__(self, filename: str = "scores.json") -> None:
        """Initialize scoreboard with a filename."""
        self.filename = filename
        self.scores = self.load_scores()

    def load_scores(self) -> dict:
        """Load scores from a JSON file."""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r") as file:
                    return json.load(file)
        except Exception as e:
            print(f"Error reading scores: {e}")
        return {}

    def save_scores(self) -> None:
        """Save scores to a JSON file."""
        try:
            with open(self.filename, "w") as file:
                json.dump(self.scores, file, indent=4)
        except Exception as e:
            print(f"Error saving scores: {e}")

    def update_score(self, quiz_name: str, score: float, total_questions: int, elapsed_seconds: int) -> None:
        """Update the scoreboard with a new score entry."""
        percentage_score = (score / total_questions) * 100
        formatted_time = self.format_time(elapsed_seconds)
        if (quiz_name not in self.scores):
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

    def get_scores(self) -> dict:
        """Return stored scores."""
        return self.scores

    def format_time(self, seconds: int) -> str:
        """Format seconds into HH:MM:SS string."""
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def parse_time(self, time_str: str) -> int:
        """Convert HH:MM:SS string into total seconds."""
        hours, minutes, seconds = map(int, time_str.split(":"))
        return hours * 3600 + minutes * 60 + seconds

class ScoreboardWidget(QWidget):
    def __init__(self, main_menu, scoreboard):
        super().__init__()
        self.main_menu = main_menu
        self.scoreboard = scoreboard
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
        self.table.setStyleSheet(self.main_menu.theme["SCOREBOARD_STYLE"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)
        self.layout().addWidget(self.table)

        self.return_to_menu_btn = QPushButton("Return to Main Menu")
        self.return_to_menu_btn.setStyleSheet(self.main_menu.theme["RETURN_BUTTON_STYLE"])
        self.return_to_menu_btn.clicked.connect(self.return_to_menu)
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

    def return_to_menu(self):
        self.hide()
        self.main_menu.main_layout.removeWidget(self)
        self.main_menu.main_menu_widget.show()
        self.deleteLater()
