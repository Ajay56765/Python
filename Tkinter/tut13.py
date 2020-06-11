


from tkinter import *
import tkinter.messagebox as tmsg

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

mainmenu.add_cascade(label = "FILE",menu = m1)

root.config(menu = mainmenu)

m2 = Menu(mainmenu,tearoff=0)
m2.add_command(label = "CUT",command = myfunc )
m2.add_command(label = "COPY",command = myfunc )
m2.add_command(label = "PASTE",command = myfunc )
m2.add_command(label = "Find",command = myfunc )
m2.add_command(label = "exit",command = myfunc )

mainmenu.add_cascade(label = "EDIT",menu = m1)
root.config(menu = mainmenu)

def help():
    print("How I can help you")
    a = tmsg.showinfo("hi", "buddy")

def rate():
    print("rate us")
    value = tmsg.askquestion("was your experince good","you need more")
    print(value)

    if value == 'yes':
        msg = "Great !! Please rate us on playstore"

    else:
        msg = "Tell us what wents wrong !!"
    tmsg.showinfo("Experince",msg)
    
m3 = Menu(mainmenu,tearoff=0)
m3.add_command(label = "help",command = help)
m3.add_command(label = "Rate us",command = rate)
mainmenu.add_cascade(label = "HELP",menu = m3)
root.config(menu = mainmenu)





root.mainloop()
