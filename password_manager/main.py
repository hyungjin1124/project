from distutils import command
from email import message
from re import search
from statistics import mode
from tkinter import *
from random import choice, shuffle, randint
from tkinter import messagebox
from turtle import width
import pyperclip
import json

from matplotlib.pyplot import text, title

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or password == "":
        messagebox.showinfo(title="problem", message="A few fields are blank.")
    else:
        is_ok = messagebox.askokcancel(title='website', message=f"There are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")   
        
        if is_ok:
            try:
                with open("password_manager/password_manager.json", mode ="r") as file:
                    # Reading old data
                    data = json.load(file)
                    # Updating old data with new data
                    data.update(new_data)
            except FileNotFoundError:
                data = new_data
            finally:
                with open("password_manager/password_manager.json", mode ="w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)

                    website_entry.delete(0, 'end')
                    password_entry.delete(0, 'end')

# ---------------------------- SEARCH ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("password_manager/password_manager.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="problem", message="No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(title="success", message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title="problem", message="No details for the website exists")
    finally:
        website_entry.delete(0, 'end')
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# background image
canvas = Canvas(width=200, height=200)
bg_image = PhotoImage(file="password_manager/logo.png")
canvas.create_image(100, 100, image=bg_image)
canvas.grid(row= 0, column= 1)

# website_label
website_label = Label(text='Website:')
website_label.grid(row= 1, column= 0)

# website_entry
website_entry = Entry(width=24)
website_entry.focus()
website_entry.grid(row=1, column=1, sticky=E, padx=2)

# email_username_label
email_username_label = Label(text='Email/Username:')
email_username_label.grid(row= 2, column= 0)

# email_username_entry
email_username_entry = Entry(width=41)
email_username_entry.insert(0, "hjdh0313@naver.com")
email_username_entry.grid(row=2, column=1, columnspan=2, sticky=E)

# password_label
password_label = Label(text='Password:')
password_label.grid(row= 3, column= 0)

# password_entry
password_entry = Entry(width=24)
password_entry.grid(row=3, column=1, sticky=E, padx=2)

# generate_password button
generate_password_button = Button()
generate_password_button.config(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

# add_button
add_button = Button()
add_button.config(text="Add", width=40, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky=E)

# search_button
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2, sticky=W)


window.mainloop()