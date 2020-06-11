from tkinter import *

root = Tk()

root.geometry('944x444')
root.title("SCROLLBAR")

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT,fill = Y)

# listbox = Listbox(root, yscrollcommand =  scrollbar.set)
#
# for i in range(344):
#     listbox.insert(END,f"Item {i}")
#
# listbox.pack(fill = 'both')

# scrollbar.config(command = listbox.yview)


text= Text(root,yscrollcommand = scrollbar.set)
text.pack(fill = BOTH)
scrollbar.config(command = text.yview())
root.mainloop()