from tkinter import *
from tkinter import messagebox
my_app = Tk()
my_app.title("Menghitung Luas Bangun")

L1 = Label(my_app, text="Bangun Geometri", font=("Arial", 17))
L1.grid(row=0, column=0, sticky="W")

L2 = Label(my_app, text="Persegi merupakan bangun datar 2 dimensi yang terdiri dari 4 sisi yang sama panjang dan memiliki 4 sudut yang sama besar,contoh benda yang berbentuk persegi adalah keramik/ubin lantai")
L2.grid(row=1, column=0, sticky="W")

L3 = Label(my_app, text="s1: ")
L3.grid(row=2, column=0, sticky="W")

L4 = Label(my_app, text="s2: ")
L4.grid(row=3, column=0, sticky="W")

str1 = StringVar(value=0)
E3 = Entry(my_app, textvariable = str1)
E3.grid(row=2, column=0)
str2 = StringVar(value=0)
E4 = Entry(my_app, textvariable = str2)
E4.grid(row=3, column=0)

def luas():
    "Menghitung Luas Persegi"
    s1 = float(str1.get())
    s2 = float(str2.get())
    l = float(s1*s2)
    L = float(l)
    B.config(text="Luas=" + L)
    
B = Button(my_app, text="Hitung luas", command=luas)
B.grid(row=5, column=0)

my_app.mainloop()
