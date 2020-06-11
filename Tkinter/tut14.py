
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()

root.geometry('644x344')
root.title("Slider Tutorial")
myslider = Scale(root, from_= 0, to=100, orient = HORIZONTAL,tickinterval = 25)

def getdollar():
    print(f"we have credited {myslider.get()} dollars to your bank")
    tmsg.showinfo("AMount detail",f"we have credited {myslider.get()} dollars to your bank")

Button(root,text = "GET DOLLAR",command = getdollar).pack()
myslider.set(20)
myslider.pack()

root.mainloop()