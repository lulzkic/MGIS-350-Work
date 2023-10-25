from tkinter import *



vanilla = 0
chocolate = 0
sprinkles = 0
whippedCream = 0
hotFudge = 0

orderTotal = 0

sales = 0 
expenses = 0
profit = 0



# create a function for add to inventory button
def cmdAddToInventory():
    global vanilla, chocolate, sprinkles, whippedCream, hotFudge, expenses
    
    # determine if add vanilla is checked
    if varAddVanilla.get() == 1:
        vanilla = vanilla + 250
        expenses = expenses + 15
    
    # determine if add chocolate is checked
    if varAddChocolate.get() == 1:
        chocolate = chocolate + 250
        expenses = expenses + 15
        
    # determine if add sprinkles is checked
    if varAddSprinkles.get() == 1:
        sprinkles = sprinkles + 64
        expenses = expenses + 40
        
    # determine if add whippedCream is checked
    if varAddWhippedCream.get() == 1:
        whippedCream = whippedCream + 64
        expenses = expenses + 12
        
    # determine if add hotFudge is checked
    if varAddHotFudge.get() == 1:
        hotFudge = hotFudge + 48
        expenses = expenses + 10
        
    lblExpenses.config(text=expenses)
        
    # output the inventory
    lblVanilla.config(text=vanilla)
    lblChocolate.config(text=chocolate)
    lblSprinkles.config(text=sprinkles)
    lblWhippedCream.config(text=whippedCream)
    lblHotFudge.config(text=hotFudge)
     

# create a function for place order button
def cmdPlaceOrder():
    global vanilla, chocolate, sprinkles, whippedCream, hotFudge, scoopFlavor, sales , profit, expenses
    
    # reset order total at beginning of each order form
    orderTotal = 0
    
    # reset user feedback messages
    lblUserFeedback.config(text="")
    
    
    print("cmdPlaceOrder Called")
    scoops = float(entScoops.get())
    
    
    if scoopFlavor.get() == 1:    # check if vanilla is checked and inventory is sufficient
        if scoops == 1 and vanilla >= 4:
            orderTotal += 3
            vanilla -= 4
            sprinklesInventory()
            hotFudgeInventory()
            whippedCreamInventory()
        elif scoops > 1 and vanilla >= (scoops * 4):      
            orderTotal += 3 + ((scoops - 1) * 1)
            vanilla -= (scoops * 4)
            sprinklesInventory()
            hotFudgeInventory()
            whippedCreamInventory()
        else:
            # add to user feedback messages
            lblUserFeedback.config(text="Insufficient inventory to place the order. Add more inventory or cancel order")
            btnPlaceOrder.config(state=DISABLED)
            
    elif scoopFlavor.get() == 2 :  # check if chocolate is checked and inventory is sufficient
        if scoops == 1 and chocolate >= 4:
            orderTotal += 3
            chocolate -= 4
            sprinklesInventory()
            hotFudgeInventory()
            whippedCreamInventory()
        elif scoops > 1 and chocolate >= (scoops * 4):
            orderTotal += 3 + ((scoops - 1) * 1)
            chocolate -= (scoops * 4)
            sprinklesInventory()
            hotFudgeInventory()
            whippedCreamInventory()
        else:
            # add to user feedback messages
            lblUserFeedback.config(text="Insufficient inventory to place the order. Add more inventory or cancel order")
            btnPlaceOrder.config(state=DISABLED)
        
        
    sales = sales + orderTotal
    profit = sales - expenses
    
    # output financial data
    lblSales.config(text=sales)
    lblProfit.config(text=profit) 
    
    #output updated inventory
    lblVanilla.config(text=vanilla)
    lblChocolate.config(text=chocolate)
    lblSprinkles.config(text=sprinkles)
    lblWhippedCream.config(text=whippedCream)
    lblHotFudge.config(text=hotFudge)


# determine if add sprinkles is checked and inventory is sufficient 
def sprinklesInventory():
    global sprinkles
    if varSprinklesTopping.get() == 1 and sprinkles >= 0.25:
        sprinkles -= 0.25 
    elif varSprinklesTopping.get() == 1 and sprinkles < 0.25:
        lblUserFeedback.config(text="Insufficient inventory to place the order. Add more inventory or cancel order")
        btnPlaceOrder.config(state=DISABLED)
                     

# determine if add whippedCream is checked and inventory is sufficient 
def whippedCreamInventory():
    global whippedCream
    if varWhippedCreamTopping.get() == 1 and whippedCream >= 1:
        whippedCream -= 1 
    elif varWhippedCreamTopping.get() == 1 and whippedCream < 1:
        lblUserFeedback.config(text="Insufficient inventory to place the order. Add more inventory or cancel order")
        btnPlaceOrder.config(state=DISABLED)
        
           
# determine if add hotFudge is checked and inventory is sufficient  
def hotFudgeInventory():   
    global hotFudge
    if varHotFudgeTopping.get() == 1 and hotFudge >= 0.5:
        hotFudge -= 0.5 
    elif varHotFudgeTopping.get() == 1 and hotFudge < 0.5:
        lblUserFeedback.config(text="Insufficient inventory to place the order. Add more inventory or cancel order")
        btnPlaceOrder.config(state=DISABLED)           
            
            
            
# create a function to get sales
def cmdGetSales():
    print("cmdGetSales Called")
    sales = 0
    # add up order total and add to sales
    sales = sales + orderTotal

# create a function to get expenses
def cmdGetExpenses():
    print("cmdGetExpenses Called")
    expenses = 0
    
