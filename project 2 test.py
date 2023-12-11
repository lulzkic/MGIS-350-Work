from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import traceback
import sqlite3
import pathlib


dbFile = pathlib.Path("C:\\Users\\user\\Downloads\\Project 2 Database - Template.sqlite3")

if dbFile.exists():
   conn = sqlite3.connect(dbFile)
   cur = conn.cursor()
else:
   messagebox.showerror("Database", "Database file not found.")
   quit()
 
vanilla = 0
chocolate = 0
sprinkles = 0
whipcream = 0
hotfudge = 0
sales = 0
expenses = 0


def updateDatabase():
   # Update inventory data
   inventory_sql = "UPDATE inventory SET vanilla=?, chocolate=?, sprinkles=?, whipcream=?, hotfudge=? WHERE id=1"
   inventory_values = (vanilla, chocolate, sprinkles, whipcream, hotfudge)
   cur.execute(inventory_sql, inventory_values)

   # Update financial data
   financial_sql = "UPDATE finances SET sales=?, expenses=? WHERE id=1"
   financial_values = (sales, expenses)
   cur.execute(financial_sql, financial_values)

   # Commit changes to the database
   conn.commit()


def updateLabels():
   global vanilla, chocolate, sprinkles, whipcream, hotfudge, sales, expenses

   # Update inventory data
   inventory_sql = "SELECT vanilla, chocolate, sprinkles, whipcream, hotfudge FROM inventory"
   cur.execute(inventory_sql)
   inventory_row = cur.fetchone()
   vanilla, chocolate, sprinkles, whipcream, hotfudge = inventory_row

   # Update financial data
   financial_sql = "SELECT sales, expenses FROM finances"
   cur.execute(financial_sql)
   financial_row = cur.fetchone()
   sales, expenses = financial_row

   # Update labels with inventory data
   lblVanInv.config(text=vanilla)
   lblChocInv.config(text=chocolate)
   lblSprinInv.config(text=sprinkles)
   lblWhipInv.config(text=whipcream)
   lblFudgInv.config(text=hotfudge)

   # Update labels with financial data
   lblSales.config(text=sales)
   lblExpenses.config(text=expenses)
   lblProfit.config(text = f"${float(sales - expenses)}")


# Update Past Orders Listbox with order numbers
   cur.execute("SELECT orderNumber FROM orders")
   order_numbers = [str(row[0]) for row in cur.fetchall()]
 
   lstPastOrders.delete(0, END)
   lstPastOrders.insert(END, *order_numbers)


def addToInventory():
   global vanilla, chocolate, sprinkles, whipcream, hotfudge, expenses

   if vanVar.get() == 1:
       vanilla = vanilla + 256.0
       lblVanInv.config(text = vanilla)
       expenses += 15
   if chocVar.get() == 1:
       chocolate = chocolate + 256.0
       lblChocInv.config(text = chocolate)
       expenses += 15
   if sprinVar.get() == 1:
       sprinkles = sprinkles + 64.0
       lblSprinInv.config(text = sprinkles)
       expenses += 40
   if whipVar.get() == 1:
       whipcream = whipcream + 64.0
       lblWhipInv.config(text = whipcream)
       expenses += 12
   if fudgVar.get() == 1:
       hotfudge = hotfudge + 48.0
       lblFudgInv.config(text = hotfudge)
       expenses += 10
   lblExpenses.config(text = f"${float(expenses)}")
   lblProfit.config(text = f"${float(sales - expenses)}")
   updateDatabase()
   updateLabels()


def addtoLineItem():
 
   try:
       scoops = int(entValue.get())
       if scoops <= 0:
           messagebox.showerror("Scoop Error", "Please enter a valid number of scoops greater than 0.")
           return
   except ValueError:
       messagebox.showerror("Scoop Error", "Please enter a valid integer for the number of scoops.")
       return
 
   scoops = int(entValue.get())
   scoopAmount = scoops * 4

   order_details = f"{scoops} Scoops {'Vanilla' if rdoSelected.get() == 0 else 'Chocolate'} "
   toppings = []

   if sprinVar1.get() == 1:
       toppings.append("Sprinkles")
   if whipVar1.get() == 1:
       toppings.append("Whipped_Cream")
   if fudgVar1.get() == 1:
       toppings.append("Hot_Fudge")

   if toppings:
       order_details += f"{' '.join(toppings)}"
     
   lstLineItems.insert(END, order_details)
 

