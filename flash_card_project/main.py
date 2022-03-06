from distutils import command
from operator import index
from sqlite3 import Row
from statistics import mode
from textwrap import indent
from tkinter import *
from tkinter import font
from turtle import width
import pandas as pd
import random

from matplotlib.pyplot import fill, text
BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pd.read_csv("flash_card_project/data/words_to_learn.csv")
except:
    data = pd.read_csv("flash_card_project/data/french_words.csv")

word_dict_list = data.to_dict(orient="records")
word = {}

# -------------------------------DELETE CARD----------------------------------
def is_known():
    word_dict_list.remove(word)
    df = pd.DataFrame(word_dict_list)
    df.to_csv("flash_card_project/data/words_to_learn.csv", index=False)
    show_word()

# -------------------------------CREATE FLASH CARD----------------------------------
def show_word():
    global word, timer
    window.after_cancel(timer)
    word = random.choice(word_dict_list)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfigure(title_section, text='French', fill="black")
    canvas.itemconfigure(word_section, text=word['French'], fill="black")
    timer = window.after(3000, flip_card)

# -------------------------------FLIP THE CARD-------------------------------------
def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfigure(title_section, text='English', fill="white")
    canvas.itemconfigure(word_section, text=word['English'], fill="white")

# -----------------------------------UI---------------------------------
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="flash_card_project/images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=front_image)

# card_back_img
back_image = PhotoImage(file="flash_card_project/images/card_back.png")

# title_section
title_section = canvas.create_text(400, 150, text = "", font=("Ariel", 40, "italic"))

# word_section
word_section = canvas.create_text(400, 263, text = "", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# wrong_button
wrong_button_img = PhotoImage(file="flash_card_project/images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0)
wrong_button.config(command=show_word)
wrong_button.grid(row=1, column=0)

# right_button
right_button_img = PhotoImage(file="flash_card_project/images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0)
right_button.config(command=is_known)
right_button.grid(row=1, column=1)

timer = window.after(3000, flip_card)
show_word()

window.mainloop()