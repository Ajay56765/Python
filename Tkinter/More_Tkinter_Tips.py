
from tkinter import *

root = Tk()
root.geometry('644x444')
root.title("AJAY-GUI")
root.wm_iconbitmap("privacy_icon_146112.ico")
root.configure(background = "grey" )
width = root.winfo_screenwidth()
height = root.winfo_height()

print(f'{width}x{height}')
Button(root,text = 'close',command = root.destroy).pack()
root.mainloop()