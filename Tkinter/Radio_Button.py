
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry('644x322')
root.title("RADIOBUTTON")

var = IntVar()

Label(root,text = "What would you like to have sir",justify = LEFT,padx = 14).pack()

radio= Radiobutton(root,text = "Dosa",padx = 14,variable = var,value=1).pack(anchor = W)
radio= Radiobutton(root,text = "SAMOSA",padx = 14,variable = var,value=2).pack(anchor = W)
radio= Radiobutton(root,text = "Idly",padx = 14,variable = var,value=3).pack(anchor = W)
radio= Radiobutton(root,text = "Jalebi",padx = 14,variable = var,value=4).pack(anchor = W)

def order():
    if var.get()==1:
        tmsg.showinfo("Your order","We hvave receive for Dosa")
    elif var.get()==2:
        tmsg.showinfo("Your order","We hvave receive for samosa")
    elif var.get() == 3:
        tmsg.showinfo("Your order", "We hvave receive for Idaly")
    elif var.get()==2:
        tmsg.showinfo("Your order","We hvave receive for Jalebi")

Button(root,text = "ORDER NOW",command = order).pack()

root.mainloop()