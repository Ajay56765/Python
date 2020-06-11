
from tkinter import *

root = Tk()

root.geometry('644x344')
root.title("Pycharm")

def myfunc():
    print("hi its me")

# mymenu= Menu(root)
# mymenu.add_command(label = "File",command = myfunc)
# mymenu.add_command(label = "Exits",command = myfunc)
#

mainmenu = Menu(root)
m1 = Menu(mainmenu,tearoff=0)
m1.add_command(label = "Save",command = myfunc )
m1.add_command(label = "Save AS",command = myfunc )
m1.add_command(label = "New Project",command = myfunc )
m1.add_command(label = "Delete",command = myfunc )
m1.add_command(label = "exit",command = myfunc )

mainmenu.add_cascade(label = "file",menu = m1)

root.config(menu = mainmenu)

m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label = "CUT",command = myfunc )
m2.add_command(label = "COPY",command = myfunc )
m2.add_command(label = "PASTE",command = myfunc )
m2.add_command(label = "Find",command = myfunc )
m2.add_command(label = "exit",command = myfunc )

mainmenu.add_cascade(label = "EDIT",menu = m1)
root.config(menu = mainmenu)
root.mainloop()