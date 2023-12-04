from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
import traceback
import sqlite3
import pathlib


dbFile = pathlib.Path("C:\\Users\\user//Desktop\\MGIS 350 Project 2\\Project 2 Database - Template.sqlite3")  # Change path as needed

if dbFile.exists():
    conn = sqlite3.connect(dbFile)
    cur = conn.cursor()
else:
    messagebox.showerror("Database", "Database file not found.")
    quit()

def fnPopulateComboboxPastOrder():
    sql = "SELECT orderNumber FROM orders"

    cur.execute(sql)
    records = cur.fetchall()    
    
    

root = Tk()
root.title("Project 2")
root.geometry("1000x500")

################################################################################

Label(root, text="INVENTORY").grid(row=0, column=0, sticky=W)
Label(root, text="Vanilla:").grid(row=1, column=0, sticky=W)
Label(root, text="Chocolate:").grid(row=2, column=0, sticky=W)
Label(root, text="Sprinkles:").grid(row=3, column=0, sticky=W)
Label(root, text="Whipped Cream:").grid(row=4, column=0, sticky=W)
Label(root, text="Hot Fudge:").grid(row=5, column=0, sticky=W)

lblVanInv = Label(root, text = "0")
lblVanInv.grid(row = 1, column = 1, sticky = W)
lblChocInv = Label(root, text = "0")
lblChocInv.grid(row = 2, column = 1, sticky = W)
lblSprinInv = Label(root, text = "0")
lblSprinInv.grid(row = 3, column = 1, sticky = W)
lblWhipInv = Label(root, text = "0")
lblWhipInv.grid(row = 4, column = 1, sticky = W)
lblFudgInv = Label(root, text = "0")
lblFudgInv.grid(row = 5, column = 1, sticky = W)

Label(root, text="ADD TO INVENTORY").grid(row=0, column=2, sticky=W)

vanVar = IntVar()
chkVan = Checkbutton(root, text="Add 256.0 oz of Vanilla:", variable = vanVar).grid(row=1, column=2, sticky=W)
chocVar = IntVar()
chkChoc = Checkbutton(root, text="Add 256.0 oz of Chocolate:", variable = chocVar).grid(row=2, column=2, sticky=W)
sprinVar = IntVar()
chkSprin = Checkbutton(root, text="Add 64.0 oz of Sprinkles:", variable = sprinVar).grid(row=3, column=2, sticky=W)
whipVar = IntVar()
chkWhip = Checkbutton(root, text="Add 64.0 oz of Whipped Cream:", variable = whipVar).grid(row=4, column=2, sticky=W)
fudgVar = IntVar()
chkFudg = Checkbutton(root, text="Add 48.0 oz of Hot Fudge:", variable = fudgVar).grid(row=5, column=2, sticky=W)

Button(root, text = "Add to Inventory").grid(row=6, column=2, sticky=W)


Label(root, text="ORDER FORM").grid(row=0, column=3, sticky=W)
Label(root, text = "Scoops").grid(row=1, column=3, sticky=W)
entValue = Entry(root, width=5)
entValue.grid(row=1, column=3, sticky=W, padx=60)
rdoSelected = IntVar()
rdoVan = Radiobutton(root, text="Vanilla", variable = rdoSelected, value=0).grid(row=2, column=3, sticky=W)
rdoChoc = Radiobutton(root, text="Chocolate", variable = rdoSelected, value=1).grid(row=2, column=3, sticky=E, padx=60)
sprinVar1 = IntVar()
chkSprin1 = Checkbutton(root, text = "Sprinkles", variable = sprinVar1).grid(row=3, column=3, sticky=W)
whipVar1 = IntVar()
chkWhip1 = Checkbutton(root, text = "Whipped Cream", variable = whipVar1).grid(row=4, column=3, sticky=W)
fudgVar1 = IntVar()
chkFudg1 = Checkbutton(root, text = "Hot Fudge", variable = fudgVar1).grid(row=5, column=3, sticky=W)
Button(root, text="Add to Order").grid(row=6, column=3, sticky=W)


Label(root, text="FINANCIAL DATA").grid(row=0, column=4, sticky=W)
Label(root, text = "Sales:").grid(row=1, column=4, sticky=W)
Label(root, text = "Expenses:").grid(row=2, column=4, sticky=W)
Label(root, text = "Profit:").grid(row=3, column=4, sticky=W)

lblSales = Label(root, text = "$0.00")
lblSales.grid(row=1, column=4, sticky=W, padx=100)
lblExpenses = Label(root, text = "$0.00")
lblExpenses.grid(row=2, column=4, sticky=W, padx=100)
lblProfit = Label(root, text = "$0.00")
lblProfit.grid(row=3, column=4, sticky=W, padx=100)

#new
lblPastOrders = Label(root, text = "PAST ORDERS")
lblPastOrders.grid(row=13, column=0, sticky=W)
frmPastOrders = Frame(root)
frmPastOrders.grid(row=14, column=0, sticky=W)
srcPastOrders = Scrollbar(frmPastOrders)
srcPastOrders.grid(row=14, column=1, sticky=W)
lstPastOrders = Listbox(frmPastOrders,height = 5, yscrollcommand=srcPastOrders.set)
lstPastOrders.grid(row=14, column=0, sticky=W)
srcPastOrders.config(command=lstPastOrders.yview)
Button(root, text = "Show Order Details").grid(row=15, column=0, sticky=W)


lblLineItems = Label(root, text = "Line Items")
lblLineItems.grid(row=11, column=3, sticky=W)
frmLineItems = Frame(root)
frmLineItems.grid(row=12, column=3, sticky=W)
srcLineItems = Scrollbar(frmLineItems)
srcLineItems.grid(row=12, column=4, sticky=W)
lstLineItems = Listbox(frmLineItems,height = 5, yscrollcommand=srcPastOrders.set)
lstLineItems.grid(row=12, column=3, sticky=W)
srcLineItems.config(command=lstLineItems.yview)
Button(root, text = 'Place Order').grid(row=13, column=3, sticky=W)
Button(root, text = 'Cancel Order').grid(row=13, column=3, sticky=W, padx=72)


lblPastOrderDetails = Label(root, text= "Past Order Details")
lblPastOrderDetails.grid(row=11, column=11, sticky=W)
frmPastOrderDetails = Frame(root)
frmPastOrderDetails.grid(row=12, column=11, sticky=W)




################################################################################

root.mainloop()

