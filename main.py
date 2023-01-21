BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

#################### DATA SETUP ####################
try:
    data = pandas.read_csv("data/en_ita.csv")
except FileNotFoundError:
    data={"Inglese": [], "Italiano": []}
else:
    data = data.to_dict(orient="records")

word= random.choice(data)

#################### LOGIC SETUP ####################

#pick a random word from data.Inglese
def next_word():
    global word
    word= random.choice(data)
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(titolo, text="Inglese", fill="black")
    canvas.itemconfig(testo, text=word["Inglese"], fill="black")
    
def see_translate_word():
    global word
    canvas.itemconfig(titolo, text="Italiano", fill="white")
    canvas.itemconfig(testo, text=word["Italiano"], fill="white")
    canvas.itemconfig(canvas_img, image=card_back_img)



################# UI SETUP ####################
window = Tk()
window.title("Flash Card Inglese - Italiano")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_img= canvas.create_image(400, 263, image=card_front_img)
titolo= canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
testo= canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons without border
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")


right_button = Button(image=right_img, highlightthickness=0, bd=0, command=next_word)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_img, highlightthickness=0, bd=0, command=see_translate_word)
wrong_button.grid(column=0, row=1)

next_word()
window.mainloop()