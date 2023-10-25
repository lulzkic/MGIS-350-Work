# Create a list
myList = [1, 2, 3, 4]
myList.append(5)
print(type(myList), myList)

# Create a tuple
myTuple = (1, 2, 3, 4)
#myTuple.append(5)  Cannot change a tuple
print(type(myTuple), myTuple)

# Create a set                      sets have no particular order when it comes back
mySet = {"a", "b", "c", "d"}
mySet.add("e")
mySet.add("c")
print(type(mySet), mySet)

# Create a dictionary for a single person
myPerson = {"name": "John Smith", "address": "123 Fake St.", "city": "Fakeville", "state": "NY"}
print(type(myPerson), myPerson)
print("Address:", myPerson["address"])

# Address Book
myAddressBook = list()

myAddressBook.append( {"name": "Sue", "address": "456 South Ave", "city": "Rochester", "state": "NY"})
myAddressBook.append(myPerson)

print(myAddressBook)
print(myAddressBook[1]['address'])