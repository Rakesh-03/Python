from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn={}


try:
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back)

def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index_label=False)

    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)

front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front)
card_title = canvas.create_text(400, 150,text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263,text="", font=("Arial", 60, "bold"))
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

button_no = PhotoImage(file="images/wrong.png")
button = Button(image=button_no, highlightthickness=0, command=next_card)
button.grid(row=1, column=0)

button_yes = PhotoImage(file="images/right.png")
button = Button(image=button_yes, highlightthickness=0, command=is_known)
button.grid(row=1, column=1)



next_card()

window.mainloop()
