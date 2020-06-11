

from tkinter import *

root = Tk()
root.geometry('644x344')

statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root,textvariable = statusvar,relief =SUNKEN,anchor = 'w')
sbar.pack(side =BOTTOM,fill=X)

def upload():
    statusvar.set("BUSY>>>>>>>")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready NOW")
Button(root,text = "UPLOAD",command = upload).pack()


root.mainloop()