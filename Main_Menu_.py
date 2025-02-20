import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
import sys

# ----------------------------
# 1. Check for Tkinter
# ----------------------------
try:
    from tkinter import *
except ImportError:
    print("Tkinter is required but not installed!")
    if sys.platform.startswith("linux"):
        print("Install it with: sudo apt-get install python3-tk")
    sys.exit(1)

# ----------------------------
# 2. Main Menu Class with Upgraded UI
# ----------------------------
class QuizLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Menu")
        self.root.geometry("500x400")
        self.root.configure(bg="#3B4252")  # Modern dark background

        self.quiz_path = self.get_quiz_path()
        self.setup_styles()  # Apply modern ttk styles
        self.create_widgets()

    def get_quiz_path(self):
        """Get path to TKINTER folder from Learning_Python root"""
        learning_python_root = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(
            learning_python_root,
            "Small_projects",
            "Moudels",
            "TKINTER"
        )

    def setup_styles(self):
        # Setup ttk styles for a modern look
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TButton", font=("Segoe UI", 12), padding=6)
        style.configure("TLabel", font=("Segoe UI", 12))

    def add_hover(self, widget, normal_bg, hover_bg):
        # Adds a simple hover effect to buttons
        def on_enter(e):
            widget['bg'] = hover_bg
        def on_leave(e):
            widget['bg'] = normal_bg
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)

    def create_widgets(self):
        # Header Frame
        header_frame = tk.Frame(self.root, bg="#3B4252")
        header_frame.pack(pady=30)
        header = tk.Label(
            header_frame, 
            text="Select a Quiz", 
            font=("Segoe UI", 20, "bold"), 
            bg="#3B4252", 
            fg="#88C0D0"
        )
        header.pack()

        # Buttons Frame
        buttons_frame = tk.Frame(self.root, bg="#3B4252")
        buttons_frame.pack(pady=20)

        quizzes = [
            ("Embryology", "EM.py"),
            ("Medical Genetics", "MG.py"),
            ("TBL Quiz", "TBL.py"),
            ("HA4 Quiz 1", "HA.py"),
            ("GPT prac Quiz", "GPT.py"),
            ("pharma", "pharma.py") 
        ]

        for text, filename in quizzes:
            btn = tk.Button(
                buttons_frame,
                text=text,
                command=lambda f=filename: self.launch_quiz(f),
                bg="#4C566A",
                fg="#ECEFF4",
                activebackground="#5E81AC",
                font=("Segoe UI", 14),
                width=25,
                relief="flat"
            )
            btn.pack(pady=8)
            self.add_hover(btn, "#4C566A", "#5E81AC")

        # Exit Button
        exit_frame = tk.Frame(self.root, bg="#3B4252")
        exit_frame.pack(pady=20)
        exit_btn = tk.Button(
            exit_frame,
            text="Exit",
            command=self.root.destroy,
            bg="#BF616A",
            fg="#ECEFF4",
            activebackground="#D08770",
            font=("Segoe UI", 14),
            width=15,
            relief="flat"
        )
        exit_btn.pack()
        self.add_hover(exit_btn, "#BF616A", "#D08770")

    def launch_quiz(self, filename):
        full_path = os.path.join(self.quiz_path, filename)
        if not os.path.exists(full_path):
            messagebox.showerror(
                "Error", 
                f"Quiz file not found:\n{filename}\nExpected at: {self.quiz_path}"
            )
            return
        try:
            subprocess.Popen([sys.executable, full_path])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch {filename}:\n{str(e)}")

# ----------------------------
# 3. Run the Application
# ----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizLauncher(root)
    root.mainloop()