def placeOrder():
   global vanilla, chocolate, sprinkles, whipcream, hotfudge, sales
 
   if not lstLineItems.get(0, END):
       messagebox.showerror("Order Error", "Please add items to the order.")
       return
 
   tempVanilla = 0
   tempChocolate = 0
   tempSprinkles = 0
   tempWhippedcream = 0
   tempHotfudge = 0
   tempSales = 0

   num_items = lstLineItems.size()
   for index in range(num_items):
       item  = lstLineItems.get(index)
       components = item.split()
       scoops = int(components[0])
       tempSales += 3 + (scoops - 1)
       flavor = components[2]
       toppings = components[3:] if len(components) > 3 else []
         
       if flavor.lower() == 'vanilla':
           tempVanilla += scoops * 4
       if flavor.lower() == 'chocolate':
           tempChocolate += scoops * 4
       if 'Hot_Fudge' in toppings:
           tempHotfudge += .5
       if 'Whipped_Cream' in toppings:
           tempWhippedcream += 1
       if 'Sprinkles' in toppings:
           tempSprinkles += .25

   if tempVanilla > vanilla or tempChocolate > chocolate or tempSprinkles > sprinkles or tempWhippedcream > whipcream or tempHotfudge > hotfudge:
       messagebox.showerror("Inventory Error", "Insufficient inventory to place the order. Add more inventory or cancel order. ")
   else:
       vanilla -= tempVanilla
       chocolate -= tempChocolate
       sprinkles -= tempSprinkles
       whipcream -= tempWhippedcream
       hotfudge -= tempHotfudge
       sales += tempSales
     
       cur.execute("SELECT MAX(CAST(orderNumber AS INTEGER)) FROM orders")
       max_order_number = cur.fetchone()[0]

       # Increment the order number
       new_order_number = str(max_order_number + 1) if max_order_number is not None else '1'

       # Insert order details into the orders table
       order_insert_sql = "INSERT INTO orders (orderNumber, lineItemText) VALUES (?, ?)"
       order_values = (new_order_number, '\n'.join(lstLineItems.get(0, END)))
       cur.execute(order_insert_sql, order_values)

       conn.commit()
       lstLineItems.delete(0, END)  # This will delete all items from index 0 to the end
       lstPastOrders.insert(END, new_order_number)
             
   tempVanilla = 0
   tempChocolate = 0
   tempSprinkles = 0
   tempWhippedcream = 0
   tempHotfudge = 0

   updateDatabase()
   updateLabels()


def cancelOrder():
   lstLineItems.delete(0, END)  # This will delete all items from index 0 to the end


def showOrderDetails():
   selected_order_number_index = lstPastOrders.curselection()
 
   if selected_order_number_index:
       selected_order_number = lstPastOrders.get(selected_order_number_index)
     
       # Retrieve and display the corresponding line item text in the Past Order Details Listbox
       cur.execute("SELECT lineItemText FROM orders WHERE orderNumber=?", (selected_order_number,))
       line_item_text = cur.fetchone()[0]
     
       # Split the line_item_text into separate lines
       lines = line_item_text.split('\n')

       # Clear existing items in the Listbox
       lstPastOrderDetails.delete(0, END)
     
       # Insert each line into the Listbox
       for line in lines:
           lstPastOrderDetails.insert(END, line)


root = Tk()
root.title("Project 2")
root.geometry("1000x500")

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

Button(root, text = "Add to Inventory", command = addToInventory).grid(row=6, column=2, sticky=W)

