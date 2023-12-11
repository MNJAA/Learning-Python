from tkinter import *
from time import sleep

root = Tk()
root.title("THE BEST CALCULATOR")
root.configure(bg="#404040")
Label1 = Label(root, text="\nEnter a Number",bg="#404040",fg="White").grid(row=0,column=0,columnspan=4)
Input = Entry(root,border="5",background="#404046",fg="White")
Input.grid(row=1,column=0,columnspan=4)


def click(i):
    global currenti 
    currenti = Input.get()
    Input.delete(0,END)
    Input.insert(0, str(currenti) + str(i) )
    
def add():
    global n1
    n1 = Input.get()
    n1 = float(n1)
    Input.delete(0,END)

def equal():
    n2 = Input.get()
    n2 = float(n2)
    Input.delete(0,END)
    global result
    result = Label(root,text=f"Result:  {n1}+{n2} = {n1 + n2}",fg="White",bg="#404040").grid(row=2,column=0,columnspan=4)

def clear():
    Input.delete(0,END)
    result = Label(root,bg="#404040",width="20").grid(row=2,column=0,columnspan=4)
    
blank = Label(root,text="",fg="White",bg="#404040").grid(row=2,column=1)
button0 = Button(root,text="0",padx=30,pady=10,border="3",command=lambda: click(0)).grid(row=6,column=0)
button1 = Button(root,text="1",padx=30,pady=10,border="3",command=lambda: click(1)).grid(row=5,column=0)
button2 = Button(root,text="2",padx=30,pady=10,border="3",command=lambda: click(2)).grid(row=5,column=1)
button3 = Button(root,text="3",padx=30,pady=10,border="3",command=lambda: click(3)).grid(row=5,column=2)
button4 = Button(root,text="4",padx=30,pady=10,border="3",command=lambda: click(4)).grid(row=4,column=0)
button5 = Button(root,text="5",padx=30,pady=10,border="3",command=lambda: click(5)).grid(row=4,column=1)
button6 = Button(root,text="6",padx=30,pady=10,border="3",command=lambda: click(6)).grid(row=4,column=2)
button7 = Button(root,text="7",padx=30,pady=10,border="3",command=lambda: click(7)).grid(row=3,column=0)
button8 = Button(root,text="8",padx=30,pady=10,border="3",command=lambda: click(8)).grid(row=3,column=1)
button9 = Button(root,text="9",padx=30,pady=10,border="3",command=lambda: click(9)).grid(row=3,column=2)
buttonadd = Button(root,text="+",padx=30,pady=10,border="3",command=add).grid(row=6,column=1)
buttonequal = Button(root,text="=",padx=30,pady=10,border="3",command=equal).grid(row=6,column=2)
buttonclear = Button(root,text="CLEAR",padx=95,pady=10,border="3.5",command=clear).grid(row=7,column=0,columnspan=3)

root.mainloop() 