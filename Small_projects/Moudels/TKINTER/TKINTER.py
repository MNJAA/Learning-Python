from tkinter import *
from PIL import Image, ImageTk
from random import shuffle
from qs import Chemistry_practical,Anatomy_questions,Anatomy_ph,Biology_questions,Biology_ph,Chemistry_questions,Chemistry_ph,NIT_questions,PPC_questions

root = Tk()
root.title("First Year MSQ Exam")
root.config(bg="#242424")
root.iconbitmap(r"Images\Icons\MSQ.ico")

f = "TimesNewRoman 16 bold"
f2 = "TimesNewRoman 11"


current_question_index = 0

def load_image(file_path):
    return ImageTk.PhotoImage(Image.open(file_path))

img_list = [
    
    load_image("Images\MSQ_Practical\img0.png"),
    load_image("Images\MSQ_Practical\img1.png"),
    load_image("Images\MSQ_Practical\img2.png"),
    load_image("Images\MSQ_Practical\img3.png"),
    
]


def display_question():
    global current_question_index
    q = Chemistry_practical[current_question_index]
    row = 3
    if current_question_index < len(Chemistry_practical):

        img = img_list[current_question_index]
            
        Label(root, image=img).grid(row=0, column=0)
        Label(root, text=f"{q['question']}",font=f,fg="White",bg="#404040").grid(row=1, column=0)
        

        all_a = [q['correct_answer']] + q['wrong_answers']
        shuffle(all_a)
        Correct = q['correct_answer']

        for i, a in enumerate(all_a, start=1):
            button = Button(root, text=f"{i}- {a}", width=30, bd=5, command=lambda ans=a: check_answer(ans))
            button.grid(row=row, column=0)
            row += 1
        

def check_answer(select):
    global current_question_index
    if select in Chemistry_practical[current_question_index]['correct_answer']:
        print("Correct")
    else:
        print("Incorrect")

    current_question_index += 1
    if current_question_index < len(Chemistry_practical):
        clear_widgets()
        display_question()


def clear_widgets():
    for widget in root.winfo_children():
        widget.destroy()


display_question()
root.mainloop()
