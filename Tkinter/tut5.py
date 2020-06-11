
from tkinter import *

root = Tk()

def hello():
    print("Hello Kinter bittons")

def name():
    print("my name is ajay")


root.geometry("444x234")
frame = Frame(root,borderwidth = 6,bg = 'grey',relief = SUNKEN)
frame.pack(side = "top",anchor ='nw')

b1 = Button(frame, fg = "red",text = "print now",command = hello)
b1.pack(side = "top",padx = 2,anchor = 'nw')

b2 = Button(frame, fg = "red",text = "whats your name",command = name)
b2.pack(side = "bottom",pady = 10,anchor = 'nw')

b3 = Button(frame, fg = "red",text = "Python Ide")
b3.pack(side = "bottom",pady = 10,anchor = 'nw')

b4 = Button(frame, fg = "red",text = "M.L module")
b4.pack(side = "bottom",pady = 10,anchor = 'nw')

b1 = Button(frame, fg = "red",text = "degnation")
b1.pack(side='bottom',pady = 10,anchor = 'nw')
root.mainloop()