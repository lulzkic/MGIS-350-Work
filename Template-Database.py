from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import traceback
import sqlite3   # Library for using the database
import pathlib  # Library for working with the file system

# A global variable for ids
global ids


# Test to ensure the database exists
dbFile = pathlib.Path("C:\\Users\\user\\Documents\\MGIS 350 Work\\Template-Database.sqlite3")

# Test to make sure the database file exists
if dbFile.exists():
    # File was found. Create the connection and cursor
    conn = sqlite3.connect(dbFile)
    cur = conn.cursor()
else:
    messagebox.showerror("Database", "Database not found.")
    quit()   # Close the program

def fnPopulateCombobox():
    # This function will use the database to update the list in the combobox
    sql = "SELECT DISTINCT account FROM transactions ORDER BY account ASC;"
# Execute the query\
    cur.execute(sql)
    # Grab the results
    records = cur.fetchall()
    # Print the records for debugging
    print("fnPopulateCombobox records:", records)
    # Take the return list adn sue it to update the values property of the combobox
    cboAccounts.config(values=records)

def cmdSubmit():
    print("cmdSubmit called")
    
    try:
        # Read in the input amount
        value = float(entAmount.get())

        # Negate Withdrawal
        value = value * transactionType.get()

        # *** INSERT CODE HERE ***
        sql = "INSERT INTO transactions (account, amount) VALUES (?, ?);"
        sql_arg = [cboAccounts.get(), value]
        
        # Execute query
        cur.execute(sql, sql_arg)
        
        # Write the changes to the database
        conn.commit()
    except ValueError as ve:
        traceback.print_exc()
        messagebox.showerror("Error", "Please enter a number for the amount")
    except sqlite3.OperationalError as oe:
        traceback.print_exc()
        messagebox.showerror("Error", "Something went wrong with the database.")
    except:
        traceback.print_exc()
        messagebox.showerror("Error", "An unknown error has occurred.")

    # Update Output
    fnDisplayTransactionsAndBalance()

def cmdRemove():
    print("cmdRemove called")
    # *** INSERT CODE HERE ***
 
    # Update Output
    fnDisplayTransactionsAndBalance()
    fnPopulateCombobox()


def fnDisplayTransactionsAndBalance(event=None):
    print("fnDisplayTransactionsAndBalance called")
    
    # Bring in the glovbal list of ids
    global ids
    
    
    balance = 0

    # Clear the listbox
    lstTransactions.delete(0, END)
    # Clear the ids
    ids.clear()
    
    # *** INSERT CODE HERE ***
    #sql = "SELECT amount FROM transactions WHERE account = '" + cboAccounts.get() + "';"
    sql = "SELECT amount FROM transactions WHERE account = ?;"
    sql_args = [cboAccounts.get()]
    # Execute the query
    cur.execute(sql, sql_args)
    # Grab the records
    records = cur.fetchall()
    # Loop through the records
    for record in records:
        lstTransactions.insert(END, record[0])
        balance = balance + record[0]
    # add the id to list of ids
    ids.append(record[1])
    
    # Displaying the balance
    lblBalance.config(text='${:9,.2f}'.format(balance))


# Setting up window
root = Tk()
root.title("Account Tracking")
root.geometry("450x200")

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

# Setting up the combobox
cboAccounts = ttk.Combobox(root)
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
srcTransactions.pack(side=RIGHT, fill=Y)
lstTransactions = Listbox(frmTransactions, height=5, yscrollcommand=srcTransactions.set)
lstTransactions.pack()
srcTransactions.config(command=lstTransactions.yview)

# Before opening the window (which was established in the lines above), update the combobox
fnPopulateCombobox()

# Running main program loop
root.mainloop()

