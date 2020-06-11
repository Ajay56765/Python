from tkinter import *

root = Tk()

root.geometry('644x344')

Label(root,text = "Welcome to Ajay Travels", font = 'comicsansms 10 bold',pady=15).grid(row =0,column=3)
name = Label(root,text = "Name")
phone = Label(root,text = "Phone")
Gender = Label(root,text = "Gender")
Emergency = Label(root,text = "Emergency contact")
paymentmode = Label(root,text = "Payment mode")

#Packing
name.grid(row = 1,column = 2)
phone.grid(row = 2,column = 2)
Gender.grid(row = 3,column = 2)
Emergency.grid(row=4 ,column = 2)
paymentmode.grid(row=5 ,column = 2)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
Emergencyvalue = StringVar()
paymentvalue = StringVar()
foodservicevalue = IntVar()

nameentry = Entry(root, textvariable = namevalue)
phoneentry = Entry(root, textvariable = phonevalue)
genderentry = Entry(root, textvariable =gendervalue )
Emergencyentry = Entry(root, textvariable = Emergencyvalue)
paymententry = Entry(root, textvariable = paymentvalue)


nameentry.grid(row=1, column= 3)
phoneentry.grid(row=2, column= 3)
genderentry.grid(row=3, column= 3)
Emergencyentry.grid(row=4, column= 3)
paymententry.grid(row=5, column= 3)


foodservice = Checkbutton(text = "want to get your meals",variable = foodservicevalue)
foodservice.grid(row = 6, column=3)

def getval():
    print("Submitted !!")

Button(text = "SUBMIT", command=getval,fg = "blue").grid(row=8,column=3)

root.mainloop()