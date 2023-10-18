from tkinter import *


# Create a function to read in the values and add them together
def cmdAddValues():
    # Read in the values from the user
    value1 = float(entValue1.get())
    value2 = float(entValue2.get())
    # Add the values together
    solution = value1 + value2
    # Display the solution
    lblSolution.config(text=solution)
    
def cmdSubtractValues():
    # Read in the values from the user
    value1 = float(entValue1.get())
    value2 = float(entValue2.get())
    # Subtract the values together
    solution = value1 - value2
    # Display the solution
    lblSolution.config(text=solution)

def cmdMultiplyValues():
    # Read in the values from the user
    value1 = float(entValue1.get())
    value2 = float(entValue2.get())
    # Multiply the values together
    solution = value1 * value2
    # Display the solution
    lblSolution.config(text=solution)
    
def DivideValues():
    # Read in the values from the user
    value1 = float(entValue1.get())
    value2 = float(entValue2.get())
    # Divide the values together
    solution = value1 / value2
    # Display the solution
    lblSolution.config(text=solution)

# Creating the window
root = Tk()
root.title("Functions")
root.geometry("350x150")

# Adding labels
lblValue1Text = Label(root, text="Value 1:")
lblValue1Text.grid(row=0, column=0, sticky=W)
lblValue2Text = Label(root, text="Value 2:")
lblValue2Text.grid(row=1, column=0, sticky=W)
lblSolutionText = Label(root, text="Solution:")
lblSolutionText.grid(row=3, column=0, sticky=W)

# Adding entry boxes and output label
entValue1 = Entry(root)
entValue1.grid(row=0, column=1, sticky=W, columnspan=2)
entValue2 = Entry(root)
entValue2.grid(row=1, column=1, sticky=W, columnspan=2)
lblSolution = Label(root, text="Not Set")
lblSolution.grid(row=3, column=1, sticky=W)

# Adding button
btnAddValues = Button(root, text="Add Values", command=cmdAddValues)
btnAddValues.grid(row=2, column=0, sticky=W)
btnSubtractValues = Button(root, text="Subtract Values", command=cmdSubtractValues)
btnSubtractValues.grid(row=2, column=1, sticky=W)
btnMultiplyValues = Button(root, text="Multiply Values", command=cmdMultiplyValues)
btnMultiplyValues.grid(row=2, column=2, sticky=W)
btnDivideValues = Button(root, text="Divide Values", command=DivideValues)
btnDivideValues.grid(row=2, column=3, sticky=W)

# Displaying window
root.mainloop()