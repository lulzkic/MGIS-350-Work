# Proper way to use try/except
try:
    # Read in a number and convert to a float
    value = float(input("Please enter a number: "))
    # Print the number entered
    print("You entered:", value)
except:                   # What we want to happen if there is an error, something went wrong
    # Show the user a custom error message
    print("Please enter a valid number.")
    



# Broken, values will not be in memory using this method
try:
    # Read in a number and convert to a float
    value = float(input("Please enter a number: "))
   
except:                   # What we want to happen if there is an error, something went wrong
    # Show the user a custom error message
    print("Please enter a valid number.")
  
# Print the number entered
print("You entered:", value)