
from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f'{canvas_width}x{canvas_height}')

can_widget = Canvas(root, width = canvas_width,height = canvas_height)
can_widget.pack()

#from x1,y1 to x2,y2
can_widget.create_line(500,500,100,100)
can_widget.create_oval(100,300,400,200,fill="red")
can_widget.create_text(200,200,text="Python")
root.mainloop()