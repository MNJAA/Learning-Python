from tkinter import *
from PIL import Image, ImageTk
from random import shuffle
from qs import Chemistry_practical,Anatomy_practical,Anatomy_questions,Chemistry_questions,NIT_questions,PPC_questions,PPC_terms

root = Tk()
root.title("First Year MCQ Exam")
root.config(bg="#242424")
root.iconbitmap("Images\Icons\MSQ.ico")

f = "TimesNewRoman 16 bold"
f2 = "TimesNewRoman 11 bold"
f3 = "TimesNewRoman 8"
f4 = "TimesNewRoman 1"


objects = ["Anatomy","Biology","Chemistry","NIT","PPC"]
wrong_questions = []
current_question_index = 0
overall_score = 0

def load_image(file_path):
    return ImageTk.PhotoImage(Image.open(file_path))

img_list = [
    load_image(r"Images\MSQ_Practical\img0.png"),
    load_image(r"Images\MSQ_Practical\img1.png"),
    load_image(r"Images\MSQ_Practical\img2.png"),
    load_image(r"Images\MSQ_Practical\img3.png")
]


def The_satrt():
    Label(root,text='Which Mid?',font=f, bg="#404040",fg="White").grid(row=0,column=0)
    button = Button(root,text='PreMid 1',font=f, bd=5, width=20,command=lambda: starting("1"))
    button.grid(row=1,column=0)
    button1 = Button(root,text='PreMid 2',font=f, bd=5, width=20,command=lambda: starting("2"))
    button1.grid(row=2,column=0)

    
def starting(a):
    clear_widgets()
    if a == '1':
        Label(root,text='Easy or Hard?',font=f, bg="#404040",fg="White").grid(row=0,column=0)
        button = Button(root,text='Practical',font=f, bd=5, width=20)
        button.grid(row=1,column=0)
        button1 = Button(root,text='Impractical',font=f,command=md1_imprac, bd=5, width=20)
        button1.grid(row=2,column=0)
    if a == '2':
        Label(root,text='Easy or Hard?',font=f, bg="#404040",fg="White").grid(row=0,column=0)
        button = Button(root,text='Practical',font=f, bd=5, width=20)
        button.grid(row=1,column=0)
        button1 = Button(root,text='Impractical',font=f, bd=5, width=20,command=md1_imprac)
        button1.grid(row=2,column=0)
        
    
#premid 1 impratcial

def md1_imprac():
    clear_widgets()
    Label(root, text="⇃Choose your subject⇂", font=f, bg="#404040",fg="White").grid(row=0, column=0)
    object_row = 1
    for object in objects:
        obj_button = Button(root, text=object,font=f, bd=5, width=20,command=lambda obj=object:get(obj))
        obj_button.grid(row=object_row, column=0)
        object_row += 1
    
def get(selection):
    global obj
    if selection == objects[0]:
        clear_widgets()
        obj = objects[0]
        anatomy()
    elif selection == objects[1]:
        clear_widgets()
        obj = objects[1]
        biology()
    elif selection == objects[2]:
        clear_widgets()
        obj = objects[2]
        chemistry()
    elif selection == objects[3]:
        clear_widgets()
        obj = objects[3]
        nit()
    elif selection == objects[4]:
        clear_widgets()
        obj = objects[4]
        ppc()

def show_result(object):
    clear_widgets()
    root.config(bg="#f0f0f0")
    Label(root, text=f"Your score is: {overall_score}/{len(object)}").grid(row=0, column=0,columnspan=3)
    Label(root, text="Your wrong questions are: ").grid(row=1, column=0,columnspan=3)
    r,c = 2,0
    for index,wrq in enumerate(wrong_questions,start=1):
        Label(root, text=f'{index}- {wrq}',font=f2).grid(row=r, column=c,sticky=W+N)
        r += 1
        if r == 31:
            r = 2
            c += 1


def clear_widgets():
    for widget in root.winfo_children():
        widget.destroy()


def anatomy():
    shuffle(Anatomy_questions)
    aq = Anatomy_questions[current_question_index]
    row = 3
    Label(root, text=f"Question - {aq['question']}", font=f, fg="White", bg="#404040").grid(row=1, column=0)

    all_a = [aq['correct_answer']] + aq['wrong_answers']
    shuffle(all_a)
    
    for answer in all_a:
        button = Button(root, text=answer,font=f ,width = 100, bd=5, command=lambda a=answer: check_anat(a))
        button.grid(row=row, column=0)
        row += 1

def check_anat(a):
    global current_question_index, overall_score
    cq = Anatomy_questions[current_question_index]
    
    if a in cq['correct_answer']:
        overall_score += 1
        print("Correct")
    
    else:  
        print("Incorrect")
        wrong_questions.append(cq['correct_answer'])

    if current_question_index < len(Anatomy_questions) - 1:
        clear_widgets()
        current_question_index += 1
        anatomy()
    else:
        show_result(Anatomy_questions)


def biology():
    shuffle(Biology_questions)
    bq = Biology_questions[current_question_index]
    row = 3
    Label(root, text=f"Question - {bq['question']}", font=f, fg="White", bg="#404040").grid(row=1, column=0)

    all_a = [bq['correct_answer']] + bq['wrong_answers']
    shuffle(all_a)
    
    for answer in all_a:
        button = Button(root, text=answer,font=f ,width=100, bd=5, command=lambda a=answer: check_bio(a))
        button.grid(row=row, column=0)
        row += 1

