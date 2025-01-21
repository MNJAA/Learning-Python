import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import time
import winsound
from qs import HP_TBL_diving, Example_questions_form  # Import your questions from qs.py

class Quiz:
    def __init__(self, root, questions):
        self.root = root
        self.questions = questions
        random.shuffle(self.questions)
        self.current_question_index = 0
        self.score = 0
        self.answered_questions = 0
        self.total_questions = len(questions)
        self.incorrect_questions = []
        self.start_time = time.time()
        self.quiz_ended = False
        self.elapsed_seconds = 0
        self.timer_running = False
        self.answered_set = set()
        self.check_buttons = []
        self.check_vars = []
        self.answer_options = []
        self.skipped_questions = []

        # Set background color
        self.root.configure(bg="#204040")

        # Top frame
        self.top_frame = tk.Frame(root, bg="#204040")
        self.top_frame.pack(fill="x", pady=10)

        # Finish Early button
        self.finish_button = tk.Button(
            self.top_frame,
            text="Finish Early",
            command=self.finish_quiz_early,
            bg="#ff5733",
            fg="white",
            font=("Times new roman", 16)
        )
        self.finish_button.pack(side="left", padx=20)

        # Timer label
        self.timer_label = tk.Label(
            self.top_frame,
            text="Time: 00:00:00",
            font=("Times new roman", 14),
            bg="#204040",
            fg="white"
        )
        self.timer_label.pack(side="left", expand=True)

        # Question number label
        self.question_number_label = tk.Label(
            self.top_frame,
            text=f"Question {self.current_question_index + 1} of {self.total_questions}",
            font=("Times new roman", 16),
            bg="#204040",
            fg="white"
        )
        self.question_number_label.pack(side="right", padx=20)

        # Bottom frame
        self.bottom_frame = tk.Frame(self.root, bg="#204040")
        self.bottom_frame.pack(side="bottom", pady=20)

        # Question label
        self.question_label = tk.Label(
            root, text="", wraplength=400, font=("Times new roman", 16), bg="#204040", fg="white"
        )
        self.question_label.pack(pady=20)
        
        # Answer options frame
        self.button_frame = tk.Frame(self.root, bg="#204040")
        self.button_frame.pack(pady=10)

        # Navigation buttons
        self.button1_frame = tk.Frame(self.bottom_frame, bg="#204040")
        self.button1_frame.pack()

        self.back_button = tk.Button(self.button1_frame, text="Back", command=self.go_back, bg="#ffd700", fg="black", font=("Times new roman", 16))
        self.back_button.pack(side="left", padx=20)

        self.submit_button = tk.Button(self.button1_frame, text="Submit", command=self.submit_answer, bg="#5c7f7f", fg="white", font=("Times new roman", 16))
        self.submit_button.pack(side="left", padx=20)

        # Progress bar
        self.progress = ttk.Progressbar(self.bottom_frame, orient="horizontal", length=250, mode="determinate")
        self.progress.pack(pady=10)
        self.progress["maximum"] = self.total_questions 
        self.progress["value"] = self.current_question_index
        self.show_question()
    
    def show_question(self):
        for cb in self.check_buttons:
            cb.destroy()
        self.check_buttons.clear()
        self.check_vars.clear()

        question_data = self.questions[self.current_question_index]
        self.question_label.config(text=question_data["question"])

        all_answers = [question_data["correct_answer"]] + question_data["wrong_answers"]
        random.shuffle(all_answers)
        self.answer_options = all_answers

        for i, answer in enumerate(all_answers):
            var = tk.IntVar(value=0)
            cb = tk.Checkbutton(
                self.button_frame,
                text=answer,
                variable=var,
                font=("Times new roman", 16),
                wraplength=400,
                command=lambda i=i: self.on_option_select(i),
                bg="#204040",
                fg="white",
                activebackground="#204040",
                activeforeground="white",
                selectcolor="#5c7f7f"
            )
            cb.pack(anchor="w")
            self.check_buttons.append(cb)
            self.check_vars.append(var)

        for var in self.check_vars:
            var.set(0)

        self.progress["value"] = self.current_question_index + 1
        self.question_number_label.config(text=f"Question {self.current_question_index + 1} of {self.total_questions}")

        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

    def update_timer(self):
        if not self.quiz_ended:
            self.elapsed_seconds += 1
            hours = self.elapsed_seconds // 3600
            minutes = (self.elapsed_seconds % 3600) // 60
            seconds = self.elapsed_seconds % 60
            formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
            self.timer_label.config(text=f"Time Elapsed: {formatted_time}")
            self.timer_label.after(1000, self.update_timer)

    def on_option_select(self, selected_index):
        for i, var in enumerate(self.check_vars):
            if i != selected_index:
                var.set(0)

    def submit_answer(self):
        selected_answer = None
        for i, var in enumerate(self.check_vars):
            if var.get() == 1:
                selected_answer = self.check_buttons[i].cget("text")
                break

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
        if result == "correct":
            winsound.Beep(1000, 500)
        elif result == "incorrect":
            winsound.Beep(500, 500)

    def end_quiz(self):
        self.quiz_ended = True
        hours = self.elapsed_seconds // 3600
        minutes = (self.elapsed_seconds % 3600) // 60
        seconds = self.elapsed_seconds % 60
        formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"

        self.question_label.config(text=f"Quiz Over! Your score: {self.score}/{self.answered_questions}")
        self.timer_label.config(text=f"Time Elapsed: {formatted_time}")

        self.button_frame.destroy()
        self.submit_button.destroy()
        self.progress.destroy()
        self.question_number_label.destroy()
        self.finish_button.destroy()
        self.back_button.destroy()
        
        # Create a frame for results with scroll capability
        results_frame = tk.Frame(self.root, bg="#204040")
        results_frame.pack(pady=20, fill="both", expand=True)  # Use pack instead of grid

        canvas = tk.Canvas(results_frame, bg="#204040")  # Canvas for scrolling
        canvas.pack(side="left", fill="both", expand=True)  # Use pack instead of grid

        scrollbar = tk.Scrollbar(results_frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")  # Use pack instead of grid
        canvas.configure(yscrollcommand=scrollbar.set)

        results_container = tk.Frame(canvas, bg="#204040")  # Inner frame to hold the result labels
        canvas.create_window((0, 0), window=results_container, anchor="nw")

        # Update the canvas scroll region after packing all widgets
        results_container.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Display Incorrect Answers
        if self.incorrect_questions:
            incorrect_label = tk.Label(
                results_container,
                text="Incorrect Answers:",
                font=("Times new roman", 14, "bold"),
                bg="#204040",
                fg="red"
            )
            incorrect_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

            # Iterate through incorrect questions
            for idx, q in enumerate(self.incorrect_questions, 1):
                # Question label (first column, spanning two columns to center it)
                question_label = tk.Label(
                    results_container,
                    text=f"{idx}. {q['question']}",
                    font=("Times new roman", 16, "bold"),
                    bg="#204040",
                    fg="white",
                    wraplength=400,
                    justify="left"
                )
                question_label.grid(row=idx * 2 - 1, column=0, padx=10, pady=5, sticky="w", columnspan=2)

                # Your Answer and Correct Answer (next row, aligned)
                answer_label = tk.Label(
                    results_container,
                    text=f"Your Answer: {q['selected_answer']}",
                    font=("Times new roman", 16),
                    bg="#204040",
                    fg="yellow",
                    wraplength=400,
                    justify="left"
                )
                answer_label.grid(row=idx * 2, column=0, padx=10, pady=5, sticky="w")

                correct_answer_label = tk.Label(
                    results_container,
                    text=f"Correct Answer: {q['correct_answer']}",
                    font=("Times new roman", 16),
                    bg="#204040",
                    fg="#3fff00",
                    wraplength=400,
                    justify="left"
                )
                correct_answer_label.grid(row=idx * 2, column=1, padx=10, pady=5, sticky="w")

        # Display Skipped Questions
        if self.skipped_questions:
            skipped_label = tk.Label(
                results_container,
                text="Skipped Questions:",
                font=("Times new roman", 14, "bold"),
                bg="#204040",
                fg="orange",
                anchor="e"
            )
            skipped_label.grid(row=0, column=4, padx=(50,10), pady=10, sticky="ne")

            # Iterate through skipped questions
            for idx, question_data in enumerate(self.skipped_questions, 1):
                # Question label (first column, spanning two columns to center it)
                question_label = tk.Label(
                    results_container,
                    text=f"{idx}. {question_data['question']}",
                    font=("Times new roman", 16, "bold"),
                    bg="#204040",
                    fg="white",
                    wraplength=400,
                    anchor="e",
                    justify="left"
                )
                question_label.grid(row=idx * 2 - 1, column=4, padx=(50,10), pady=5, sticky="e", columnspan=2)

                # Correct Answer (next row)
                correct_answer_label = tk.Label(
                    results_container,
                    text=f"Correct Answer: {question_data['correct_answer']}",
                    font=("Times new roman", 16),
                    bg="#204040",
                    fg="#3fff00",
                    wraplength=400,
                    anchor="e",
                    justify="left"
                )
                correct_answer_label.grid(row=idx * 2, column=4, padx=(50,10), pady=5, sticky="e")

        # Results display code remains the same as original...

    def finish_quiz_early(self):
        if messagebox.askyesno("Finish Quiz", "Are you sure you want to finish the quiz early?"):
            self.end_quiz()

    def go_back(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.show_question()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("MCQ Quiz")
    root.config(bg="#204040")
    root.geometry("1100x600")
    root.resizable(True, True)
    exam_questions = HP_TBL_diving
    quiz = Quiz(root, exam_questions)
    root.mainloop()