
from tkinter import *

root = Tk()

def getvals():
    print(f"the user name is {user_value.get()}")
    print(f"The password is {passvalue.get()}")
root.geometry('444x234')

user = Label(root,text = 'username')
password = Label(root,text = 'password')

user.grid()
password.grid(row=1)

user_value = StringVar()
passvalue = StringVar()

userentry = Entry(root,textvariable=user_value)
passentry = Entry(root,textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

button = Button(text = "submit",command=getvals).grid()

root.mainloop()