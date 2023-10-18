from tkinter import *

runningTotal = 0

# Create a function to read in the values and add them together
def cmdAddValues():
    # Read in the values from the user
    value1 = float(entValue1.get())
    value2 = float(entValue2.get())
    # Add the values together
    solution = value1 + value2
    # Display the solution
    lblSolution.config(text=solution)


def cmdRunningTotal():
    global runningTotal  #need to bring in global variable so you can use it in the function
    # Read in the first value from the user
    value1 = float(entValue1.get())
    
    # Establish Running Total variable
    #runningTotal = 0 You need to set this as a global variable
    
    # Add the input to our running total
    runningTotal = runningTotal + value1
    
    # Output the solution
    lblSolution.config(text=runningTotal)

# Creating the window
root = Tk()
root.title("Functions")
root.geometry("300x150")

# Adding labels
lblValue1Text = Label(root, text="Value 1:")
lblValue1Text.grid(row=0, column=0, sticky=W)
lblValue2Text = Label(root, text="Value 2:")
lblValue2Text.grid(row=1, column=0, sticky=W)
lblSolutionText = Label(root, text="Solution:")
lblSolutionText.grid(row=2, column=0, sticky=W)

# Adding entry boxes and output label
entValue1 = Entry(root)
entValue1.grid(row=0, column=1, sticky=W, columnspan=2)
entValue2 = Entry(root)
entValue2.grid(row=1, column=1, sticky=W, columnspan=2)
lblSolution = Label(root, text="Not Set")
lblSolution.grid(row=2, column=1, sticky=W)
lblDummy = Label(root, text="Hi")
lblDummy.grid(row=2, column=2)

# Adding button
btnAddValues = Button(root, text="Add Values", command=cmdAddValues)
btnAddValues.grid(row=3, column=0, sticky=W)

# Add Running Total Button
Button(root, text="Add to Running Total", command=cmdRunningTotal).grid(column=0, row=4, sticky=W)

# Displaying window
root.mainloop()