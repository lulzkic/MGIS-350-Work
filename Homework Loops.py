"""
MGIS 350 - Homework: Loops
"""

num = int(input("Enter a valid number greater than 10: "))

if num <= 10:
    print("Input value must be greater than 10. Exiting script.")
else:
    for i in range(0, num + 1, 5):
        print(i)