from tkinter import *
from PIL import Image, ImageTk
from random import shuffle
from qs import Anatomy_practical,Anatomy2_questions,Anatomy_questions,Biology_questions,Chemistry_practical,Chemistry_questions,NIT_questions,PPC_questions,PPC_terms

root = Tk()
root.title("First Year MCQ Exam")
root.config(bg="#242424")
root.iconbitmap("Images\Icons\MSQ.ico")

f = "TimesNewRoman 13 bold"
f2 = "TimesNewRoman 10 bold"
f3 = "TimesNewRoman 8 bold"
f4 = "TimesNewRoman 1"



wrong_questions = []
current_question_index = 0
overall_score = 0




# global defs
def clear_widgets():
            for widget in root.winfo_children():
                widget.destroy()
                
def show_result(object):
        clear_widgets()
        root.config(bg="#f0f0f0")
        Label(root, text=f"Your score is: {overall_score}/{len(object)}").grid(row=0, column=0,columnspan=3)
        Label(root, text="Your wrong questions are: ").grid(row=1, column=0,columnspan=3)
        r,c = 2,0
        for index,wrq in enumerate(wrong_questions,start=1):
            Label(root, text=f'{index}- {wrq}',font=f2,wraplength=450).grid(row=r, column=c,sticky=W+N)
            r += 1
            if r == 20:
                r = 2
                c += 1

def The_satrt():
    Label(root,text='Which Mid?',font=f, bg="#404040",fg="White").grid(row=0,column=0)
    button = Button(root,text='PreMid 1',font=f, bd=5, width=20,command=lambda: starting("PreMid 1"))
    button.grid(row=1,column=0)
    button1 = Button(root,text='PreMid 2',font=f, bd=5, width=20,command=lambda: starting("PreMid 2"))
    button1.grid(row=2,column=0)
   
def starting(a):
    clear_widgets()
    if a == 'PreMid 1':
        Label(root,text='Easy or Hard?',font=f, bg="#404040",fg="White").grid(row=0,column=0)
        button = Button(root,text='Practical',font=f, bd=5, width=20,command=mid1("Prac").md1_theo,)
        button.grid(row=1,column=0)
        button1 = Button(root,text='Theoretical',font=f, bd=5, width=20,command=mid1("Theo").md1_theo)
        button1.grid(row=2,column=0)
    if a == 'PreMid 2':
        Label(root,text='Easy or Hard?',font=f, bg="#404040",fg="White").grid(row=0,column=0)
        button = Button(root,text='Practical',font=f, bd=5, width=20)
        button.grid(row=1,column=0)
        button1 = Button(root,text='Theoretical',font=f, bd=5, width=20,command=mid2().md2_theo)
        button1.grid(row=2,column=0)

def load_image(file_path):
    return ImageTk.PhotoImage(Image.open(file_path))

anatimgs= [
    
    load_image(r"Images\MMCQ_Practical\Anatomy\img0.png"),
    load_image(r"Images\MMCQ_Practical\Anatomy\img1.png"),
    load_image(r"Images\MMCQ_Practical\Anatomy\img2.png"),
    load_image(r"Images\MMCQ_Practical\Anatomy\img2.png"),
    load_image(r"Images\MMCQ_Practical\Anatomy\img3.png"),
    load_image(r"Images\MMCQ_Practical\Anatomy\img4.png"),
    load_image(r"Images\MMCQ_Practical\Anatomy\img4.png"),
    load_image(r"Images\MMCQ_Practical\Anatomy\img5.png"),
    load_image(r"Images\MMCQ_Practical\Anatomy\img5.png"),
    load_image(r"Images\MMCQ_Practical\Anatomy\img6.png"),
    load_image(r"Images\MMCQ_Practical\Anatomy\img6.png")
]

