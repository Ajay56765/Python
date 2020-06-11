
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry('644x344')
width = StringVar()
height = StringVar()

Entry(root,textvariable = width).pack()
Entry(root,textvariable = height).pack()

def Update():
    tmsg.showinfo("Software update","Updating software")

    root.geometry(f"{width.get()}x{height.get()}")

Button(root,text = "Apply",command = Update).pack()

root.mainloop()