

from tkinter import *

root = Tk()
root.title("Events in Tkinter")
root.geometry('644x344')

def ajay(event):
    print(f"you clicked on the button{event.x},{event.y}")

widget = Button(root,text ="click me please")
widget.pack()
widget.bind('<Button-1>',ajay)

root.mainloop()