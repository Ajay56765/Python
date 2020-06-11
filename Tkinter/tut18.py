

from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry('644x344')
root.title("SLIDER")
#
# myslider1 = Scale(root,from_ = 0, to =455)
# myslider1.pack()
Label(root,text = "How manu dollars you want").pack()
myslider2 = Scale(root,from_ = 0, to =455,orient = HORIZONTAL,tickinterval =200)
myslider2.set(10)
def get_dollar():
    tmsg.showinfo("your Account",f"We have credied {myslider2.get()} dollars to your account")


myslider2.pack()

Button(root,text = "GET DOLLARS",pady =10,command = get_dollar).pack()

root.mainloop()