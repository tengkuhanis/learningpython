# PROGRAM TO IMPLEMENT HASHING USING GUI
'''
ECIE3101/ECIE3312 DATA STRUCTURE AND ALGORITHM DESIGN
SEMESTER 1 20/21
PROJECT THEME: VISUALIZATION OF DATA STRUCTURE

=============== COLLABORATORS =====================

ECIE3312:
-Tengku Hanis Sofea Tengku Effendy (1810258)
-Nur Ain Nabila binti Mohd Rozi    (1815508)
-Siti Nur Farzana Binti Mohd Nasir (1818400)
-Nurul Farah Hazry binti Edy Hazry (1817042)
-Sarah Hannani binti Abdul Manah   (1912850)

ECIE3101:
-Tengku Hanis Sofea Tengku Effendy (1810258)
-Muhammad Adhwa Fathullah bin Nor Asmadi (1729131)
-Siti Nur Farzana Binti Mohd Nasir (1818400)
-Nur Ain Nabila binti Mohd Rozi (1815508)
-Ahmad Rahimi bin Yusoff (1722199)
'''

from tkinter import *

position, value, put = [], [], []
val = []

def keyval():
    insert = Toplevel(window)
    insert.title("Hash Keys")
    insert.geometry("500x300")
    Label(insert, text="Enter the values and click 'Hash Now'.").grid(row=0, sticky=W)
    Label(insert, text="Enter '0' if you don't want to insert any more ").grid(row=1, sticky=W)
    Label(insert, text="values in the rest of the table.").grid(row=2, sticky=W)
    for i in range(int(type2.get())):
        x = Entry(insert)
        x.grid(row=i+3, column=0)
        value.append(x)


    Button(insert,text="Hash Now", fg='pink', bg='black', command=hashing).grid(row=i+3, column=1)

def hashing():
    global x
    table = Toplevel(window)
    table.title("Hash Table")
    table.geometry("500x300")
    for i in range(int(type2.get())):
        position = int(value[i].get()) % int(type2.get())
        put.append(position)
    print(put)

    for entry in value:
        val.append(int(entry.get()))

    Label(table, text="These are the positions of the entered elements"
                      "\naccording to their sequence from left to right.").grid(row=0, column=0, sticky=W)
    Label(table, text=[entry for entry in put]).grid(row=1, column=0, sticky=W)
    Button(table, text="Quit", fg='orange', bg='black', command=quit).grid(row=2, column=0)

def quit():
    window.destroy()

# main function
window = Tk()
window.title("Hashing")
window.geometry("500x300")
Label(window, text="Hello!").grid(row=0, sticky=W)
Label(window, text="Types of hashing algorithm:").grid(row=1, sticky=W)
Label(window, text="1-Quadratic Probing").grid(row=2, sticky=W)
Label(window, text="2-Cubic Probing").grid(row=3, sticky=W)
Label(window, text="Choose a hashing type(1 or 2):").grid(row=4, sticky=W)
type1 = Entry(window)
type1.grid(row=4, column=1)

Label(window, text="Enter the Size of the hash table:").grid(row=5, sticky=W)
type2 = Entry(window)
type2.grid(row=5, column=1)

btnNext = Button(window,text="Next", fg='light blue', bg='black', command=keyval)
btnNext.grid(row=6, column=1, sticky=SE)

window.mainloop()