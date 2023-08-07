from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
current_card = {}
to_learn = {}

try:
    # Lees el CSV con Pandas
    data = pd.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/lithuanian_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # Con el orient [{'Lithuanian': 'ir', 'Spanish': 'y'}]
    to_learn = data.to_dict(orient="records")



def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(card_title, text="Lithuanian", fill="black")
    canvas.itemconfig(card_word, text=current_card["Lithuanian"], fill="black")
    window.after(3000, func=flip_card)
    print(current_card["Lithuanian"], current_card["Spanish"])

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv", index=False)
    next_card()



window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

#Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# De esta manera haces referencia a la imagen
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

#Canvas Text
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=LANG_FONT)
card_word = canvas.create_text(400, 263, text=f"Text", fill="black", font=WORD_FONT)


#Buttons
right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()



window.mainloop()