# Specify the file location
filepath = "DataFile.txt"

# Open the file in write mode - Will overwrite the existing file 
#fileObject = open(filepath, "w")

# Open the file in append mode - Add to the file
fileObject = open(filepath, "a")

# Write to the file
fileObject.write("Writing to the file. \n")

# Close the file
fileObject.close()

# Open the file in read mode
fileObject = open(filepath, "r")

# Print the contents of the file 
print(fileObject.read())

# Close the file 
fileObject.close()