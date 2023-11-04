from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Collections Homework")
root.geometry("450x200")

# collections 
positive = []
negative = []

def enter():
    value = float(entAmount.get())
    if value == 0:
        print("Positive values:", positive)
        print("Negative values:", negative)
        lblPositive.config(text="Positive values: " + str(positive))
        lblNegative.config(text="Negative values: " + str(negative))
    elif value > 0:
        positive.append(value)
    else:
        negative.append(value)
    entAmount.delete(0, END)

Label(root, text="Please enter a positive or negative number (enter a zero to end):").grid(row=0, column=0, sticky=W)
entAmount = Entry(root, width=10)
entAmount.grid(row=0, column=1, sticky=W)
Button(root, text="Enter", command=enter).grid(row=1, column=1, sticky=W)

lblPositive = Label(root, text="Positive values:")
lblPositive.grid(row=2, column=0, sticky=W)
lblNegative = Label(root, text="Negative values:")
lblNegative.grid(row=3, column=0, sticky=W)


root.mainloop()