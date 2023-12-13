from tkinter import *

f = "TimesNewRoman 16 bold"
f2 = "TimesNewRoman 11"

root = Tk()
root.title("THE BEST CALCULATOR")
root.configure(bg="#404040")
Label1 = Label(root, text="\nادخل رقماً",bg="#404040",fg="White",font=f).grid(row=0,column=0,columnspan=4)
Input = Entry(root,border="5",background="#404046",fg="White",font=f2)
Input.grid(row=1,column=0,columnspan=4)

def click(i):
    global currenti
    currenti = Input.get()
    Input.delete(0,END)
    Input.insert(0, str(currenti) + str(i) )

def add():
    global n1,Eq
    n1 = Input.get()
    n1 = float(n1)
    Input.delete(0,END)
    Eq = "add"

def subtract():
    global n1,Eq
    n1 = Input.get()
    n1 = float(n1)
    Input.delete(0,END)
    Eq = "sub"

def multiply():
    global n1,Eq
    n1 = Input.get()
    n1 = float(n1)
    Input.delete(0,END)
    Eq = "multi"

def divide():
    global n1,Eq
    n1 = Input.get()
    n1 = float(n1)
    Input.delete(0,END)
    Eq = "divide"

def equal():
    global n1,Eq
    n2 = Input.get()
    n2 = float(n2)
    Input.delete(0,END)

    if Eq == "add":
        result = Label(root,text=f"الناتج:  {n1}+{n2} = {n1 + n2}",font=f2,fg="White",bg="#404040")
    elif Eq == "sub":
        result = Label(root,text=f"الناتج:  {n1}-{n2} = {n1 - n2}",font=f2,fg="White",bg="#404040")
    elif Eq == "multi":
        result = Label(root,text=f"الناتج:  {n1}÷{n2} = {n1 * n2}",font=f2,fg="White",bg="#404040")
    elif Eq == "divide":
        if n2 != 0:
            result = Label(root,text=f"الناتج:  {n1}÷{n2} = {n1 / n2}",font=f2,fg="White",bg="#404040")
        else:result = Label(root,text=f"Can't Divide By ZERO",font=f,fg="White",bg="#404040")

    result.grid(row=2,column=0,columnspan=4)

def clear():
    Input.delete(0,END)
    result = Label(root,bg="#404040",width="34").grid(row=2,column=0,columnspan=6)

blank = Label(root,text="",fg="White",bg="#404040").grid(row=2,column=1)
button0 = Button(root,text="0",padx=30,pady=10,font=f,bg="#d9d9d9",border=3,command=lambda: click(0)).grid(row=6,column=0)
button1 = Button(root,text="1",padx=30,pady=10,font=f,bg="#d9d9d9",border=3,command=lambda: click(1)).grid(row=5,column=0)
button2 = Button(root,text="2",padx=30,pady=10,font=f,bg="#d9d9d9",border=3,command=lambda: click(2)).grid(row=5,column=1)
button3 = Button(root,text="3",padx=30,pady=10,font=f,bg="#d9d9d9",border=3,command=lambda: click(3)).grid(row=5,column=2)
button4 = Button(root,text="4",padx=30,pady=10,font=f,bg="#d9d9d9",border=3,command=lambda: click(4)).grid(row=4,column=0)
button5 = Button(root,text="5",padx=30,pady=10,font=f,bg="#d9d9d9",border=3,command=lambda: click(5)).grid(row=4,column=1)
button6 = Button(root,text="6",padx=30,pady=10,font=f,bg="#d9d9d9",border=3,command=lambda: click(6)).grid(row=4,column=2)
button7 = Button(root,text="7",padx=30,pady=10,font=f,bg="#d9d9d9",border=3,command=lambda: click(7)).grid(row=3,column=0)
button8 = Button(root,text="8",padx=30,pady=10,font=f,bg="#d9d9d9",border=3,command=lambda: click(8)).grid(row=3,column=1)
button9 = Button(root,text="9",padx=30,pady=10,font=f,bg="#d9d9d9",border=3,command=lambda: click(9)).grid(row=3,column=2)
buttonadd = Button(root, text="+", padx=30, pady=10, font=f,bg="#d9d9d9", border=3, command=add).grid(row=6, column=1)
buttonsubtract = Button(root, text="-", padx=32.4, pady=10, font=f,bg="#d9d9d9", border=3, command=subtract).grid(row=6, column=2)
buttonmultiply = Button(root, text="×", padx=30, pady=10, font=f,bg="#d9d9d9", border=3, command=multiply).grid(row=7, column=0)
buttondivide = Button(root, text="÷", padx=30, pady=10, font=f,bg="#d9d9d9", border=3, command=divide).grid(row=7, column=1)
buttonequal = Button(root, text="=", padx=30, pady=10, font=f,bg="#d9d9d9", border=3, command=equal).grid(row=7, column=2)
buttonclear = Button(root,text="CLEAR",padx=95,pady=10,font=f,bg="#d9d9d9",border="3.5",command=clear).grid(row=8,column=0,columnspan=3)

root.mainloop() 