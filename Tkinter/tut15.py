
from tkinter import *
import tkinter.messagebox as tmsg

root =Tk()
root.geometry('644x344')



var = StringVar()
var.set("radio")
Label(root,text="What would you like to have Sir !!", font='lucida 19 bold',justify=LEFT,padx=14).pack()

def order():
    tmsg.showinfo("Your Order", f"we received your order for {var.get()} !! Thanks for ordering")

radio = Radiobutton(root,text="Dhosaa",padx=14, variable=var, value='Dhos').pack(anchor=W)
radio = Radiobutton(root,text="Idaly",padx=14, variable=var, value='Idaly').pack(anchor=W)
radio = Radiobutton(root,text="samosa",padx=14, variable=var, value='Samosa').pack(anchor=W)
radio = Radiobutton(root,text="Noodle",padx=14, variable=var, value='Noodle').pack(anchor=W)
radio = Radiobutton(root,text="Vada",padx=14, variable=var, value='vada').pack(anchor=W)

Button(root,text="Order now",command=order).pack()
root.mainloop()
