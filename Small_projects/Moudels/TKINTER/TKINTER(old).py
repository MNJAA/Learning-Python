from tkinter import *
from PIL import Image, ImageTk
from random import shuffle,choice
from time import sleep
from ANSI import BrightGreen,un
from qs import Chemistry_practical,Anatomy_practical,Anatomy_questions,Anatomy_ph,Biology_questions,Biology_ph,Chemistry_questions,Chemistry_ph,NIT_questions,PPC_questions

root = Tk()
root.title("First Year MSQ Exam")
root.config(bg="#242424")
root.iconbitmap("Images\Icons\MSQ.ico")

f = "TimesNewRoman 16 bold"
f2 = "TimesNewRoman 11"
objects = [
    "Anatomy","Biology","Chemistry","PPC","NIT"
    ]
wrong_questions = []
current_question_index = 0

def load_image(file_path):
    return ImageTk.PhotoImage(Image.open(file_path))

img_list = [
    load_image(r"Images\MSQ_Practical\img0.png"),
    load_image(r"Images\MSQ_Practical\img1.png"),
    load_image(r"Images\MSQ_Practical\img2.png"),
    load_image(r"Images\MSQ_Practical\img3.png")
]

obj = ""
def object_pick():
    Label(root, text="⇃Choose your object⇂", font=f2, bg="#404040",fg="White").grid(row=0, column=0)
    object_row = 1
    for object in objects:
        obj_button = Button(root, text=f"{object}", bd=5, width=20,command=lambda obj=object:get(obj))
        obj_button.grid(row=object_row, column=0)
        object_row += 1
def get(selection):
    
    if selection == objects[0]:
        clear_widgets()
        Anatomy()
    elif selection == objects[2]:
        clear_widgets()
        chemistry()

def clear_widgets():
    global current_question_index
    current_question_index = 0
    for widget in root.winfo_children():
        widget.destroy()


def Anatomy():
    Label(root, text=f"{BrightGreen}{choice(Anatomy_ph)}{un}")
    
    if current_question_index < len(Anatomy_practical):
        q = Anatomy_questions[current_question_index]
        Label(root, text=f"Question - {q['question']}", font=f, fg="White", bg="#404040").grid(row=1, column=0, columnspan=3)

        all_options = [q['correct_answer']] + q['wrong_answers']
        shuffle(all_options)
        row = 3
        for a in all_options:
            button = Button(root, text=f"{a}", width=30, bd=5, command=lambda answer=a: check_answer(answer, obj))
            button.grid(row=row, column=1)
            row += 1


def chemistry():
    global current_question_index
    if current_question_index < len(Chemistry_practical):
        q = Chemistry_practical[current_question_index]
        row = 3
        img = img_list[current_question_index]
        Label(root, image=img).grid(row=0, column=0)
        Label(root, text=f"{q['question']}", font=f, fg="White", bg="#404040").grid(row=1, column=0)

        all_a = [q['correct_answer']] + q['wrong_answers']
        shuffle(all_a)

        for a in all_a:
            button = Button(root, text=f"{a}", width=30, bd=5, command=lambda answer=a: check_answer(answer, obj))
            button.grid(row=row, column=0)
            row += 1


def check_answer(answer, obj):
    global current_question_index
    overall_score = 0 
    q = Chemistry_practical[current_question_index]
    
    if obj == "Anatomy":
        if answer in Anatomy_questions[current_question_index]['correct_answer']:
            print("Correct")
            overall_score += 1
        else:  
            print("Incorrect")
            wrong_questions.append(q['question'])
            
        if current_question_index < len(Anatomy_practical) - 1:
            current_question_index += 1
            clear_widgets()
            Anatomy()
        elif current_question_index == len(Anatomy_practical) - 1:
            clear_widgets()
            Label(root, text=f"Your score is: {overall_score}/{len(Anatomy_practical)}").grid(row=1, column=0, columnspan=3)
        
    elif obj == "Chemistry":
        if answer in Chemistry_practical[current_question_index]['correct_answer']:
            print("Correct")
            overall_score += 1
        else:  
            print("Incorrect")
            
        if current_question_index < len(Chemistry_practical) - 1:
            current_question_index += 1
            clear_widgets()
            chemistry()
        elif current_question_index == len(Chemistry_practical) - 1:
            clear_widgets()
            Label(root, text=f"Your score is: {overall_score}/{len(Chemistry_practical)}").grid(row=1, column=0, columnspan=3)


                




object_pick()
root.mainloop()