# Load the graphics library, tkinter
from tkinter import *
import random


# Create a function for the Click Here button
def cmdClickHere():
    print("cmdClickHere was called...") 
    # Display our message in the label
    lblOutput.config(text="Hello")

def cmdEnter(event):
    btnClickHere.place(x = random.randint(0,380), y = random.randint(0,180))

# Create our window and call it root
root = Tk()

# Set the size of our window
root.geometry("400x200")

# Set the title of our window
root.title("My 1st GUI")
#root['bg'] = "white"  to change the background color

# Create our click here button
btnClickHere = Button(root, text="Click Here", command=cmdClickHere) #No () on function call with command
btnClickHere.grid(row=0, column=0)
btnClickHere.bind("<Enter>", cmdEnter)

# Create our output label
lblOutput = Label(root, text="N/A")
lblOutput.grid(column=1, row=0)

# Display the window
root.mainloop()
