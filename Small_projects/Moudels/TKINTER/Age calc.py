from tkinter import *
from datetime import datetime
from ANSI import BrightGreen,un

#set the base
root = Tk()
root.title("Age Calculator")
root.config(bg="#242424")

f = "TimesNewRoman 16 bold"
f2 = "TimesNewRoman 11"
f3 = "TimesNewRoman 8"
f4 = "TimesNewRoman 1"

Label_000 = Label(root,text='',font=f4,bg='#242424').grid(row=1,column=0)
Label_00 = Label(root,text='',font=f4,bg='#242424').grid(row=5,column=4)
Label_0 = Label(root,text='Months = 31 day, Enter numbers only',font=f3,fg='red',bg='#242424').grid(row=6,column=1,columnspan=3)
Button_0 = Button(root,text='Exit',bg='#242424',font=f3,fg='red',bd=5,command=exit)
Button_0.grid(row=0,column=3,sticky=NE)

def exit():
    root.destroy


def start():
    global Label_1
    global Button_1
    Label_1 = Label(root,text='Know how old are you' ,font=f,fg='White',bg='#242424')
    Label_1.grid(row=2,column=1,columnspan=3)
    Button_1 = Button(root, text= 'start',font=f2,fg='Black',bd=5,command=start_ending)
    Button_1.grid(row=3,column=1,columnspan=3)
    
def start_ending():
    Label_1.destroy()
    Button_1.destroy()
    year()


def year():
    global Label_2
    global Enter_1
    global Button_2
    Label_2 = Label(root,text='Enter The year. Ex:2024' ,font=f,fg='White',bg='#242424')
    Label_2.grid(row=2,column=1,columnspan=3)
    Enter_1 = Entry(root,bg='#737375',fg='White')
    Enter_1.grid(row=3,column=1,padx=20,columnspan=3)
    Button_2 = Button(root, text= 'Enter',font=f2,fg='Black',command=year_ending)
    Button_2.grid(row=4,column=1,columnspan=3)
    
def year_ending():
    global Y
    Y = Enter_1.get()
    Label_2.destroy()
    Button_2.destroy()
    Enter_1.destroy()
    month()
    Button_5 = Button(root, text= 'Repeat',bg='#242424',font=f3,fg='red',bd=5,command=year)
    Button_5.grid(row=0,column=3,sticky=NW)


def month():
    global Label_3
    global Enter_2
    global Button_3
    Label_3 = Label(root,text='Enter The month. Ex:12' ,font=f,fg='White',bg='#242424')
    Label_3.grid(row=2,column=1,columnspan=3)
    Enter_2 = Entry(root,bg='#737375',fg='White')
    Enter_2.grid(row=3,column=1,padx=20,columnspan=3)
    Button_3 = Button(root, text= 'Enter',font=f2,fg='Black',command=month_ending)
    Button_3.grid(row=4,column=1,columnspan=3)

def month_ending():
    global M
    M = Enter_2.get()
    Label_3.destroy()
    Button_3.destroy()
    Enter_2.destroy()
    day()


def day():
    global Label_4
    global Enter_3
    global Button_4
    Label_4 = Label(root,text='Enter The day. Ex:31' ,font=f,fg='White',bg='#242424')
    Label_4.grid(row=2,column=1,columnspan=3)
    Enter_3 = Entry(root,bg='#737375',fg='White')
    Enter_3.grid(row=3,column=1,padx=20,columnspan=3)
    Button_4 = Button(root, text= 'Enter',font=f2,fg='Black',command=day_ending)
    Button_4.grid(row=4,column=1,columnspan=3)

def day_ending():
    global D
    D = Enter_3.get()
    Label_4.destroy()
    Button_4.destroy()
    Enter_3.destroy()
    age()


def age():
    global Y, M, D
    try:
        Y = int(Y)
        M = int(M)
        D = int(D)
    except:TypeError
    
    current_date = datetime.now().date()
    y = current_date.year
    m = current_date.month
    d = current_date.day
    t = datetime.now().time()
    
    yage = 0
    mage = 0
    dage = 0
    
    if Y < y:
        yage = y - Y
        
        if M < m:
            mage = m - M
        elif M > m:
            yage -= 1
            mage = 12 - (M - m)
            
        if D < d:
            dage = d - D
        elif D > d:
            if M == m:
                yage -= 1
            # Assuming every month has 31 days for simplicity
            dage = d + (31 - D)
    elif Y == y:
        if M < m:
            yage = 0
            mage = m - M
            if D < d:
                dage = d - D
            elif D > d:
                dage = d + (31 - D)
        elif M == m:
            if D < d:
                yage = 0
                mage = 0
                dage = d - D
            elif D > d:
                yage = 0
                mage = 0
                dage = d + (31 - D)
        else:year()
                
    Age = f"{yage} Years, {mage} Months, {dage} Days And {t}"
    Label_5 = Label(root,text=f'Your age: {Age}' ,font=f,fg='White',bg='#242424')
    Label_5.grid(row=2,column=1,columnspan=3)


start()


root.mainloop()