chemimgs = [
    load_image(r"Images\MMCQ_Practical\Chemistry\img0.png"),
    load_image(r"Images\MMCQ_Practical\Chemistry\img1.png"),
    load_image(r"Images\MMCQ_Practical\Chemistry\img2.png"),
    load_image(r"Images\MMCQ_Practical\Chemistry\img3.png")
]

class mid1:
# premid 1 
# Theoretical
    objects = ["Anatomy","Biology","Chemistry","NIT","PPC"]
    Pobjects = ["Anatomy","Chemistry"]
 
    def __init__(self,state):
        self.state = state
    

    def md1_theo(self):
        clear_widgets()
        Label(root, text="⇃Choose your subject⇂", font=f, bg="#404040",fg="White").grid(row=0, column=0)
        object_row = 1
        if self.state == "Theo":
            for object in self.objects:
                obj_button = Button(root, text=object,font=f, bd=5, width=20,command=lambda selection=object:self.get(selection))
                obj_button.grid(row=object_row, column=0)
                object_row += 1
        else:
            for object in self.Pobjects:
                obj_button = Button(root, text=object,font=f, bd=5, width=20,command=lambda selection=object:self.Pget(selection))
                obj_button.grid(row=object_row, column=0)
                object_row += 1
    
    def get(self,selection):
        if selection == self.objects[0]:
            clear_widgets()
            self.anatomy()
        elif selection == self.objects[1]:
            clear_widgets()
            self.biology()
        elif selection == self.objects[2]:
            clear_widgets()
            self.chemistry()
        elif selection == self.objects[3]:
            clear_widgets()
            self.nit()
        elif selection == self.objects[4]:
            clear_widgets()
            self.ppc()

    def Pget(self,selection):
        if selection == self.Pobjects[0]:
            clear_widgets()
            self.Panatomy()
        elif selection == self.Pobjects[1]:
            clear_widgets()
            self.Pchemistry()
        

    def anatomy(self):
        shuffle(Anatomy_questions)
        aq = Anatomy_questions[current_question_index]
        row = 3
        Label(root, text=f"Question - {aq['question']}", font=f, fg="White", bg="#404040",wraplength=1000).grid(row=1, column=0)

        all_a = [aq['correct_answer']] + aq['wrong_answers']
        shuffle(all_a)
        
        for answer in all_a:
            button = Button(root, text=answer,font=f ,width = 100, bd=5,wraplength=1000, command=lambda a=answer: self.check_anat(a))
            button.grid(row=row, column=0)
            row += 1

    def check_anat(self,a):
        global current_question_index, overall_score
        cq = Anatomy_questions[current_question_index]
        
        if a in cq['correct_answer']:
            overall_score += 1
            print("Correct")
        
        else:  
            print("Incorrect")
            wrong_questions.append(cq['question'])

        if current_question_index < len(Anatomy_questions) - 1:
            clear_widgets()
            current_question_index += 1
            self.anatomy()
        else:
            show_result(Anatomy_questions)


    def biology(self):
        shuffle(Biology_questions)
        bq = Biology_questions[current_question_index]
        row = 3
        Label(root, text=f"Question - {bq['question']}", font=f, fg="White",wraplength=1000, bg="#404040").grid(row=1, column=0)

        all_a = [bq['correct_answer']] + bq['wrong_answers']
        shuffle(all_a)
        
        for answer in all_a:
            button = Button(root, text=answer,font=f ,width=100,wraplength=1000, bd=5, command=lambda a=answer: self.check_bio(a))
            button.grid(row=row, column=0)
            row += 1

    def check_bio(self,a):
        global current_question_index, overall_score
        bq = Biology_questions[current_question_index]
        
        if a in bq['correct_answer']:
            overall_score += 1
            print("Correct")
        
        else:  
            print("Incorrect")
            wrong_questions.append(bq['question'])

        if current_question_index < len(Biology_questions) - 1:
            clear_widgets()
            current_question_index += 1
            self.biology()
        else:
            show_result(Biology_questions)


    def chemistry(self):
        shuffle(Chemistry_questions)
        cq = Chemistry_questions[current_question_index]
        row = 3
        Label(root, text=f"Question - {cq['question']}",wraplength=1000, font=f, fg="White", bg="#404040").grid(row=1, column=0)

        all_a = [cq['correct_answer']] + cq['wrong_answers']
        shuffle(all_a)
        
        for answer in all_a:
            button = Button(root, text=answer,wraplength=1000,font=f ,width=100, bd=5, command=lambda a=answer: self.check_chem(a))
            button.grid(row=row, column=0)
            row += 1

    def check_chem(self,a):
        global current_question_index, overall_score
        cq = Chemistry_questions[current_question_index]
        
        if a in cq['correct_answer']:
            overall_score += 1
            print("Correct")
        
        else:  
            print("Incorrect")
            wrong_questions.append(cq['question'])

        if current_question_index < len(Chemistry_questions) - 1:
            clear_widgets()
            current_question_index += 1
            self.chemistry()
        else:
            show_result(Chemistry_questions)


    def nit(self):
        shuffle(NIT_questions)
        nq = NIT_questions[current_question_index]
        row = 3
        Label(root, text=f"Question - {nq['question']}",wraplength=1000, font=f, fg="White", bg="#404040").grid(row=1, column=0)

        all_a = [nq['correct_answer']] + nq['wrong_answers']
        shuffle(all_a)
        
        for answer in all_a:
            button = Button(root, text=answer,font=f ,width=100, bd=5, command=lambda a=answer: self.check_nit(a))
            button.grid(row=row, column=0)
            row += 1

    def check_nit(self,a):
        global current_question_index, overall_score
        nq = NIT_questions[current_question_index]
        
        if a in nq['correct_answer']:
            overall_score += 1
            print("Correct")
        
        else:  
            print("Incorrect")
            wrong_questions.append(nq['question'])

        if current_question_index < len(NIT_questions) - 1:
            clear_widgets()
            current_question_index += 1
            self.nit()
        else:
            show_result(NIT_questions)


    def ppc(self):
        shuffle(PPC_questions)
        pq = PPC_questions[current_question_index]
        row = 3
        Label(root, text=f"Question - {pq['question']}",wraplength=1000, font=f, fg="White", bg="#404040").grid(row=1, column=0)

        all_a = [pq['correct_answer']] + pq['wrong_answers']
        shuffle(all_a)
        
        for answer in all_a:
            button = Button(root, text=answer,font=f ,width = 100, bd=5, command=lambda a=answer: self.check_ppc(a))
            button.grid(row=row, column=0)
            row += 1

    def check_ppc(self,a):
        global current_question_index, overall_score
        pq = PPC_questions[current_question_index]
        
        if a in pq['correct_answer']:
            overall_score += 1
            print("Correct")
        
        else:  
            print("Incorrect")
            wrong_questions.append(pq['question'])

        if current_question_index < len(PPC_questions) - 1:
            clear_widgets()
            current_question_index += 1
            self.ppc()
        else:
            show_result(PPC_questions)


    #premid 1 practical

    def Panatomy(self):
        aq = Anatomy_practical[current_question_index]
        row = 3
        img = anatimgs[current_question_index]
        Label(root, image=img).grid(row=0, column=0)
        Label(root, text=aq['question'],wraplength=1000, font=f, fg="White", bg="#404040").grid(row=1, column=0)

        all_a = [aq['correct_answer']] + aq['wrong_answers']
        shuffle(all_a)

        for answers in all_a:
            button = Button(root, text=answers,wraplength=1000, width=50, bd=5, command=lambda a=answers: self.check_Panat(a))
            button.grid(row=row, column=0)
            row += 1

    def check_Panat(self,a):
        global current_question_index, overall_score
        aq = Anatomy_practical[current_question_index]
        
        if a in aq['correct_answer']:
            overall_score += 1
            print("Correct")
        
        else:  
            print("Incorrect")
            wrong_questions.append(aq['correct_answer'])

        if current_question_index < len(Anatomy_practical) - 1:
            clear_widgets()
            current_question_index += 1
            self.Panatomy()
        else:
            show_result(Anatomy_practical)

        
    def Pchemistry(self):
        cq = Chemistry_practical[current_question_index]
        row = 3
        img = chemimgs[current_question_index]
        Label(root, image=img).grid(row=0, column=0)
        Label(root, text=cq['question'],wraplength=1000, font=f, fg="White", bg="#404040").grid(row=1, column=0)

        all_a = [cq['correct_answer']] + cq['wrong_answers']
        shuffle(all_a)

        for answers in all_a:
            button = Button(root, text=answers,wraplength=1000, width=30, bd=5, command=lambda a=answers: self.check_Pchem(a))
            button.grid(row=row, column=0)
            row += 1

    def check_Pchem(self,a):
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
            self.Pchemistry()
        else:
            show_result(Chemistry_practical)


