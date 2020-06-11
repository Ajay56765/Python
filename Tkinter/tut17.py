from tkinter import *

root = Tk()
root.geometry('644x344')
root.title("Scrollbar")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

listbox=Listbox(root,yscrollcommand=scrollbar.set)

for i in range(344):
    listbox.insert(END,f"Item {i}")


listbox.pack()
root.mainloop()