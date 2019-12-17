from tkinter import *
from tkinter import messagebox
my_app = Tk()
my_app.title("kalkulator")

L1 = Label(my_app, test = "first number")
L1.grid(row=0, column=0)
str1 = StringVar()
E1 = Entry(my_app, textvariable=str1)
E1.grid(row=0, column=1, columnspan=3)
L2 = Label(my_app, text = "second number")
L2.grid(row=1, column=0)
str2 = StringVar()
E2 = Entry(my_app, textvariable = str2)
E2.grid(row=0, column=1)
L3 = Label(my_app, text = "result")
L3.grid(row=1, column=0)
L4 = Label(my_app, text = "0")
L4.grid(row=1, column=1)

def plus():
    a = float (str1.get())
    b = float (str2.get())
    hasil = a+b
    L4.config(text=hasil)

def minus():
    c = float (str1.get())
    d = float (str2.get())
    hasil = c-d
    
