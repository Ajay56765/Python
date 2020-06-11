from tkinter import *
from PIL import Image, ImageTk


root = Tk()

root.geometry("1000x1000")
# photo = PhotoImage(file = "my.png")

image = Image.open("B612_20191117_151150_424.jpg")
photo = ImageTk.PhotoImage(image)

# photo1 = PhotoImage(file = "B612_20191117_151150_424.jpg")
label = Label(image = photo)
label.pack()

root.mainloop()
