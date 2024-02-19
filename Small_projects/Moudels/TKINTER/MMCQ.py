from tkinter import *
from PIL import Image, ImageTk
from random import shuffle
from qs import Anatomy_practical,Anatomy_questions,Biology_questions,Chemistry_practical,Chemistry_questions,NIT_questions,PPC_questions,PPC_terms

root = Tk()
root.title("First Year MCQ Exam")
root.config(bg="#242424")
root.iconbitmap("Images\Icons\MSQ.ico")

f = "TimesNewRoman 16 bold"
f2 = "TimesNewRoman 11 bold"
f3 = "TimesNewRoman 8"
f4 = "TimesNewRoman 1"



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


#global defs
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
            Label(root, text=f'{index}- {wrq}',font=f2).grid(row=r, column=c,sticky=W+N)
            r += 1
            if r == 31:
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
        button = Button(root,text='Practical',font=f, bd=5, width=20)
        button.grid(row=1,column=0)
        button1 = Button(root,text='Impractical',font=f,command=mid1().md1_imprac, bd=5, width=20)
        button1.grid(row=2,column=0)
    if a == 'PreMid 2':
        Label(root,text='Easy or Hard?',font=f, bg="#404040",fg="White").grid(row=0,column=0)
        button = Button(root,text='Practical',font=f, bd=5, width=20)
        button.grid(row=1,column=0)
        button1 = Button(root,text='Impractical',font=f, bd=5, width=20,command=mid2().md2_imprac)
        button1.grid(row=2,column=0)

   
class mid1:
#premid 1 impratcial 
    objects = ["Anatomy","Biology","Chemistry","NIT","PPC"]

    def md1_imprac(self):
        clear_widgets()
        Label(root, text="⇃Choose your subject⇂", font=f, bg="#404040",fg="White").grid(row=0, column=0)
        object_row = 1
        for object in self.objects:
            obj_button = Button(root, text=object,font=f, bd=5, width=20,command=lambda obj=object:self.get(obj))
            obj_button.grid(row=object_row, column=0)
            object_row += 1
    
    def get(self,selection):
        global obj
        if selection == self.self.objects[0]:
            clear_widgets()
            obj = self.objects[0]
            self.anatomy()
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
            self.ppc()


    def anatomy(self):
        shuffle(Anatomy_questions)
        aq = Anatomy_questions[current_question_index]
        row = 3
        Label(root, text=f"Question - {aq['question']}", font=f, fg="White", bg="#404040").grid(row=1, column=0)

        all_a = [aq['correct_answer']] + aq['wrong_answers']
        shuffle(all_a)
        
        for answer in all_a:
            button = Button(root, text=answer,font=f ,width = 100, bd=5, command=lambda a=answer: self.check_anat(a))
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
            wrong_questions.append(cq['correct_answer'])

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
        Label(root, text=f"Question - {bq['question']}", font=f, fg="White", bg="#404040").grid(row=1, column=0)

        all_a = [bq['correct_answer']] + bq['wrong_answers']
        shuffle(all_a)
        
        for answer in all_a:
            button = Button(root, text=answer,font=f ,width=100, bd=5, command=lambda a=answer: self.check_bio(a))
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
            wrong_questions.append(bq['correct_answer'])

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
        Label(root, text=f"Question - {cq['question']}", font=f, fg="White", bg="#404040").grid(row=1, column=0)

        all_a = [cq['correct_answer']] + cq['wrong_answers']
        shuffle(all_a)
        
        for answer in all_a:
            button = Button(root, text=answer,font=f ,width=100, bd=5, command=lambda a=answer: self.check_chem(a))
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
            wrong_questions.append(cq['correct_answer'])

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
        Label(root, text=f"Question - {nq['question']}", font=f, fg="White", bg="#404040").grid(row=1, column=0)

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
            wrong_questions.append(nq['correct_answer'])

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
        Label(root, text=f"Question - {pq['question']}", font=f, fg="White", bg="#404040").grid(row=1, column=0)

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
            wrong_questions.append(pq['correct_answer'])

        if current_question_index < len(PPC_questions) - 1:
            clear_widgets()
            current_question_index += 1
            self.ppc()
        else:
            show_result(PPC_questions)


    #premid 1 practical

    def chemistry_p(self):
        cq = Chemistry_practical[current_question_index]
        row = 3
        img = img_list[current_question_index]
        Label(root, image=img).grid(row=0, column=0)
        Label(root, text=cq['question'], font=f, fg="White", bg="#404040").grid(row=1, column=0)

        all_a = [cq['correct_answer']] + cq['wrong_answers']
        shuffle(all_a)

        for answers in all_a:
            button = Button(root, text=answers, width=30, bd=5, command=lambda a=answers: self.check_chem(a))
            button.grid(row=row, column=0)
            row += 1

    def check_pchem(self,a):
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
            self.chemistry_p()
        else:
            show_result(Chemistry_practical)



class mid2:
#premid 2 
#impractical
    objects = ["Anatomy","Biology","Chemistry","NIT","All PPC terms"]
    
    def md2_imprac(self):
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
            self.anatomy()
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
    
    def ppct(self):
        clear_widgets()
        shuffle(PPC_terms)
        pt = PPC_terms[current_question_index]
        row = 3
        Label(root, text=f"Question - {pt['question']}", font=f, fg="White", bg="#404040").grid(row=1, column=0)

        all_a = [pt['correct_answer']] + pt['wrong_answers']
        shuffle(all_a)
        
        for answer in all_a:
            button = Button(root, text=answer,font=f ,width=100, bd=5, command=lambda a=answer: self.check_ppct(a))
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