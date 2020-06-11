
from tkinter import *

root=Tk()
root.geometry('644x344')
root.title("List Tutorial")

lbx= Listbox(root)
lbx.pack()
lbx.insert(END,"First item to be inseted")

def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1

i=0
Button(root,text = 'Add Item',command = add).pack()

root.mainloop()