from tkinter import *
import tkinter.messagebox
window = Tk()
window.title("Registration Form")
window.geometry('900x1200')
window.configure(background ="azure")

Page = Label(window, text="Employee Registration Form ", font=("bold", 20)).grid(row=0, column=2)
First_Name = Label(window, text ="First Name", width=20, font=("bold", 12)).grid(row = 1, column = 1)
Last_Name = Label(window, text ="Last Name", width=20, font=("bold", 12)).grid(row = 2, column = 1)
Address = Label(window, text ="Address", width=20, font=("bold", 12)).grid(row = 3, column = 1)
City = Label(window, text ="City", width=20, font=("bold", 12)).grid(row = 4, column = 1)
State = Label(window, text ="State", width=20, font=("bold", 12)).grid(row = 5, column = 1)
Country = Label(window, text ="Country", width=20, font=("bold", 12)).grid(row = 7, column = 1)
Postal = Label(window, text ="Postal /Zip Code", width=20, font=("bold", 12)).grid(row = 6, column = 1)
list1 = ['India', 'America', 'Portugal', 'Spain', 'Australia', 'Brazil']
a = StringVar()
droplist = OptionMenu(window, a, *list1)
droplist.config(width=15)
a.set('select your country')
droplist.grid(row=7, column=2)
Mobile = Label(window, text ="Contact Number", width=20, font=("bold", 12)).grid(row = 8, column = 1)
Email = Label(window, text ="Email Id", width=20, font=("bold", 12)).grid(row = 9, column = 1)
Gender = Label(window, text ="Gender", width=20, font=("bold", 12)).grid(row = 10, column = 1)
var = IntVar()
Radiobutton(window, text="Male", padx = 30, variable=var, value=1).grid(row = 10, column = 2)
Radiobutton(window, text="Female", padx = 20, variable=var, value=2).grid(row = 10, column = 3)
Choose = Label(window, text="Date Of Birth", width=20, font=("bold", 12)).grid(row = 11, column = 1)
label_12 = Label(window, text="Programming", width=20, font=("bold", 12))
label_12.grid(row=12, column=1)
var1 = IntVar()
Checkbutton(window, text="java", variable=var1).grid(row = 12, column = 2)
var2 = IntVar()
Checkbutton(window, text="python", variable=var2).grid(row = 12, column = 3)

# Creating CheckBox
# The variable 'variable' mentioned here holds Integer value, by default 0
variable=IntVar()

# This will creates checkbutton widget and uses place() method.
Checkbutton(window, text="I Accept all Term and Conditions", variable=variable).place(x=100, y=400)

First_Name1 = Entry(window).grid(row=1, column=2)
Last_Name1 = Entry(window).grid(row=2, column=2)
Adderss1 = Entry(window).grid(row=3, column=2)
City1 = Entry(window).grid(row=4, column=2)
State1 = Entry(window).grid(row=5, column=2)
Postal1 = Entry(window).grid(row=6, column=2)
Email1 = Entry(window).grid(row=9, column=2)
Mobile1 = Entry(window).grid(row=8, column=2)
choose = Entry(window).grid(row=11, column=2)


def onClick():
    tkinter.messagebox.showinfo("Welcome", "Submitted  Successfully :)")


# Create a Button
Button(window, text="Submit", command=onClick, width=40, bg='deep pink4', fg='white').place(x=100, y=450)


window.mainloop()