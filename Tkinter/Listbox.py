
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry('455x245')
root.title("LISTBOX TUTORIAL")

lbx = Listbox(root)

lbx.pack()
lbx.insert(END, "First Item of your listbox")

i=0
def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1

Button(root,text ="Add",command = add).pack()

root.mainloop()