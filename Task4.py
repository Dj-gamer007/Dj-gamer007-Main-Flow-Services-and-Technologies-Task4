from tkinter import *
from PIL import ImageTk, Image

def init_calculator():
    rt = Tk()
    rt.title("Calculator")
    rt.iconbitmap("C:\\Users\\jayaraman\\Main Flow Services And Technology Internship\\Calculator Photo\\Calc-icon.ico")
    rt.geometry("300x430")

    bg = ImageTk.PhotoImage(file="C:\\Users\\jayaraman\\Main Flow Services And Technology Internship\\Calculator Photo\\300x430_background.png")
    bg_label = Label(rt, image=bg)
    bg_label.place(x=0, y=0)

    e = Entry(rt, width=35, borderwidth=10, font=("Times", 10))
    e.grid(row=0, column=0, pady=20, padx=30, columnspan=3)

    image = {
        "1": ImageTk.PhotoImage(file="C:\\Users\\jayaraman\\Main Flow Services And Technology Internship\\Calculator Photo\\1.png"),
        "2": ImageTk.PhotoImage(file="C:\\Users\\jayaraman\\Main Flow Services And Technology Internship\\Calculator Photo\\2.png"),
        "3": ImageTk.PhotoImage(file="C:\\Users\\jayaraman\\Main Flow Services And Technology Internship\\Calculator Photo\\3.png"),
        "4": ImageTk.PhotoImage(file="C:\\Users\\jayaraman\\Main Flow Services And Technology Internship\\Calculator Photo\\4.png"),
        "5": ImageTk.PhotoImage(file="C:\\Users\\jayaraman\\Main Flow Services And Technology Internship\\Calculator Photo\\5.png"),
        "6": ImageTk.PhotoImage(file="C:\\Users\\jayaraman\\Main Flow Services And Technology Internship\\Calculator Photo\\6.png"),
        "7": ImageTk.PhotoImage(file="C:\\Users\\jayaraman\\Main Flow Services And Technology Internship\\Calculator Photo\\7.png"),
        "8": ImageTk.PhotoImage(file="C:\\Users\\jayaraman\\Main Flow Services And Technology Internship\\Calculator Photo\\8.png"),
        "9": ImageTk.PhotoImage(file="C:\\Users\\jayaraman\\Main Flow Services And Technology Internship\\Calculator Photo\\9.png"),
        "0": ImageTk.PhotoImage(file="C:\\Users\\jayaraman\\Main Flow Services And Technology Internship\\Calculator Photo\\10.png"),
        "+": ImageTk.PhotoImage(file="C:\\Users\\jayaraman\\Main Flow Services And Technology Internship\\Calculator Photo\\11.png"),
        "-": ImageTk.PhotoImage(file="C:\\Users\\jayaraman\\Main Flow Services And Technology Internship\\Calculator Photo\\12.png"),
        "*": ImageTk.PhotoImage(file="C:\\Users\\jayaraman\\Main Flow Services And Technology Internship\\Calculator Photo\\13.png"),
        "/": ImageTk.PhotoImage(file="C:\\Users\\jayaraman\\Main Flow Services And Technology Internship\\Calculator Photo\\14.png"),
        "=": ImageTk.PhotoImage(file="C:\\Users\\jayaraman\\Main Flow Services And Technology Internship\\Calculator Photo\\15.png"),
        "C": ImageTk.PhotoImage(file="C:\\Users\\jayaraman\\Main Flow Services And Technology Internship\\Calculator Photo\\16.png")
    }

    def button_click(number):
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

    def button_add():
        first_number = e.get()
        global f_num
        global maths
        maths = "addition"
        f_num = int(first_number)
        e.delete(0, END)

    def button_sub():
        first_number = e.get()
        global f_num
        global maths
        maths = "subtraction"
        f_num = int(first_number)
        e.delete(0, END)

    def button_mul():
        first_number = e.get()
        global f_num
        global maths
        maths = "multiplication"
        f_num = int(first_number)
        e.delete(0, END)

    def button_div():
        first_number = e.get()
        global f_num
        global maths
        maths = "division"
        f_num = int(first_number)
        e.delete(0, END)

    def button_equals():
        second_number = e.get()
        e.delete(0, END)

        if maths == "addition":
            e.insert(0, f_num + int(second_number))
        if maths == "subtraction":
            e.insert(0, f_num - int(second_number))
        if maths == "multiplication":
            e.insert(0, f_num * int(second_number))
        if maths == "division":
            e.insert(0, f_num / int(second_number))

    def button_clear():
        e.delete(0, END)

    buttons = {
        "1": (1, 0, lambda: button_click(1)),
        "2": (1, 1, lambda: button_click(2)),
        "3": (1, 2, lambda: button_click(3)),
        "4": (2, 0, lambda: button_click(4)),
        "5": (2, 1, lambda: button_click(5)),
        "6": (2, 2, lambda: button_click(6)),
        "7": (3, 0, lambda: button_click(7)),
        "8": (3, 1, lambda: button_click(8)),
        "9": (3, 2, lambda: button_click(9)),
        "0": (4, 1, lambda: button_click(0)),
        "+": (4, 2, button_add),
        "-": (4, 0, button_sub),
        "*": (5, 1, button_mul),
        "/": (5, 0, button_div),
        "=": (5, 2, button_equals),
        "C": (6, 1, button_clear)
    }

    for (row, col, cmd) in buttons.values():
        Button(rt, border="3", image=image[list(buttons.keys())[list(buttons.values()).index((row, col, cmd))]], command=cmd).grid(row=row, column=col)

    rt.images = image  
    rt.mainloop()

init_calculator()