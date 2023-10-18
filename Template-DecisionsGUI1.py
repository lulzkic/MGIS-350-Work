from tkinter import *

# Global Running Total Variable
runningTotal = 0

# Function for the Submit Button
def cmdSubmit():
    global runningTotal
    # Read in my value
    value = float(entValue.get())

    # Test is add was selected
    if rdoSelected.get() == 0:
        runningTotal = runningTotal + value
    else:
        runningTotal = runningTotal - value
        
    # Output the solution
    lblTotal.config(text=runningTotal)
        
root = Tk()
root.title("Decisions GUI - 1")
root.geometry("400x200")

Label(root, text="Input Value").grid(row=0, column=0, sticky=W)
entValue = Entry(root)
entValue.grid(row=0, column=1, sticky=W)
Button(root, text="Submit", command=cmdSubmit).grid(row=0, column=2, sticky=W)

# Create a variable for the radio buttons
rdoSelected = IntVar()


# Insert code for our radio buttons for add and subtract
rdoAdd = Radiobutton(root, text="Add", variable=rdoSelected, value=0)
rdoAdd.grid(row=1, column=0, sticky=W)
rdoSubtract = Radiobutton(root, text="Subtract", variable=rdoSelected, value=1)
rdoSubtract.grid(row=2, column=0, sticky=W)

Label(root, text="Running Total:").grid(row=3, column=0, sticky=W)
lblTotal = Label(root, text="0")
lblTotal.grid(row=3, column=1, sticky=W)

root.mainloop()