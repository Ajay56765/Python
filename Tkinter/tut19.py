

from tkinter import *

root = Tk()

root.geometry('644x344')
root.title("Tkinter_Menu")

def myfunc():
    print("Hi Its Menu function !!")

Mainmenu = Menu(root)

m1 = Menu(Mainmenu,tearoff = 0)
m1.add_command(label = 'File',command = myfunc)
m1.add_command(label = 'SAVE',command = myfunc)
m1.add_separator()
m1.add_command(label = 'SAVE AS',command = myfunc)
m1.add_command(label = 'EDIT',command = myfunc)


Mainmenu.add_cascade(label = "File",menu =m1)

m2 = Menu(Mainmenu,tearoff = 0)
m2.add_command(label = 'CUT',command = myfunc)
m2.add_command(label = 'COPY',command = myfunc)
m2.add_separator()
m2.add_command(label = 'PASTE',command = myfunc)
m2.add_command(label = 'COPY PATH',command = myfunc)

root.config(menu = Mainmenu)
Mainmenu.add_cascade(label = "Edit",menu =m2)


root.mainloop()


