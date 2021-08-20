from tkinter import *


root = Tk()
root.title('Calculator')

entry = Entry(root, width=25)
entry.grid(row=0, column=0, columnspan=3)


def button_clicked(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def clear():
    entry.delete(0, END)


def add():
    global c_num
    global maths
    maths = 'add'
    current = entry.get()
    c_num = int(current)
    entry.delete(0, END)
    next_num = entry.get()


def sub():
    global c_num
    global maths
    maths = 'sub'
    current = entry.get()
    c_num = int(current)
    entry.delete(0, END)
    next_num = entry.get()


def mul():
    global c_num
    global maths
    maths = 'mul'
    current = entry.get()
    c_num = int(current)
    entry.delete(0, END)
    next_num = entry.get()


def div():
    global c_num
    global maths
    maths = 'div'
    current = entry.get()
    c_num = int(current)
    entry.delete(0, END)
    next_num = entry.get()


def equals():
    next_num = entry.get()
    entry.delete(0, END)
    if maths == 'add':
        entry.insert(0, c_num+int(next_num))

    elif maths == 'sub':
        entry.insert(0, c_num-int(next_num))

    elif maths == 'mul':
        entry.insert(0, c_num*int(next_num))

    elif maths == 'div':
        entry.insert(0, c_num/int(next_num))


button_1 = Button(text='1', padx=20, pady=10, command=lambda: button_clicked(1), borderwidth=4)
button_2 = Button(text='2', padx=20, pady=10, command=lambda: button_clicked(2), borderwidth=4)
button_3 = Button(text='3', padx=20, pady=10, command=lambda: button_clicked(3), borderwidth=4)
button_4 = Button(text='4', padx=20, pady=10, command=lambda: button_clicked(4), borderwidth=4)
button_5 = Button(text='5', padx=20, pady=10, command=lambda: button_clicked(5), borderwidth=4)
button_6 = Button(text='6', padx=20, pady=10, command=lambda: button_clicked(6), borderwidth=4)
button_7 = Button(text='7', padx=20, pady=10, command=lambda: button_clicked(7), borderwidth=4)
button_8 = Button(text='8', padx=20, pady=10, command=lambda: button_clicked(8), borderwidth=4)
button_9 = Button(text='9', padx=20, pady=10, command=lambda: button_clicked(9), borderwidth=4)
button_0 = Button(text='0', padx=20, pady=10, command=lambda: button_clicked(0), borderwidth=4)
button_plus = Button(text='+', padx=19, pady=10, command=add, borderwidth=4)
button_sub = Button(text='-', padx=20, pady=10, command=sub, borderwidth=4)
button_mul = Button(text='x', padx=20, pady=10, command=mul, borderwidth=4)
button_div = Button(text='/', padx=20, pady=10, command=div, borderwidth=4)
button_equal = Button(text='=', padx=40, pady=10, command=equals, borderwidth=4)
button_clear = Button(text='Clear', padx=10, pady=10, command=clear)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_plus.grid(row=4, column=1)
button_clear.grid(row=4, column=2)
button_equal.grid(row=6, column=0,columnspan=3)
button_sub.grid(row=5, column=0)
button_mul.grid(row=5, column=1)
button_div.grid(row=5, column=2)

root.mainloop()