def check_bio(a):
    global current_question_index, overall_score
    bq = Biology_questions[current_question_index]
    
    if a in bq['correct_answer']:
        overall_score += 1
        print("Correct")
    
    else:  
        print("Incorrect")
        wrong_questions.append(bq['correct_answer'])

    if current_question_index < len(Biology_questions) - 1:
        clear_widgets()
        current_question_index += 1
        biology()
    else:
        show_result(Biology_questions)


def chemistry():
    shuffle(Chemistry_questions)
    cq = Chemistry_questions[current_question_index]
    row = 3
    Label(root, text=f"Question - {cq['question']}", font=f, fg="White", bg="#404040").grid(row=1, column=0)

    all_a = [cq['correct_answer']] + cq['wrong_answers']
    shuffle(all_a)
    
    for answer in all_a:
        button = Button(root, text=answer,font=f ,width=100, bd=5, command=lambda a=answer: check_chem(a))
        button.grid(row=row, column=0)
        row += 1

def check_chem(a):
    global current_question_index, overall_score
    cq = Chemistry_questions[current_question_index]
    
    if a in cq['correct_answer']:
        overall_score += 1
        print("Correct")
    
    else:  
        print("Incorrect")
        wrong_questions.append(cq['correct_answer'])

    if current_question_index < len(Chemistry_questions) - 1:
        clear_widgets()
        current_question_index += 1
        chemistry()
    else:
        show_result(Chemistry_questions)


def nit():
    shuffle(NIT_questions)
    nq = NIT_questions[current_question_index]
    row = 3
    Label(root, text=f"Question - {nq['question']}", font=f, fg="White", bg="#404040").grid(row=1, column=0)

    all_a = [nq['correct_answer']] + nq['wrong_answers']
    shuffle(all_a)
    
    for answer in all_a:
        button = Button(root, text=answer,font=f ,width=100, bd=5, command=lambda a=answer: check_nit(a))
        button.grid(row=row, column=0)
        row += 1

def check_nit(a):
    global current_question_index, overall_score
    nq = NIT_questions[current_question_index]
    
    if a in nq['correct_answer']:
        overall_score += 1
        print("Correct")
    
    else:  
        print("Incorrect")
        wrong_questions.append(nq['correct_answer'])

    if current_question_index < len(NIT_questions) - 1:
        clear_widgets()
        current_question_index += 1
        nit()
    else:
        show_result(NIT_questions)


def ppc():
    shuffle(PPC_questions)
    pq = PPC_questions[current_question_index]
    row = 3
    Label(root, text=f"Question - {pq['question']}", font=f, fg="White", bg="#404040").grid(row=1, column=0)

    all_a = [pq['correct_answer']] + pq['wrong_answers']
    shuffle(all_a)
    
    for answer in all_a:
        button = Button(root, text=answer,font=f ,width = 100, bd=5, command=lambda a=answer: check_ppc(a))
        button.grid(row=row, column=0)
        row += 1

def check_ppc(a):
    global current_question_index, overall_score
    pq = PPC_questions[current_question_index]
    
    if a in pq['correct_answer']:
        overall_score += 1
        print("Correct")
    
    else:  
        print("Incorrect")
        wrong_questions.append(pq['correct_answer'])

    if current_question_index < len(PPC_questions) - 1:
        clear_widgets()
        current_question_index += 1
        ppc()
    else:
        show_result(PPC_questions)


#premid 1 practical

def chemistry_p():
    cq = Chemistry_practical[current_question_index]
    row = 3
    img = img_list[current_question_index]
    Label(root, image=img).grid(row=0, column=0)
    Label(root, text=cq['question'], font=f, fg="White", bg="#404040").grid(row=1, column=0)

    all_a = [cq['correct_answer']] + cq['wrong_answers']
    shuffle(all_a)

    for answers in all_a:
        button = Button(root, text=answers, width=30, bd=5, command=lambda a=answers: check_chem(a))
        button.grid(row=row, column=0)
        row += 1

def check_pchem(a):
    global current_question_index, overall_score
    cq = Chemistry_practical[current_question_index]
    
    if a in cq['correct_answer']:
        overall_score += 1
        print("Correct")
    
    else:  
        print("Incorrect")
        wrong_questions.append(cq['correct_answer'])

    if current_question_index < len(Chemistry_practical) - 1:
        clear_widgets()
        current_question_index += 1
        chemistry_p()
    else:
        show_result(Chemistry_practical)



#premid 2 impractical

def ppct():
    clear_widgets()
    shuffle(PPC_terms)
    pt = PPC_terms[current_question_index]
    row = 3
    Label(root, text=f"Question - {pt['question']}", font=f, fg="White", bg="#404040").grid(row=1, column=0)

    all_a = [pt['correct_answer']] + pt['wrong_answers']
    shuffle(all_a)
    
    for answer in all_a:
        button = Button(root, text=answer,font=f ,width=100, bd=5, command=lambda a=answer: check_ppct(a))
        button.grid(row=row, column=0)
        row += 1

def check_ppct(a):
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
        ppct()
    else:
        show_result(PPC_terms)



The_satrt()
root.mainloop()