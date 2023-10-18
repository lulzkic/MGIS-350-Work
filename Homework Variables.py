"""
MGIS 350 - Homework: Variables
September 7, 2023
By Tiffany Wu  
"""

name = input("Please enter your name: ")        ## prompt the user to enter their name
print("Hello", name)                              ## print a greeting with the user's name
value1 = float(input("Can you please provide me a number: "))       ## prompt the user to enter a number
value2 = float(input("Can you please provide me a second number: "))        ## prompt the user to enter a second number
print(name + ",", "the sum of", value1, "and", value2, "is", str(value1 + value2) + ".")    ## print the user's name and the sum of the two numbers