

from tkinter import *
import tkinter.messagebox as tmsg

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

m3 = Menu(root,tearoff=0)

def help():
    print("How may I help you")
    a= tmsg.showinfo("HELP CENTRE","How may I help you")
    print(a)

def rate():
    v= tmsg.askquestion("was Your experience ","Did you enjoy")
    print(v)
    if v =="yes":
        msg = "Please rate us on playstore"

    else:
        msg = "Please tell us what went wrong"
    tmsg.showinfo("your feedback",msg)

def buy():

    print("Would you like to buy")
    ans = tmsg.askretrycancel("Paytment","would you like to buy")
    if ans:
        tmsg.showinfo("Try","Try one more time")
    else:
        tmsg.showinfo("Crossed the limit",
                      "You crossed the maximum limit")

m3.add_command(label = "Help",command = help)
m3.add_command(label = "Rate us",command = rate)
m3.add_command(label = "BUY",command = buy)

Mainmenu.add_cascade(label = "HELP",menu = m3)
root.config(menu = Mainmenu)


root.mainloop()


