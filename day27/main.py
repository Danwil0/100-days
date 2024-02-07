from tkinter import *

def button_clicked():
    print("i got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("my first gui program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

# label

my_label = Label(text="i am a label", font=("Arial", 24))
my_label["text"] = "new text"
my_label.config(text="new text")
my_label.grid(column=0, row=0)

# button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="press Me", command=button_clicked)
button2.grid(column=2, row=0)

# entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)




























window.mainloop()
