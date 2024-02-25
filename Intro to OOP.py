# Class info at the top of the file

from MyLibrary import * # Circle

# Define two circles

myShape1 = Circle()
myShape2 = Circle()
myShape3 = Sphere()

# Change the values of r
myShape1.r = -15
myShape2.r = 4

myShape1.setR(-10)

# Print the circumferences
print("1:", myShape1.getCircumference())
print("2:", myShape2.getCircumference())

print("Done")