class mid2:
# premid 2 
# Theoretical
    objects = ["Anatomy","Biology","Chemistry","NIT","All PPC terms"]
    
    def md2_theo(self):
        clear_widgets()
        Label(root, text="⇃Choose your subject⇂", font=f, bg="#404040",fg="White").grid(row=0, column=0)
        object_row = 1
        for object in self.objects:
            obj_button = Button(root, text=object,font=f, bd=5, width=20,command=lambda obj=object:self.get(obj))
            obj_button.grid(row=object_row, column=0)
            object_row += 1
            
    def get(self,selection):
        global obj
        if selection == self.objects[0]:
            clear_widgets()
            obj = self.objects[0]
            self.anatomy2()
        elif selection == self.objects[1]:
            clear_widgets()
            obj = self.objects[1]
            self.biology()
        elif selection == self.objects[2]:
            clear_widgets()
            obj = self.objects[2]
            self.chemistry()
        elif selection == self.objects[3]:
            clear_widgets()
            obj = self.objects[3]
            self.nit()
        elif selection == self.objects[4]:
            clear_widgets()
            obj = self.objects[4]
            self.ppct()


    def anatomy2(self):
        shuffle(Anatomy2_questions)
        aq = Anatomy2_questions[current_question_index]
        row = 3
        Label(root, text=f"Question - {aq['question']}", font=f, fg="White", bg="#404040",wraplength=1000).grid(row=1, column=0)

        all_a = [aq['correct_answer']] + aq['wrong_answers']
        shuffle(all_a)
        
        for answer in all_a:
            button = Button(root, text=answer,font=f ,width = 100, bd=5,wraplength=1000, command=lambda a=answer: self.check_anat2(a))
            button.grid(row=row, column=0)
            row += 1

    def check_anat2(self,a):
        global current_question_index, overall_score
        cq = Anatomy2_questions[current_question_index]
        
        if a in cq['correct_answer']:
            overall_score += 1
            print("Correct")
        
        else:  
            print("Incorrect")
            wrong_questions.append(cq['question'])

        if current_question_index < len(Anatomy2_questions) - 1:
            clear_widgets()
            current_question_index += 1
            self.anatomy2()
        else:
            show_result(Anatomy2_questions)

    
    def ppct(self):
        clear_widgets()
        shuffle(PPC_terms)
        pt = PPC_terms[current_question_index]
        row = 3
        Label(root, text=f"Question - {pt['question']}",wraplength=1000, font=f, fg="White", bg="#404040").grid(row=1, column=0)

        all_a = [pt['correct_answer']] + pt['wrong_answers']
        shuffle(all_a)
        
        for answer in all_a:
            button = Button(root, text=answer,wraplength=1000,font=f ,width=100, bd=5, command=lambda a=answer: self.check_ppct(a))
            button.grid(row=row, column=0)
            row += 1

    def check_ppct(self,a):
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
            self.ppct()
        else:
            show_result(PPC_terms)



The_satrt()
root.mainloop()