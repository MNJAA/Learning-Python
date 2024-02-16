from tkinter import *
from random import shuffle
from qs import PPC_terms
root = Tk()
root.title('TERMNOLOGY MCQ')
root.config(bg="#242424")

f = "TimesNewRoman 16 bold"
f2 = "TimesNewRoman 11"
f3 = "TimesNewRoman 8"
f4 = "TimesNewRoman 1"
wrong_questions = [ ]
current_question_index = 0
overall_score = 0


def start():
    l1 = Label(root,text="To start the PPC termnolgy test CLICK the satrt button")
    l1.grid(row=0)
    b1 = Button(root,text="start",command=Ask)
    b1.grid(row=1)
    


def show_result(object):
    clear_widgets()
    root.config(bg="#f0f0f0")
    Label(root, text=f"Your score is: {overall_score}/{len(object)}").grid(row=0, column=0,columnspan=3)
    Label(root, text="Your wrong questions are: ").grid(row=1, column=0,columnspan=3)
    r,c = 2,0
    for index,wrq in enumerate(wrong_questions,start=1):
        Label(root, text=f'{index}- {wrq}',font=f2).grid(row=r, column=c,sticky=W+N)
        r += 1
        if r == 30:
            r = 2
            c += 1


def Ask():
    clear_widgets()
    shuffle(PPC_terms)
    pt = PPC_terms[current_question_index]
    row = 3
    Label(root, text=f"Question - {pt['question']}", font=f, fg="White", bg="#404040").grid(row=1, column=0)

    all_a = [pt['correct_answer']] + pt['wrong_answers']
    shuffle(all_a)
    
    for answer in all_a:
        button = Button(root, text=answer,font=f ,width=100, bd=5, command=lambda a=answer: Check(a))
        button.grid(row=row, column=0)
        row += 1


def Check(a):
    global current_question_index, overall_score
    pt = PPC_terms[current_question_index]
    
    if a in pt['correct_answer']:
        overall_score += 1
        print("Correct")
    
    else:  
        print("Incorrect")
        wrong_questions.append(pt['correct_answer'])

    if current_question_index < len(PPC_terms) - 1:
        clear_widgets()
        current_question_index += 1
        Ask()
    else:
        show_result(PPC_terms)


def clear_widgets():
    for widget in root.winfo_children():
        widget.destroy()

start()

root.mainloop()