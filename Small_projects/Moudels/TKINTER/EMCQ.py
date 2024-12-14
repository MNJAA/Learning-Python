import tkinter as tk
from tkinter import ttk
import random  # Import random module for shuffling
import time  # Import time module to handle timer
from qs import HEM  # Import questions from your qs.py file

class Quiz:
    def __init__(self, root, questions):
        self.root = root
        self.questions = questions  # Questions list
        random.shuffle(self.questions)  # Shuffle the questions
        self.current_question_index = 0
        self.selected_option = None  # Store selected option for each question
        self.score = 0
        self.total_questions = len(questions)
        self.incorrect_questions = []  # To track incorrect questions
        self.start_time = time.time()  # Record the start time for the timer
        self.elapsed_seconds = 0  # Track the elapsed time in seconds
        self.quiz_ended = False  # Flag to track if quiz has ended
        self.timer_running = True  # Start with the timer running

        # Set background color
        self.root.configure(bg="#204040")

        # UI Elements
        self.timer_label = tk.Label(root, text="Time: 00:00:00", font=("Arial", 14), bg="#204040", fg="white")
        self.timer_label.pack(pady=10)  # Timer above the question

        self.question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 14), bg="#204040", fg="white")
        self.question_label.pack(pady=20)

        self.options_frame = tk.Frame(root, bg="#204040")
        self.options_frame.pack(pady=20)

        self.check_buttons = []  # Store checkbox widgets
        self.check_vars = []  # List of IntVar for each checkbox (check if selected)
        self.answer_options = []  # To store the actual answers (used for checking correctness)
        for i in range(4):  # Assuming 4 choices per question (can be adjusted)
            var = tk.IntVar(value=0)
            cb = tk.Checkbutton(
                self.options_frame,
                text="",
                variable=var,
                font=("Arial", 12),
                wraplength=400,
                command=lambda i=i: self.on_option_select(i),  # Trigger when an option is selected
                bg="#204040",
                fg="white",
                activebackground="#204040",
                activeforeground="white",
                selectcolor="#5c7f7f"  # Color for selected checkbox (this is optional)
            )
            cb.pack(anchor="w")
            self.check_buttons.append(cb)
            self.check_vars.append(var)

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer, bg="#5c7f7f", fg="white", font=("Arial", 12))
        self.submit_button.pack(pady=20)

        # Progress Bar
        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)
        self.progress["maximum"] = self.total_questions  # Set progress bar max to total questions
        self.progress["value"] = self.current_question_index  # Initialize progress bar

        # Question number label under the progress bar
        self.question_number_label = tk.Label(root, text=f"Question {self.current_question_index + 1} of {self.total_questions}", font=("Arial", 12), bg="#204040", fg="white")
        self.question_number_label.pack(pady=5)

        self.show_question()

    def show_question(self):
        # Load the current question
        question_data = self.questions[self.current_question_index]
        self.question_label.config(text=question_data["question"])

        # Get all possible answers (correct + wrong)
        all_answers = [question_data["correct_answer"]] + question_data["wrong_answers"]
        random.shuffle(all_answers)  # Shuffle the answers

        # Store the actual answer choices for later comparison
        self.answer_options = all_answers

        # Set checkboxes for answers
        for i, answer in enumerate(all_answers):
            self.check_buttons[i].config(text=answer)
            self.check_vars[i].set(0)  # Uncheck all checkboxes

        # Update progress bar and question number label
        self.progress["value"] = self.current_question_index + 1
        self.question_number_label.config(text=f"Question {self.current_question_index + 1} of {self.total_questions}")

        # Start the timer update
        if not self.quiz_ended:  # Only update the timer if quiz hasn't ended
            self.update_timer()

    def update_timer(self):
        if self.timer_running:
            # Increment the elapsed time by 1 second
            self.elapsed_seconds = int(time.time() - self.start_time)

            # Calculate hours, minutes, and seconds
            hours = self.elapsed_seconds // 3600
            minutes = (self.elapsed_seconds % 3600) // 60
            seconds = self.elapsed_seconds % 60

            # Format the time as HH:MM:SS
            formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"

            # Update the timer label with the formatted time
            self.timer_label.config(text=f"Time Elapsed: {formatted_time}")

            # Call this method again after 1 second
            self.timer_label.after(1000, self.update_timer)

    def on_option_select(self, selected_index):
        # Allow only one selection at a time (uncheck others)
        for i, var in enumerate(self.check_vars):
            if i != selected_index:
                var.set(0)

    def submit_answer(self):
        # Get the selected answer (only one box allowed)
        selected_answer = None
        for i, var in enumerate(self.check_vars):
            if var.get() == 1:
                selected_answer = self.check_buttons[i].cget("text")
                break

        if selected_answer:
            correct_answer = self.questions[self.current_question_index]["correct_answer"]
            # Check if the selected answer is correct
            if selected_answer == correct_answer:
                self.score += 1
            else:
                # Track the wrong question and selected answer
                self.incorrect_questions.append({
                    "question": self.questions[self.current_question_index]["question"],
                    "correct_answer": correct_answer,
                    "selected_answer": selected_answer
                })

        # Move to the next question or end quiz
        self.current_question_index += 1
        if self.current_question_index < self.total_questions:
            self.show_question()
        else:
            self.end_quiz()

    def end_quiz(self):
        # Calculate the total time taken
        self.timer_running = False  # Stop the timer updates

        # Format the final time taken
        hours = self.elapsed_seconds // 3600
        minutes = (self.elapsed_seconds % 3600) // 60
        seconds = self.elapsed_seconds % 60

        formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"

        # Display the final score and time taken
        self.question_label.config(text=f"Quiz Over! Your score: {self.score}/{self.total_questions}")
        self.timer_label.config(text=f"Time taken: {formatted_time}")
        self.options_frame.destroy()
        self.submit_button.destroy()
        self.progress.destroy()
        self.question_number_label.destroy()

        # Create a scrollable frame to show incorrect answers
        scroll_frame = tk.Frame(self.root, bg="#204040")
        scroll_frame.pack(pady=20, fill="both", expand=True)

        canvas = tk.Canvas(scroll_frame, bg="#204040")
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        incorrect_frame = tk.Frame(canvas, bg="#204040")
        canvas.create_window((0, 0), window=incorrect_frame, anchor="nw")

        # Create better alignment for incorrect questions
        for idx, q in enumerate(self.incorrect_questions, 1):
            # Add question number and format the labels properly
            question_label = tk.Label(
                incorrect_frame, 
                text=f"Q{idx}: {q['question']}", 
                bg="#204040", 
                fg="white", 
                font=("Arial", 12, 'bold')
            )
            question_label.grid(row=idx*2-1, column=0, sticky="w", padx=10, pady=5)

            correct_answer_label = tk.Label(
                incorrect_frame, 
                text=f"   Correct Answer: {q['correct_answer']}", 
                bg="#204040", 
                fg="#3fff00", 
                font=("Arial", 12)
            )
            correct_answer_label.grid(row=idx*2, column=0, sticky="w", padx=10, pady=5)

            user_answer_label = tk.Label(
                incorrect_frame, 
                text=f"   Your Answer: {q['selected_answer']}", 
                bg="#204040", 
                fg="yellow", 
                font=("Arial", 12)
            )
            user_answer_label.grid(row=idx*2, column=1, sticky="w", padx=10, pady=5)

        # Update the scroll region to encompass all widgets in the frame
        incorrect_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    root.title("MCQ Quiz")
    root.geometry("500x600")  # Increase height to accommodate incorrect answers list
    
    exam_questions = HEM  # Questions from qs.py
    quiz = Quiz(root, exam_questions)
    
    root.mainloop()
