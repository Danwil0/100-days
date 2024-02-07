from tkinter import *
import pandas
import random
choice = None


BACKGROUND_COLOR = "#B1DDC6"
french_ps = {}
current_card = {}

# new flash card
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    french_ps = original_data.to_dict(orient="records")
else:
    french_ps = data.to_dict(orient="records")


def choice1():
    global choice
    choice = 'green'
def choice2():
    global choice
    choice = 'red'

def french_word():
    global current_card, flip_timer, choice
    window.after_cancel(flip_timer)
    current_card = random.choice(french_ps)
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(txt_id, text=current_card["French"], fill="black")
    canvas.itemconfig(image_on_canvas, image=canvas_image)
    if choice == "green":
        french_ps.remove(current_card)
        df = pandas.DataFrame(french_ps)
        df.to_csv("words_to_learn.csv", index=False)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(image_on_canvas, image=canvas_image_back)
    canvas.itemconfig(txt_id, text=current_card["English"], fill="white")
    canvas.itemconfig(image_on_canvas, image=canvas_image_back)


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


canvas_image = PhotoImage(file="../flash-card-project-start/images/card_front.png")
canvas_image_back = PhotoImage(file="../flash-card-project-start/images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_on_canvas = canvas.create_image(0, 0, anchor=NW, image=canvas_image)
canvas_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
txt_id = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="../flash-card-project-start/images/right.png")
right_button = Button(image=right_image, command=lambda: [french_word(), choice1()], highlightthickness=0, height=50, width=50)
right_button.grid(column=0, row=1)

left_image = PhotoImage(file="../flash-card-project-start/images/wrong.png")
left_button = Button(image=left_image, command=lambda: [french_word(), choice2()], highlightthickness=0, height=50, width=50)
left_button.grid(column=1, row=1)

french_word()

window.mainloop()
