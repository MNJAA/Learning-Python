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
# 2. Main Menu Class
# ----------------------------
class QuizLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Menu")
        self.root.geometry("400x300")
        self.root.configure(bg="#2E3440")
        
        # Get path to TKINTER folder
        self.quiz_path = self.get_quiz_path()
        
        # Create GUI
        self.create_widgets()
        
    def get_quiz_path(self):
        """Get path to TKINTER folder from Learning_Python root"""
        # Path to Learning_Python (where this script is located)
        learning_python_root = os.path.dirname(os.path.abspath(__file__))
        
        # Path to TKINTER folder
        return os.path.join(
            learning_python_root,
            "Small_projects",
            "Moudels",
            "TKINTER"
        )
        
    def create_widgets(self):
        # Header
        header = tk.Label(
            self.root, 
            text="Select a Quiz", 
            font=("Helvetica", 18, "bold"), 
            bg="#2E3440", 
            fg="#88C0D0"
        )
        header.pack(pady=20)
        
        # Quiz buttons
        quizzes = [
            ("Embryology", "EM.py"),
            ("Medical Genetics", "MG.py"),
            ("TBL Quiz", "TBL.py")
        ]
        
        for text, filename in quizzes:
            btn = tk.Button(
                self.root,
                text=text,
                command=lambda f=filename: self.launch_quiz(f),
                bg="#4C566A",
                fg="#ECEFF4",
                activebackground="#5E81AC",
                font=("Arial", 12),
                width=25,
                relief="flat"
            )
            btn.pack(pady=7)
            
        # Exit button
        exit_btn = tk.Button(
            self.root,
            text="Exit",
            command=self.root.destroy,
            bg="#BF616A",
            fg="#ECEFF4",
            font=("Arial", 12),
            width=15,
            relief="flat"
        )
        exit_btn.pack(pady=20)
        
    def launch_quiz(self, filename):
        full_path = os.path.join(self.quiz_path, filename)
        
        if not os.path.exists(full_path):
            messagebox.showerror("Error", 
                f"Quiz file not found:\n{filename}\n"
                f"Expected at: {self.quiz_path}")
            return
            
        try:
            # Launch quiz in its own process
            subprocess.Popen([sys.executable, full_path])
        except Exception as e:
            messagebox.showerror("Error", 
                f"Failed to launch {filename}:\n{str(e)}")

# ----------------------------
# 3. Run the Application
# ----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizLauncher(root)
    root.mainloop()