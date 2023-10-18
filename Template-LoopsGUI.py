from tkinter import *
root = Tk()
root.title("Checking Account")
root.geometry("450x200")


def cmdSubmit():
    print("cmdSubmit Called")
    amount = float(entAmount.get())
    amount = amount * transactionType.get()
    # Insert value into output list
    lstTransactions.insert(END, amount)
    # Display balance
    fnGetBalance()


def cmdRemove():
    print("cmdRemove Called")
    # Remove a selected value
    lstTransactions.delete(lstTransactions.curselection())  # curselection() = current selection
    # Display balance
    fnGetBalance()
    
    
def fnGetBalance():
    print("fnGetBalance Called")
    balance = 0
    # Loop through list of values
    for i, value in enumerate(lstTransactions.get(0, END)):
        balance = balance + value
        
    # Display the balance
    lblBalance.config(text=balance)
    
    #return balance not going to use


Label(root, text="Amount:").grid(row=0, column=0, sticky=W)
Label(root, text="Balance:").grid(row=3, column=0, sticky=W)
lblBalance = Label(root, text="$0.00")
lblBalance.grid(row=3, column=1, sticky=W)

entAmount = Entry(root)
entAmount.grid(row=0, column=1)

Button(root, text="Submit", command=cmdSubmit).grid(row=1, column=1, sticky=E)
Button(root, text="Remove", command=cmdRemove).grid(row=2, column=1, sticky=E)

transactionType = IntVar()
rdoDeposit = Radiobutton(root, text="Deposit", variable=transactionType, value=1)
rdoDeposit.grid(row=1, column=0, sticky=W)
rdoDeposit.select()
rdoWithdrawal = Radiobutton(root, text="Withdrawal", variable=transactionType, value=-1)
rdoWithdrawal.grid(row=2, column=0, sticky=W)

Label(root, text="Transactions:").grid(row=0, column=3, sticky=W)

# Insert transactions listbox in Row 1, Column 3, spaning 4 rows.
frmTransactions = Frame(root)
frmTransactions.grid(row=1, column=3, rowspan=4, sticky=W)
# Creating Scrollbar
scrTransactions = Scrollbar(frmTransactions)
scrTransactions.grid(row=0, column=1, sticky=N+S+W)
# Creating Listbox
lstTransactions = Listbox(frmTransactions, height=5, yscrollcommand=scrTransactions.set)
lstTransactions.grid(row=0,column=0, sticky=W)
# Adding the listbox to the scrollbar's command
scrTransactions.config(command=lstTransactions.yview)

root.mainloop()
