from tkinter import *
from tkinter import messagebox
import traceback


root = Tk()
root.title("Error Checking")
root.geometry("450x75")

goodValues = list()

def cmdSubmit():
    print("fnSubmit called")
    try:
        value = float(entAmount.get())
        print("Value = " , value, " | ", type(value))
        if 0 <= value <= 100:
            goodValues.append(value)
        elif value == -1:
            print("Values Entered:", goodValues)
        elif value < -1 or value > 100:
            print("Value must be between 0 and 100. Please try again")
            messagebox.showerror("Invalid Value", "Value must be between 0 and 100. Please try again")
            
    except:
        traceback.print_exc()    # Outputs to the terminal the last error message from the interpreter (Python) 
        print("A numeric value must be between 0 and 100. Please try again.")
        messagebox.showwarning("Not a Numeric Value", "A numeric value must be between 0 and 100. Please try again.") 


Label(root, text="Please enter a value between 0 and 100 (enter -1 to end) :").grid(row=0, column=0, sticky=W)
entAmount = Entry(root, width=10)
entAmount.grid(row=0, column=1, sticky=W)
Button(root, text="Submit", command=cmdSubmit).grid(row=2, column=2, sticky=W)

root.mainloop()

