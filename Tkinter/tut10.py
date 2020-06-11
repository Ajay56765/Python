
from tkinter import *

root = Tk()

def ajay(event):
    print(f'you clicked on the button at {event.x},{event.y}')
root.title("Events Tkinter")
root.geometry('644x244')
widget = Button(root,text = 'Click me')
widget.pack()

widget.bind('<Button-1>', ajay)
widget.bind('<Double-1>',quit)
root.mainloop()