Label(root, text="ORDER FORM").grid(row=0, column=3, sticky=W)
Label(root, text = "Scoops").grid(row=1, column=3, sticky=W)
entValue = Entry(root, width=5)
entValue.grid(row=1, column=3, sticky=W, padx=60)
rdoSelected = IntVar()
rdoVan = Radiobutton(root, text="Vanilla", variable = rdoSelected, value=0).grid(row=2, column=3, sticky=W)
rdoChoc = Radiobutton(root, text="Chocolate", variable = rdoSelected, value=1).grid(row=2, column=3, sticky=W, padx=70)
sprinVar1 = IntVar()
chkSprin1 = Checkbutton(root, text = "Sprinkles", variable = sprinVar1).grid(row=3, column=3, sticky=W)
whipVar1 = IntVar()
chkWhip1 = Checkbutton(root, text = "Whipped Cream", variable = whipVar1).grid(row=4, column=3, sticky=W)
fudgVar1 = IntVar()
chkFudg1 = Checkbutton(root, text = "Hot Fudge", variable = fudgVar1).grid(row=5, column=3, sticky=W)
Button(root, text="Add to Order", command = addtoLineItem).grid(row=6, column=3, sticky=W)

Label(root, text="FINANCIAL DATA").grid(row=0, column=3, sticky=W, padx=200)
Label(root, text = "Sales:").grid(row=1, column=3, sticky=W, padx=200)
Label(root, text = "Expenses:").grid(row=2, column=3, sticky=W, padx=200)
Label(root, text = "Profit:").grid(row=3, column=3, sticky=W, padx=200)


lblSales = Label(root, text = "$0.00")
lblSales.grid(row=1, column=3, sticky=W, padx=240)
lblExpenses = Label(root, text = "$0.00")
lblExpenses.grid(row=2, column=3, sticky=W, padx=265)
lblProfit = Label(root, text = "$0.00")
lblProfit.grid(row=3, column=3, sticky=W, padx=240)

lblPastOrders = Label(root, text = "PAST ORDERS")
lblPastOrders.grid(row=10, column=0, sticky=W)
frmPastOrders = Frame(root)
frmPastOrders.grid(row=11, column=0, sticky=W)
srcPastOrders = Scrollbar(frmPastOrders)
srcPastOrders.grid(row=11, column=1, sticky=NS)
lstPastOrders = Listbox(frmPastOrders,height = 5, yscrollcommand=srcPastOrders.set)
lstPastOrders.grid(row=11, column=0, sticky=W)
srcPastOrders.config(command=lstPastOrders.yview)
Button(root, text = "Show Order Details", command=showOrderDetails).grid(row=12, column=0, sticky=W)

lblLineItems = Label(root, text = "Line Items")
lblLineItems.grid(row=7, column=3, sticky=W)
frmLineItems = Frame(root)
frmLineItems.grid(row=8, column=3, sticky=W)
srcLineItems = Scrollbar(frmLineItems)
srcLineItems.grid(row=8, column=4, sticky=NS)
lstLineItems = Listbox(frmLineItems,height = 5, width = 50, yscrollcommand=srcLineItems.set)
lstLineItems.grid(row=8, column=3, sticky=W)
srcLineItems.config(command=lstLineItems.yview)
Button(root, text = 'Place Order', command = placeOrder).grid(row=9, column=3, sticky=W)
Button(root, text = 'Cancel Order', command = cancelOrder).grid(row=9, column=3, sticky=W, padx=110)

lblPastOrderDetails = Label(root, text="PAST ORDER DETAILS")
lblPastOrderDetails.grid(row=10, column=3, sticky=W)  # Corrected column value
frmPastOrderDetails = Frame(root)
frmPastOrderDetails.grid(   row=11, column=3, sticky=W)  # Corrected column value
srcPastOrderDetails = Scrollbar(frmPastOrderDetails)
lstPastOrderDetails = Listbox(frmPastOrderDetails, height=5, width = 50,yscrollcommand=srcPastOrderDetails.set)
lstPastOrderDetails.grid(row=11, column=3, sticky=W)
srcPastOrderDetails.config(command=lstPastOrderDetails.yview)
srcPastOrderDetails.grid(row=11, column=4, sticky=NS)

updateLabels()


root.mainloop()