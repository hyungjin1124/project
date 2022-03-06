from distutils import command
from tkinter import *

from matplotlib.pyplot import text

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

def button_clicked():
    my_label['text'] = input.get()

# Label

my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))

my_label.config(text="New Text")
my_label.grid(row=0, column=0)

# Button

button = Button(text='Click Me', command=button_clicked)
button.grid(row=1, column=1)

new_button = Button(text='New Button', command=button_clicked)
new_button.grid(row=0, column=2)

# Entry

input = Entry(width=10)
input.grid(row=2, column=3)



window.mainloop()