from tkinter import *


# Global variable for our file path
filePath = "DataFile.txt"

def fnOpenDataFile():
    global filePath
    # Open the file for reading
    fileObject = open(filePath, "r")
    
    # Add the file contents to the list box
    # Capture all of the data, and loop through to add each line one at a time.
    dataSet = fileObject.read().splitlines
    for line in dataSet():
        lstValues.insert(END, line)
    
    # Close the file
    fileObject.close()

def cmdSubmit():
    global filePath
    # Open the file for appending
    fileObject = open(filePath, "a")
    
    # Write what's in the entry box to the file
    fileObject.write(entValue.get() + "\n")
    
    # Add the input to the listbox
    lstValues.insert(END, entValue.get())
    
    # Close the file
    fileObject.close()
    
    

# Creating the window
root = Tk()
root.title("Files")
root.geometry("400x150")

# Adding labels
Label(root, text="Input Value:").grid(row=0, column=0, sticky=W)

# Adding entry boxes and output label
entValue = Entry(root)
entValue.grid(row=0, column=1, sticky=W)

# Adding button
Button(root, text="Submit", command=cmdSubmit).grid(row=0, column=2, sticky=W)

# Listbox for values
Label(root, text="Values:").grid(row=1, column=0, sticky=W)
frmValues = Frame(root)
frmValues.grid(row=2, column=0, sticky=W)
scrValues = Scrollbar(frmValues)
scrValues.grid(row=0, column=1, sticky=N+S+W)
lstValues = Listbox(frmValues, height=5, yscrollcommand=scrValues.set)
lstValues.grid(row=0, column=0)
scrValues.config(command=lstValues.yview)

# Call function to open file to display values
fnOpenDataFile()


# Displaying window
root.mainloop()