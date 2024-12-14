import tkinter as tk
import os
from tkinter import PhotoImage as pi

from tkinter import messagebox as mg

os.environ['TCL_LIBRARY'] = 'C:/Users/ADMIN/AppData/Local/Programs/Python/Python313/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'C:/Users/ADMIN/AppData/Local/Programs/Python/Python313/tcl/tcl8.6'

root = tk.Tk()
root.title("Calculator")
root.geometry("345x400")
root.config(bg="Silver")

first_number = None
operator = None

def show_text(text):

    t1.insert(tk.END, text)

def clear_text():

    t1.delete(1.0, tk.END)

def get_everything(op):

    global first_number, operator
    if t1.get(1.0, tk.END).strip():

        first_number = float(t1.get(1.0, tk.END).strip())
        operator = op
        clear_text()

def perform():

    global first_number, operator
    if first_number is not None and operator:

        second_number = float(t1.get(1.0, tk.END).strip())
        if operator == '+':
            result = first_number + second_number

        elif operator == '-':
            result = first_number - second_number

        elif operator == 'x':
            result = first_number * second_number

        elif operator == '/':
            if second_number==0:
                mg.showerror("Error", "Cannot divide by 0")
                root.destroy()

            else:
                result = first_number/second_number

        clear_text()
        show_text(str(result))
        first_number = None
        second_number = None


t1 = tk.Text(root, height=2, width=31, borderwidth=4, bg="lightblue")
t1.pack()
t1.place(x=45, y=70)

l1 = tk.Label(root, text="CALCULATOR", font=20, foreground="Red", borderwidth=3)
l1.place(x=105, y=20)

b1 = tk.Button(root, text="1", width=5, height=2, borderwidth=4, bg="lightblue", command=lambda: show_text("1"))
b1.place(x=60,y=130)

b2 = tk.Button(root, text="2", width=5, height=2, borderwidth=4, bg="lightblue", command=lambda: show_text("2"))
b2.place(x=120,y=130)

b3 = tk.Button(root, text="3", width=5, height=2, borderwidth=4, bg="lightblue", command=lambda: show_text("3"))
b3.place(x=180,y=130)

b4 = tk.Button(root, text="4", width=5, height=2, borderwidth=4, bg="lightblue", command=lambda: show_text("4"))
b4.place(x=60,y=185)

b5 = tk.Button(root, text="5", width=5, height=2, borderwidth=4, bg="lightblue", command=lambda: show_text("5"))
b5.place(x=120,y=185)

b6 = tk.Button(root, text="6", width=5, height=2, borderwidth=4, bg="lightblue", command=lambda: show_text("6"))
b6.place(x=180,y=185)

b7 = tk.Button(root, text="7", width=5, height=2, borderwidth=4, bg="lightblue", command=lambda: show_text("7"))
b7.place(x=60,y=240)

b8 = tk.Button(root, text="8", width=5, height=2, borderwidth=4, bg="lightblue", command=lambda: show_text("8"))
b8.place(x=120,y=240)

b9 = tk.Button(root, text="9", width=5, height=2, borderwidth=4, bg="lightblue", command=lambda: show_text("9"))
b9.place(x=180,y=240)

b10 = tk.Button(root, text="0", width=5, height=2, borderwidth=4, bg="lightblue", command=lambda: show_text("0"))
b10.place(x=120,y=295)

b11 = tk.Button(root, text="+", width=5, height=2, borderwidth=4, bg="lightblue", command=lambda: get_everything('+'))
b11.place(x=240,y=130)

b12 = tk.Button(root, text="-", width=5, height=2, borderwidth=4, bg="lightblue", command=lambda: get_everything('-'))
b12.place(x=240,y=185)

b13 = tk.Button(root, text="x", width=5, height=2, borderwidth=4, bg="lightblue", command=lambda: get_everything('x'))
b13.place(x=240,y=240)

b14 = tk.Button(root, text="/", width=5, height=2, borderwidth=4, bg="lightblue", command=lambda: get_everything('/'))
b14.place(x=240,y=295)

b15 = tk.Button(root, text="=", width=5, height=2, borderwidth=4, bg="Yellow", command=perform)
b15.place(x=180,y=295)

b16 = tk.Button(root, text=".", width=5, height=2, borderwidth=4, bg="lightblue", command=lambda: show_text("."))
b16.place(x=60,y=295)

root.mainloop()