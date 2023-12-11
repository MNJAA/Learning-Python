from tkinter import *
from time import sleep

root = Tk()
input = Entry(root)
input.grid(row=55,column=50)
input.insert(0,"Enter YES")
def yes():
    V = input.get()
    if V == "YES":
      text4 = Label(root, text="YES IT IS",fg="DarkGreen").grid(row=56,column=50)
    else:
        sleep(2)
        text5 = Label(root, text="Try later").grid(row=56,column=50)
text0 = Label(root, text="================================").grid(row=0,column=50)
text1 = Label(root, text="is it working?",fg="Red").grid(row=54,column=50)
text2 = Button(root, text="????",fg="DarkBlue", padx=10,command=yes).grid(row=57,column=50)
text3 = Label(root, text="================================").grid(row=58,column=50)

root.mainloop() 