from tkinter import *
from PIL import Image, ImageTk
from random import shuffle,choice
from time import sleep
from ANSI import BrightGreen,un
from qs import Chemistry_practical,Anatomy_practical,Anatomy_questions,Biology_questions,Chemistry_questions,NIT_questions,PPC_questions

#set the base
root = Tk()
root.title("First Year MSQ Exam")
root.config(bg="#242424")
root.iconbitmap("Images\Icons\MSQ.ico")

f = "TimesNewRoman 16 bold"
f2 = "TimesNewRoman 11"
f3 = "TimesNewRoman 8"
f4 = "TimesNewRoman 1"

objects_list = " "

#displays two options prac and imprac 
def mid1():
    Button_1.destroy()
    Button_2.destroy()
    Button_3 =Button(root,text="Practical",bd=5,padx=25,command=lambda: objects("prac"))
    Button_3.grid(row=1,column=1,sticky=W+E)
    Button_4 =Button(root,text="Impractical",bd=5,padx=25,command=lambda: objects("imprac"))
    Button_4.grid(row=2,column=1,sticky=W+E)
    
#diplays the objects for each option above
def objects(selection):
    global Button_5 
    if selection == "prac":
        objects_list = ["Anatomy","Chemsitry","Biology"]
        r = 1
        for ob in objects_list:
            Button_5 = Button(root, text=ob,bd=5,padx=25,command=lambda ob=ob: practical_roll(ob))
            Button_5.grid(row=r,column=1,sticky=W+E)
            r += 1
            
    if selection == "imprac":
        objects_list = ["Anatomy","Chemsitry","Biology","LLM","PPC","NIT"]
        r = 1
        for ob in objects_list:
            Button_5 = Button(root, text=ob,bd=5,padx=25,command=lambda ob=ob: impractical_roll(ob))
            Button_5.grid(row=r,column=1,sticky=W+E)
            r += 1

def impractical_roll(ob):
    Button_5.destroy()
    objects_list = ["Anatomy","Chemsitry","Biology"]
    if ob == objects_list[0]:
        shuffle(Anatomy_questions)
        for q in Anatomy_questions:
            
            Label_2 = Label(root, text=q['question'])
            Label_2.grid(row=0, column=0,columnspan=3)
            all_answers = q['wrong_answers'] + [q['correct_answer']]
            shuffle(all_answers)
            r = 1
            for a in all_answers:
                Button_6 = Button(root, text=a,bd=5,padx=40)
                Button_6.grid(row=r,column=1,sticky=W+E)
                r += 1

def practical_roll(ob):
    pass


#set the text and buttons
Label_1 = Label(root, text="What you need?",fg = "#ffffff",bg = "#242424" )
Label_1.grid(row =0, column=0,columnspan=2,sticky=W+E)

Button_1 = Button(root, text="Mid 1",bd=5,padx=40,command=mid1)
Button_1.grid(row=1,column=0)

Button_2 = Button(root, text="Mid 2",bd=5,padx=40)
Button_2.grid(row=2,column=0)


root.mainloop()