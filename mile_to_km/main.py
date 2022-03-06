from tkinter import *
from turtle import width

from matplotlib.pyplot import text

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)

def miles_to_km():
    n_miles = input.get()
    km = round(float(n_miles) * 1.60934, 2)
    n_km.config(text=f"{km}")

# input
input = Entry(width=10)
input.grid(row=0, column=1)

# label
miles = Label(text="Miles")
miles.grid(row=0, column=2)

convert = Label(text="is equal to")
convert.grid(row=1, column=0)

n_km = Label(text="0")
n_km.grid(row=1, column=1)

km = Label(text="Km")
km.grid(row=1, column=2)

# button
button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

window.mainloop()