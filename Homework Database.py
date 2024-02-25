from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import pathlib

# Create a connection to the database
dbFile = pathlib.Path("C:\\Users\\user\\Documents\\MGIS 350 Work\\Homework_Database.sqlite3")

if dbFile.exists():
    # File was found. Create the connection and cursor
    conn = sqlite3.connect(dbFile)
    cur = conn.cursor()
else:
    messagebox.showerror("Database", "Database file not found.")
    quit() # Close the program


def cmdSubmit():
    print("cmdSubmit called")

    try:
        # Retrieve the value from the entry field
        name = entName.get()

        # Insert the name into the database
        sql = "INSERT INTO Contacts (name) VALUES (?)"
        cur.execute(sql, (name,))
        conn.commit()
    except:
        messagebox.showerror("Error", "Try again.")

    # Update Output
    fnDisplayRoster()


def fnDisplayRoster():
    print("fnDisplayRoster called")

    # Clear the listbox
    lstRoster.delete(0, END)

    # Fetch the records from the database
    cur.execute("SELECT name FROM Contacts")
    records = cur.fetchall()

    # Loop through the records and insert them into the listbox
    for record in records:
        lstRoster.insert(END, record[0])


# Setting up window
root = Tk()
root.title("HW - Database")
root.geometry("450x200")

Label(root, text="Name:").grid(row=0, column=0, sticky=W)
entName = Entry(root, width=20)
entName.grid(row=0, column=1, sticky=W)
Button(root, text="Submit", command=cmdSubmit).grid(row=0, column=2, sticky=W)

Label(root, text="Roster:").grid(row=3, column=0, sticky=W)
frmRoster = Frame(root)
frmRoster.grid(row=4, rowspan=4, column=0, sticky=W)
srcRoster = Scrollbar(frmRoster)
srcRoster.pack(side=RIGHT, fill=Y)
lstRoster = Listbox(frmRoster, height=5, yscrollcommand=srcRoster.set)
lstRoster.pack()
srcRoster.config(command=lstRoster.yview)

# Before opening the window (which was established in the lines above), update the listbox
fnDisplayRoster()

# Running main program loop
root.mainloop()