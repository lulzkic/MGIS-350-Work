from tkinter import *
from tkinter import ttk
import traceback
from tkinter import messagebox

# Set the location of the data file
filePath = "AccountData.csv"

# Variable to detecting changes
changesMade = False

root = Tk()
root.title("Account Tracking")
root.geometry("450x200")

# Define lists for data
accountData = list()
ids = list()

# Function to read in the data and populate the accountData variable
def fnOpenDataFile():
    global filePath, accountData
    # Create a variable for the list of account names
    accountNames = set()
    # Read in data
    fileObject = open(filePath, "r")
    dataSet = fileObject.read().splitlines()
    # Loop through the dataSet
    for line in dataSet:
        # Create a temporary variable and set it to the line variable
        # split by commas
        tmp = line.split(",")
        # DEBUGGING
        print("tmp:", tmp)
        # Add the data to the list
        accountData.append({'amount': float(tmp[0]), 'account': tmp[1]})
        # Add the account name to the set
        accountNames.add(tmp[1]) # Results in unique account names in the set

    # Add the set of unique accout names, sorted, to the combobox
    accountNames = list(accountNames)
    accountNames.sort()
    cboAccounts.config(values=accountNames)

    # DEBUGGING
    print("dataSet:", dataSet)
    print("accountData:", accountData)

def cmdSave():
    global filePath, accountData, changesMade
    # Overwrite the file with what is in memory
    fileObject = open(filePath, "w")
    # Loop through each accountData entry and add them one at a time to the file
    for record in accountData:
        fileObject.write(str(record['amount']) + "," + record['account'] + "\n")
    # Close the file
    fileObject.close()
    # Reset the changes made variable
    changesMade = False

def closing():
    # Where changes made
    if changesMade == True:
        if messagebox.askyesno("Save Changes", "Do you want to save changes?"):
            # Yes, save the changes
            cmdSave()
        else:
            # No, do not save changes.
            pass
    # Manually kill the window
    root.destroy()
    

def cmdSubmit():
    global changesMade
    print("fnSubmit called")
    # Read in the input amount
    try:
        value = (float(entAmount.get())) * transactionType.get()
    
        # Create dictionary for the entry
        accountData.append({'amount': value, 'account': cboAccounts.get()})
        changesMade = True

        # Updating combobox
        currentValues = cboAccounts["values"]
        if cboAccounts.get() not in currentValues:
            newValues = list(currentValues)
            newValues.append(cboAccounts.get())
            cboAccounts["values"] = sorted(newValues)
    except:
        messagebox.showerror("ERROR", "Amount must be a proper number.")

    # Update Output
    fnDisplayTransactionsAndBalance()

def cmdRemove():
    global changesMade
    print("fnRemove called")

    # Deleting from list based on selected value using ids to determine the index
    del accountData[ids[lstTransactions.curselection()[0]]]
    changesMade = True

    # Update Output
    fnDisplayTransactionsAndBalance()

def fnDisplayTransactionsAndBalance(event = None):
    print("fnDisplayTransactionsAndBalance called")
    balance = 0

    # Clear listbox & ids
    lstTransactions.delete(0,END)
    ids.clear()
    # Loop through the list to get the values and balance
    i = 0
    for record in accountData:
        if record['account'] == cboAccounts.get():
            balance += record['amount']
            lstTransactions.insert(END, record['amount'])
            ids.append(i)
        # Incrememnt i
        i = i + 1
    
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

# Combobox Set Up
cboAccounts = ttk.Combobox(root)#, values=("Checking", "Savings"))
cboAccounts.grid(row=1, column=1, sticky=W)
cboAccounts.bind("<<ComboboxSelected>>", fnDisplayTransactionsAndBalance)

# Setting up balance controls
Label(root, text="Balance:").grid(row=4, column=0, sticky=W)
lblBalance = Label(root, text="$0.00")
lblBalance.grid(row=4, column=1, sticky=W)

# Setting up remove controls
Button(root, text="Remove", command=cmdRemove).grid(row=3, column=2, sticky=W)
Button(root, text="Save", command=cmdSave).grid(row=4, column=2, sticky=W)

# Setting up display of transaction controls
Label(root, text="Transactions:").grid(row=0, column=3, sticky=W)
frmTransactions = Frame(root)
frmTransactions.grid(row=1, rowspan=4, column=3, sticky=W)
srcTransactions = Scrollbar(frmTransactions)
srcTransactions.grid(row=0, column=1, sticky=N+S+W)
lstTransactions = Listbox(frmTransactions, height=5, yscrollcommand=srcTransactions.set)
lstTransactions.grid(row=0, column=0)
srcTransactions.config(command=lstTransactions.yview)

# Open our data file
fnOpenDataFile()

# Add code to watch for the close event
root.protocol("WM_DELETE_WINDOW", closing)

# Running main program loop
root.mainloop()