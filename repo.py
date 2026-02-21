'''Dance class form'''


from tkinter import *

def getvals():
    print(f"Name: {namevalue.get()}")
    print(f"Age: {agevalue.get()}")
    print(f"Dance Style: {stylevalue.get()}")
    print(f"Gender: {gendervalue.get()}")

root = Tk()
root.geometry("650x570")
root.title("Dance Class Registration Form")

# Labels
Label(root, text="Dance Class Registration Form", font="comicsansms 15 bold").grid(row=0, column=1)

Label(root, text="Full Name").grid(row=1, column=0)
Label(root, text="Age").grid(row=2, column=0)
Label(root, text="Dance Style").grid(row=3, column=0)
Label(root, text="Gender").grid(row=4, column=0)

                        # Tkinter Variable Classes
namevalue = StringVar()
agevalue = StringVar()
stylevalue = StringVar()
gendervalue = StringVar()

# Entries
Entry(root, textvariable=namevalue).grid(row=1, column=1)
Entry(root, textvariable=agevalue).grid(row=2, column=1)
Entry(root, textvariable=stylevalue).grid(row=3, column=1)

# Radio Buttons for Gender
Radiobutton(root, text="Male", variable=gendervalue, value="Male").grid(row=4, column=1)
Radiobutton(root, text="Female", variable=gendervalue, value="Female").grid(row=5, column=1)
Radiobutton(root, text="Other", variable=gendervalue, value="Other").grid(row=6, column=1)

# Submit Button
Button(root, text="Submit", command=getvals).grid(row=7, column=1)

root.mainloop()



