from tkinter import *
from tkinter import ttk  # Additional libraries for the Combobox

root = Tk()
root.title("Account Tracking")
root.geometry("450x200")

# Define collections for the accounts
# *** INSERT CODE HERE ***
checking = []             #two different ways to create an empty list 
savings = list()

def cmdSubmit():
    print("fnSubmit called")
    # Read in the input amount
    value = (float(entAmount.get())) * transactionType.get()
    print("Value = " , value, " | ", type(value))
    # Insert value into collection based on which account is selected

    # *** INSERT CODE HERE ***
    # Output what the user selected
    print("Account Selected:", cboAccounts.get())
    
    # Test to determine which account was selected
    if cboAccounts.get() == "Checking":
        checking.append(value)
    elif cboAccounts.get() == "Savings":
        savings.append(value)
    
    # Update Output
    fnDisplayTransactionsAndBalance()

def cmdRemove():
    print("fnRemove called")
    # *** INSERT CODE HERE ***
    
    # Update Output
    fnDisplayTransactionsAndBalance()


def fnDisplayTransactionsAndBalance():
    print("fnDisplayTransactionsAndBalance called")
    balance = 0

    # *** INSERT CODE HERE ***
    if cboAccounts.get() == "Checking":
        # loop through the checking values and add them one at a time to the listbox
        for row in checking:  #for variable name in list    
            lstTransactions.insert(END, row)
    
    
    # Displaying the balance
    lblBalance.config(text='${:9,.2f}'.format(balance))    # makes text look like us currency


# Setting up input controls
Label(root, text="Amount:").grid(row=0, column=0, sticky=W)
entAmount = Entry(root, width=10)
entAmount.grid(row=0, column=1, sticky=W)
Button(root, text="Submit", command=cmdSubmit).grid(row=2, column=2, sticky=W)
Label(root, text="Account:").grid(row=1, column=0, sticky=W)

transactionType = IntVar()
rd1 = Radiobutton(root, text="Deposit", variable=transactionType, value=1)
rd1.grid(row=2, column=0, sticky=W)
rd1.select()
rd2 = Radiobutton(root, text="Withdrawal", variable=transactionType, value=-1)
rd2.grid(row=3, column=0, sticky=W)

# *** INSERT CODE HERE FOR COMBOBOX ***
cboAccounts = ttk.Combobox(root, values = ["Checking", "Savings"])    #provides list of text to combobox
cboAccounts.grid(row=1, column=1, sticky=W)


# Setting up balance controls
Label(root, text="Balance:").grid(row=4, column=0, sticky=W)
lblBalance = Label(root, text="$0.00")
lblBalance.grid(row=4, column=1, sticky=W)

# Setting up remove controls
Button(root, text="Remove", command=cmdRemove).grid(row=3, column=2, sticky=W)

# Setting up display of transaction controls
Label(root, text="Transactions:").grid(row=0, column=3, sticky=W)
frmTransactions = Frame(root)
frmTransactions.grid(row=1, rowspan=4, column=3, sticky=W)
srcTransactions = Scrollbar(frmTransactions)
srcTransactions.grid(row=0, column=1, sticky=N+S+W)
lstTransactions = Listbox(frmTransactions, height=5, yscrollcommand=srcTransactions.set)
lstTransactions.grid(row=0, column=0)
srcTransactions.config(command=lstTransactions.yview)

# Running main program loop
root.mainloop()