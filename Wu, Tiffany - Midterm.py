# Tiffany Wu
# October 21, 2023


from tkinter import *


def cmdSubmit():
    print("cmdSubmit Called")
    amount = float(entInput.get())
    lstValues.insert(END, amount)
    update_stats()
    
def cmdRemove():
    print("cmdRemove Called")
    lstValues.delete(lstValues.curselection())
    update_stats()   
    
def update_stats():
    values = [float(lstValues.get(i)) for i in range(lstValues.size())]
    total = sum(values)
    count = len(values)
    average = total / count if count > 0 else 0

    lblOutputSum.config(text=total)
    lblOutputCount.config(text=count)
    lblOutputAverage.config(text=average)



root = Tk()
root.title("Midterm Exam")
root.geometry("300x200")

Label(root, text="Input Value:").grid(row=0, column=0, sticky=W)
entInput = Entry(root)
entInput.grid(row=0, column=1, columnspan=2, sticky=W)
Button(root, text="Submit", command=cmdSubmit).grid(row=0, column=3, sticky=W)

Label(root, text="Values:").grid(row=1, column=0, sticky=W)
fmrValues = Frame(root)
fmrValues.grid(row=1, column=1, rowspan=4, columnspan=2, sticky=W)
scrValues = Scrollbar(fmrValues)
scrValues.grid(row=0, column=1, sticky=N+S+W)
lstValues = Listbox(fmrValues, height=5, yscrollcommand=scrValues.set)
lstValues.grid(row=0, column=0)
scrValues.config(command=lstValues.yview)
Button(root, text="Remove", command=cmdRemove).grid(row=1, column=3, sticky=W)

Label(root, text="Stats:").grid(row=5, column=0, sticky=W)
Label(root, text="Sum:").grid(row=5, column=1, sticky=W)
Label(root, text="Count:").grid(row=6, column=1, sticky=W)
Label(root, text="Average:").grid(row=7, column=1, sticky=W)

lblOutputSum = Label(root, text="0")
lblOutputSum.grid(row=5, column=2, sticky=E, padx=10)
lblOutputCount = Label(root, text="0")
lblOutputCount.grid(row=6, column=2, sticky=E, padx=10)
lblOutputAverage = Label(root, text="0")
lblOutputAverage.grid(row=7, column=2, sticky=E, padx=10)

root.mainloop()