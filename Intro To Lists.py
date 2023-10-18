# Create a list of letters
values = ["a", "b", "c", "d", "e", "f"]
# print the entire list
print("List:", values)

# Print the third value from the list
print("Third value:", values[2])

# change a value
print(values, "Before Change")
values[2] = "z"   #changes value from whatever it was to the new value
print(values, "After Change")

# add a value
print(values, "Before Add")
values.append("y")
print(values, "After Add")

# insert a value
print(values, "Before Insert")
values.insert(3, "x")
print(values, "After Insert")

# remove a value
values.append("d")
print(values, "Before Remove")
values.remove("d")   # removes the first instance of the value
print(values, "After Remove")

# remove a value based on index
print(values, "Before Pop")
values.pop(1)     
print(values, "After Pop")

# call an invalid index
#print("Invalid:", values[10])

print("While Loop Example")
# create a variable for tracking my position within the list
x = 0
# set up a while loop to test to make sure the position is valid
while x < len(values):
    print(values[x])
    # increment x by 1
    x += 1
print("Done")

print("For Loop Example")
for rows in values:
    print(rows)
print("Done")
