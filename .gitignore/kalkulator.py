from tkinter import *

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def button_add():
    firstNumber = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(firstNumber)
    entry.delete(0, END)

def button_minus():
    firstNumber = entry.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(firstNumber)
    entry.delete(0, END)

def button_multiplication():
    firstNumber = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(firstNumber)
    entry.delete(0, END)

def button_division():
    firstNumber = entry.get()
    global f_num
    global math
    math = "division"
    f_num = int(firstNumber)
    entry.delete(0, END)

def clear():
    entry.delete(0, END)

def button_equal():
    secondNumber = entry.get()
    entry.delete(0, END)

    if math == "addition":
        entry.insert(0, f_num + int(secondNumber))
    if math == "substraction":
        entry.insert(0, f_num - int(secondNumber))
    if math == "multiplication":
        entry.insert(0, f_num * int(secondNumber))
    if math == "division":
        try:
            entry.insert(0, f_num / int(secondNumber))
        except:
            print("Nie dziel przez 0")

root = Tk()
root.title("Calculator")
root.geometry("184x220")

entry = Entry(root, borderwidth=0, bg="#666666", fg="#eeeeee", font=("Helvetica", 16))
entry.place(x=10, y=10, width=164, height=40)

one = Button(root, text="1", command=lambda: button_click(1))
two = Button(root, text="2", command=lambda: button_click(2))
three = Button(root, text="3", command=lambda: button_click(3))
four = Button(root, text="4", command=lambda: button_click(4))
five = Button(root, text="5", command=lambda: button_click(5))
six = Button(root, text="6", command=lambda: button_click(6))
seven = Button(root, text="7", command=lambda: button_click(7))
eight = Button(root, text="8", command=lambda: button_click(8))
nine = Button(root, text="9", command=lambda: button_click(9))
zero = Button(root, text="0", command=lambda: button_click(0))

add = Button(root, text="+", command=button_add)
subtract = Button(root, text="-", command=button_minus)
multiply = Button(root, text="*", command=button_multiplication)
divide = Button(root, text="/", command=button_division)
equal = Button(root, text="=", command=button_equal)
clear = Button(root, text="C", command=clear)

button_width = 40
button_height = 40

seven.place(x=12, y=50, width=button_width, height=button_height)
eight.place(x=52, y=50, width=button_width, height=button_height)
nine.place(x=92, y=50, width=button_width, height=button_height)
add.place(x=132, y=50, width=button_width, height=button_height)

four.place(x=12, y=90, width=button_width, height=button_height)
five.place(x=52, y=90, width=button_width, height=button_height)
six.place(x=92, y=90, width=button_width, height=button_height)
subtract.place(x=132, y=90, width=button_width, height=button_height)

one.place(x=12, y=130, width=button_width, height=button_height)
two.place(x=52, y=130, width=button_width, height=button_height)
three.place(x=92, y=130, width=button_width, height=button_height)
multiply.place(x=132, y=130, width=button_width, height=button_height)

zero.place(x=12, y=170, width=button_width, height=button_height)
clear.place(x=52, y=170, width=button_width, height=button_height)
equal.place(x=92, y=170, width=button_width, height=button_height)
divide.place(x=132, y=170, width=button_width, height=button_height)

root.mainloop()