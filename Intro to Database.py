import sqlite3   # Library for using the database
import pathlib  # Library for working with the file system

# Creating a variable for where the database is location
dbFile = pathlib.Path("C:\\Users\\user\\Documents\\MGIS 350 Work\\Template-Database.sqlite3")    # Must use double backslashes for paths

# Test to make sure the database file exists
if dbFile.exists():

    # Connect to the database file
    conn = sqlite3.connect(dbFile)

    # Create a cursor where we can execute our command
    cur = conn.cursor()

    # Create our SQL Query
    sql = "SELECT * FROM transactions WHERE account = 'Checking';"

    # Execute the query
    cur.execute(sql)

    # Grab the records from the query results
    records = cur.fetchall()
    
    balance = 0
    print(records)
    # Print one record at a time
    for record in records:
        print(record)
        balance = balance + record[1]
        
    print("Balance: ", balance)

else:
    print("File doesn't exist")