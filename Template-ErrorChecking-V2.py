from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox # Adds the message box library for error messages
import traceback  # Adds the library for some additional debugging tools

root = Tk()
root.title("Account Tracking")
root.geometry("450x200")

# Define collections for the accounts
checking = list()
savings = list()
answer = True

def cmdSubmit():
    print("fnSubmit called")
    global answer
    try:
        # Read in the input amount
        value = float(entAmount.get())

        # Create the answer variable with a default of True
        #answer = True


        # Check to see if the value is <=0
        if value <= 0:
            answer = messagebox.askyesno("Proceed?", "You have entered a value zero or less. Do you want to proceed?")
            print("DEBUGGING answer variable:", answer)    
            
            # Determine if we need to proceed
            if answer:
                print("Proceed")
            else:
                print("Do nothing")
            
        #else:  
        if answer:  
            # Negate value of withdraw
            value = value * transactionType.get()
            
            # Insert value into collection based on which account is selected
            if cboAccounts.get() == "Checking":
                checking.append(value)
            elif cboAccounts.get() == "Savings":
                savings.append(value)
            else:
                # Show an error to the user to select a valid account
                messagebox.showwarning("Account Error", "Please select a valid account.")
    except:
        traceback.print_exc()    # Outputs to the terminal the last error message from the interpreter (Python)  
        messagebox.showerror("Input Error", "Please enter a valid number for the amount.")
        print("Please enter a valid number for the amount.") 
    
    # Update Output
    fnDisplayTransactionsAndBalance()

def cmdRemove():
    print("fnRemove called")
    # *** INSERT CODE HERE ***
    
    # Update Output
    fnDisplayTransactionsAndBalance()


def fnDisplayTransactionsAndBalance(event=None):
    print("fnDisplayTransactionsAndBalance called")
    balance = 0

    # Clear listbox
    lstTransactions.delete(0,END)

    # Loop through values to display in listbox and calculate balance
    if cboAccounts.get() == "Checking":
        for i in checking:
            lstTransactions.insert(END, i)
            balance = balance + i
    if cboAccounts.get() == "Savings":
        for i in savings:
            lstTransactions.insert(END, i)
            balance = balance + i
    
    # Displaying the balance
    lblBalance.config(text='${:9,.2f}'.format(balance))


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

# Setting up combobox
cboAccounts = Combobox(root, values=("Checking", "Savings"))
cboAccounts.grid(row=1, column=1, sticky=W)
cboAccounts.bind("<<ComboboxSelected>>", fnDisplayTransactionsAndBalance)

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