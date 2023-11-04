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

myAddressBook.append( {"name": "Sue", "address": "456 South Ave", "city": "Rochester", "state": "NY", "zip": "12345"} )
myAddressBook.append(myPerson)

print(myAddressBook)
print(myAddressBook[1]['address'])

# Loop through our data to see who is missing a zip code
for person in myAddressBook:
    print("person:", person)
    # test for a zip code
    if 'zip' in person:
        print(person['name'], "has a zip code")
    else:
        print(person['name'], "does not have a zip code")
        person['zip'] = input("Please enter a zip code: ")
        
print("Complete Address Book", myAddressBook)