
from tkinter import *

root =Tk()

root.geometry("444x234")

f1 = Frame(root,bg = 'grey',borderwidth =6,relief = SUNKEN)
f2 = Frame(root,borderwidth = 8,bg ='grey',relief = SUNKEN)

f2.pack(side = "top",fill =X)
f1.pack(side = "left",fill=Y)

l1 = Label(f2,text = "Pycharm",bg = 'white',fg = 'red',font = "comicsansms 10 italic")
l = Label(f1,text = "Project Tkinter")

l.pack(pady=130)
l1.pack()

root.mainloop()