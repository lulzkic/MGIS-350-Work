# Prompt the user for a number
value = float(input("Please enter a number: "))

# Test to see if the number is greater than 0
if value > 0:
    #Output that the value is positive
    print("Positive")
else:
    #test to see if the number is equal to 0
    if value == 0:
        #output that the value is zero
        print("Zero")
    else:
        #Output that the value is negative
        print("Negative")
   
   
# Second example of how to code.
# Test to see if number is greater than 0
if value > 0:
    #Output that the value is positive
    print("Positive - 2")               #2 is in there to indicate that it is the second test
#Test tp see if the number is equal to 0
elif value == 0:
    #Output that the value is zero
    print("Zero - 2")
else:
    #Output that the value is negative
    print("Negative - 2")

# Let the user know we done 
print("Done")