# create a function to get profit
def cmdGetProfit():
    print("cmdGetProfit Called")
    profit = 0
    profit = sales - expenses

def cmdGetFinancialData():
    cmdGetSales()
    cmdGetExpenses()
    cmdGetProfit()



# window
root = Tk()
root.title("Ice Cream Stand Project 1")
root.geometry("750x300")

Button(root, text="Add To Inventory", command=cmdAddToInventory).grid(row=6, column=2, sticky=W, padx=5)
btnPlaceOrder = Button(root, text="Place Order", command=cmdPlaceOrder).grid(row=6, column=3, sticky=W, padx=5)


# inventory column
Label(root, text="INVENTORY").grid(row=0, column=0, sticky=W)

Label(root, text="Vanilla:").grid(row=1, column=0, sticky=W)
lblVanilla = Label(root, text ="0")
lblVanilla.grid(row=1, column=1, sticky=W)

Label(root, text="Chocolate:").grid(row=2, column=0, sticky=W)
lblChocolate = Label(root, text ="0")
lblChocolate.grid(row=2, column=1, sticky=W)

Label(root, text="Sprinkles:").grid(row=3, column=0, sticky=W)
lblSprinkles = Label(root, text ="0")
lblSprinkles.grid(row=3, column=1, sticky=W)

Label(root, text="Whipped Cream:").grid(row=4, column=0, sticky=W)
lblWhippedCream = Label(root, text ="0")
lblWhippedCream.grid(row=4, column=1, sticky=W)

Label(root, text="Hot Fudge:").grid(row=5, column=0, sticky=W)
lblHotFudge = Label(root, text ="0")
lblHotFudge.grid(row=5, column=1, sticky=W)


# add to inventory column
Label(root, text="ADD TO INVENTORY").grid(row=0, column=2, padx=5, sticky=W)

# create variable for add vanilla checkbox
varAddVanilla = IntVar()
chkAddVanilla = Checkbutton(root, text="Add 250.0 oz of Vanilla", variable=varAddVanilla)
chkAddVanilla.grid(row=1, column=2, padx=5, sticky=W)

# create variable for add chocolate checkbox
varAddChocolate = IntVar()
chkAddChocolate = Checkbutton(root, text="Add 250.0 oz of Chocolate", variable=varAddChocolate)
chkAddChocolate.grid(row=2, column=2, padx=5, sticky=W)

# create variable for add sprinkles checkbox
varAddSprinkles = IntVar()
chkAddSprinkles = Checkbutton(root, text="Add 64.0 oz of Sprinkles", variable=varAddSprinkles)
chkAddSprinkles.grid(row=3, column=2, padx=5, sticky=W)

# create variable for add whipped cream checkbox
varAddWhippedCream = IntVar()
chkAddWhippedCream = Checkbutton(root, text="Add 64.0 oz of Whipped Cream", variable=varAddWhippedCream)
chkAddWhippedCream.grid(row=4, column=2, padx=5, sticky=W)

# create variable for add hot fudge checkbox
varAddHotFudge = IntVar()
chkAddHotFudge = Checkbutton(root, text="Add 48.0 oz of Hot Fudge", variable=varAddHotFudge)
chkAddHotFudge.grid(row=5, column=2, padx=5, sticky=W)


# order form column
Label(root, text="ORDER FORM").grid(row=0, column=3, sticky=W)

Label(root, text="Scoops:").grid(row=1, column=3, sticky=W)
entScoops = Entry(root)
entScoops.grid(row=1, column=4, sticky=W)

# flavor type radio buttons
scoopFlavor = IntVar()
rdoVanilla = Radiobutton(root, text="Vanilla", variable=scoopFlavor, value=1)
rdoVanilla.grid(row=2, column=3, sticky=W, padx=5)
rdoVanilla.select()
rdoChocolate = Radiobutton(root, text="Chocolate", variable=scoopFlavor, value=2)
rdoChocolate.grid(row=2, column=4, sticky=W)

# select toppings
varSprinklesTopping = IntVar()
chkSprinkles = Checkbutton(root, text="Sprinkles", variable=varSprinklesTopping)
chkSprinkles.grid(row=3, column=3, sticky=W)
varWhippedCreamTopping = IntVar()
chkWhippedCream = Checkbutton(root, text="Whipped Cream", variable=varWhippedCreamTopping)
chkWhippedCream.grid(row=4, column=3, sticky=W)
varHotFudgeTopping = IntVar()
chkHotFudge = Checkbutton(root, text="Hot Fudge", variable=varHotFudgeTopping)
chkHotFudge.grid(row=5, column=3, sticky=W)


# user feedback row
 
Label(root, text="USER FEEDBACK:").grid(row=7, column=0, pady= 5, sticky=W)
lblUserFeedback = Label(root, text=" ")
lblUserFeedback.grid(row=8, column=0, columnspan=4)


# financial data column
Label(root, text="FINANCIAL DATA").grid(row=0, column=5, sticky=W)

Label(root, text="Sales:").grid(row=1, column=5, sticky=W)
lblSales = Label(root, text="$0.00")
lblSales.grid(row=1, column=6, sticky=W)

Label(root, text="Expenses:").grid(row=2, column=5, sticky=W)
lblExpenses = Label(root, text="$0.00")
lblExpenses.grid(row=2, column=6, sticky=W)

Label(root, text="Profit:").grid(row=3, column=5, sticky=W)
lblProfit = Label(root, text="$0.00")
lblProfit.grid(row=3, column=6, sticky=W)


root.mainloop()