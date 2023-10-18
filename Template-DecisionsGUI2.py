from tkinter import *

subtotal = 0
discount = 0
tax = 0
total = 0

# Create a function for our update button
def cmdUpdate():
    global subtotal, discount, tax, total
    
    # Read in the subtotal
    subtotal = float(entValue.get())
    
    # Determine if tax is checked
    if varTax.get() == 1:
        tax = subtotal * 0.08
        
    # Determine if discount is checked
    if varDiscount.get() == 1:
        discount = subtotal * 0.1

    # Calculate the total
    total = subtotal - discount + tax
    
    # Output
    lblTax.config(text=tax)
    lblDiscount.config(text=discount)
    lblTotal.config(text=total)

root = Tk()
root.title("Decisions GUI 2")
root.geometry("400x200")

Label(root, text="Input Value:").grid(row=0, column=0, sticky=W)
entValue = Entry(root)
entValue.grid(row=0, column=1, sticky=W)
Button(root, text="Update", command=cmdUpdate).grid(row=0, column=2, sticky=W)

# Create the variable for the tax checkbox
varTax = IntVar()
chkTax = Checkbutton(root, text="Apply Tax", variable=varTax)
chkTax.grid(row=1, column=0, sticky=W)

# Create the variable for the discount checkbox
varDiscount = IntVar()
chkDiscount = Checkbutton(root, text="Apply Discount", variable=varDiscount)
chkDiscount.grid(row=1, column=1, sticky=W)

Label(root, text="Discount:").grid(row=3, column=0, sticky=W)
lblDiscount = Label(root, text="0")
lblDiscount.grid(row=3, column=1, sticky=W)

Label(root, text="Tax:").grid(row=4, column=0, sticky=W)
lblTax = Label(root, text="0")
lblTax.grid(row=4, column=1, sticky=W)

Label(root, text="Total:").grid(row=5, column=0, sticky=W)
lblTotal = Label(root, text="0")
lblTotal.grid(row=5, column=1, sticky=W)

root.mainloop()
