import tkinter as tk

# List of questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "answers": ["Paris", "London", "Rome", "Madrid"],
        "correct": 0
    },
    {
        "question": "Who is the author of To Kill a Mockingbird?",
        "answers": ["Harper Lee", "Mark Twain", "George Orwell", "Ernest Hemingway"],
        "correct": 0
    },
    # Add more questions as needed
]

# Current question index
current_question = 0

# Score
score = 0

# Create the main window
window = tk.Tk()

# Function to handle button clicks
def on_button_click(choice):
    global current_question, score
    if choice == questions[current_question]["correct"]:
        score += 1
    if current_question < len(questions) - 1:
        current_question += 1
        update_question()
    else:
        # Show final score
        result_label.config(text=f"Your score is: {score}/{len(questions)}")
        result_label.pack()
        quiz_frame.pack_forget()

# Function to update the question and answer buttons
def update_question():
    question_label.config(text=questions[current_question]["question"])
    for i, answer in enumerate(questions[current_question]["answers"]):
        button_vars[i].set(answer)

# Create a frame for the quiz
quiz_frame = tk.Frame(window)

# Create a label for the question
question_label = tk.Label(quiz_frame, text=questions[current_question]["question"])
question_label.pack()

# Create a label and entry for user input
answer_var = tk.StringVar()
answer_entry = tk.Entry(quiz_frame, textvariable=answer_var)
answer_entry.pack()

# Create buttons for the answers
button_vars = [tk.StringVar() for _ in range(4)]
for i in range(4):
    button = tk.Radiobutton(quiz_frame, textvariable=button_vars[i], value=i, command=lambda i=i: on_button_click(i))
    button.pack()

# Create a label for the final score
result_label = tk.Label(window, text="")

# Pack the quiz frame and start the main loop
quiz_frame.pack()
window.mainloop()