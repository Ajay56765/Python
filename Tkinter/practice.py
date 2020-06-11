
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.geometry('1000x800')


label1 = Label(root, text = "FILL THE APPLICATION",font = 'comicsansms 12 bold',fg = "black",bg = "grey",padx = 13).grid(row=0,column=4,sticky = E,pady = 10)
#label2 = Label(root,text= "NOTE : PLEASE READ THE INSTRUCTION CAREFULLY",font = "comicsansms 10 italic").grid(row=1,column=1)



Ft_name = Label(root,text = "FIRST NAME",padx=1, pady =10,font = 'bold',anchor=E,justify = LEFT).grid(row=2,column=0)
lt_name = Label(root,text = "LAST_NAME",pady =10,font = 'bold').grid(row=2,column=10)
Father_Name = Label(root,text = "FATHER_NAME",pady =10,font = 'bold').grid(row=4,column=0)
MOb_no= Label(root,text = "MOB NO",pady =10,font = 'bold').grid(row=5,column=0)
DOB = Label(root,text = "DATE OF BIRTH",pady =10,font = 'bold').grid(row=6,column=0)
address = Label(root,text = "PRESENT ADDRESS ",pady =10,font = 'bold').grid(row=7,column=0)
pin_code = Label(root,text = "PIN CODE",pady =10,font = 'bold').grid(row=8,column=0)
gender = Label(root,text = "GENDER",pady =10,font = 'bold').grid(row=9,column=0)

fstname = StringVar()
lastname = StringVar()
fathername =StringVar()
mobno = IntVar()
dateofb = StringVar()
address =StringVar()
pincode = IntVar()
gender = IntVar()

ftname = Entry(root,textvariable = fstname).grid(row=2,column=3)
ltname = Entry(root,textvariable = lastname).grid(row=2,column=15)
fathername = Entry(root,textvariable = fathername).grid(row=4,column=3)
mbno = Entry(root,textvariable = mobno).grid(row=5,column=3)
db = Entry(root,textvariable = dateofb).grid(row=6,column=3)
addres = Text(root,height = 5,width = 25).grid(row=7,column=3)

pncode = Entry(root,textvariable = pin_code).grid(row=8,column=3)


def genders():

    if gender.get()==1:
        print("selecetd MALE")
    if gender.get()==2:
        print("selected female")
    else:
        print("selected other")
R1 = Radiobutton(root, text="MALE", variable=gender, value=1,command=genders).grid(row =9 ,column =3 )
R2 = Radiobutton(root, text="FEMALE", variable=gender, value=2,command=genders).grid(row =9 ,column =4 )
R3 = Radiobutton(root, text="OTHER", variable=gender, value=3,command=genders).grid(row =9 ,column =5 )

check_box = Checkbutton(root,text = "Read the Instrauction").grid(row = 10,column = 4)
chekc_button = Button(root,text = "Allow to submit").grid(row = 12,column = 4)


root.mainloop()