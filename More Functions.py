#Function to say hello
def sayHi(firstName):
    print("Hello", firstName)
    
# Main Program
sayHi("Tiffany")
sayHi("Sally")

################################

#Function to add two values
def addValues(value1, value2):
    print(value1 + value2)
    
# Main Program
addValues(2, 5)
addValues(4,1.9)


################################

def getValuesAdded(value1, value2):
    solution = value1 + value2
    return solution

# Main Program
result = getValuesAdded(20,50)
print("result:", result)


################################

print("Variable Example")
value = 0

def getValue():
    # link the value variable to the main programs value variable
    global value
    value = 1
    print("Value from within the function:", value)
    
getValue()
print("Value from outside the function:", value)