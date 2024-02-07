from tkinter import *

window = Tk()
window.title("Centimeters to feet")
window.config(padx=20, pady=20)

def calculation():
    cmm = float(entry_cm.get())
    foot = round(cmm / 30.48)
    is_equal_val.config(text=f"{foot}")


is_equal_to = Label(text="is equal to", font=("Arial", 14))
is_equal_to.grid(column=0, row=1)

is_equal_val = Label(text=0, font=("Arial", 14))
is_equal_val.grid(column=1, row=1)
is_equal_val.config(padx=35, pady=35)


entry_cm = Entry(width=8)
entry_cm.grid(column=1, row=0)

cm = Label(text="centimeters", font=("Arial", 14))
cm.grid(column=2, row=0)
cm.config(padx=10, pady=10)

feetlabel = Label(text="Feet", font=("Arial", 14))
feetlabel.grid(column=2, row=1)
feetlabel.config(padx=10, pady=10)


calc_bttn = Button(text="calculate", command=calculation)
calc_bttn.grid(column=1, row=2)









window.mainloop()
