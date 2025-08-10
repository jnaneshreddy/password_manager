from tkinter import *
from tkinter import messagebox
import random

import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genarate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for x in range(nr_letters)]

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_list += [random.choice(numbers) for x in range(nr_numbers)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_list += [random.choice(symbols) for x in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)

    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password = password_entry.get()

    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo("Empty field alert","dont leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details enterd:\n Email:{email}\n"
                                                     f"Password:{password}\n Is it ok to save")
        if is_ok:
            with open ("data.txt","a") as f:
                f.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
# ---------------------------- UI SETUP -------------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Configure columns to expand
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=0)

# Logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
Label(text="Website:").grid(row=1, column=0)
Label(text="Email/Username:").grid(row=2, column=0)
Label(text="Password:").grid(row=3, column=0)

# Entries
website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
website_entry.focus()
email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
email_entry.insert(0,"jnaneshreddyv730@gmail.com")

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="ew")


# Buttons
password_generate_button = Button(text="Generate Password",command=genarate_pass)
password_generate_button.grid(row=3, column=2, sticky="ew")

add_button = Button(text="Add",command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
