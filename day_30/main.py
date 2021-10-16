from tkinter import *
from tkinter import messagebox
import random
import pyperclip 
import json

FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    
    input_password.delete(0, END)
    input_password.insert(0, f"{password}")
    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = input_website.get()
    email_data = input_email.get()
    password_data = input_password.get()
    new_data = {
        website_data:{
            "email": email_data,
            "password": password_data,
        }
    }
    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open(r"day_30\data.json", mode="r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
           with open(r"day_30\data.json", mode="w") as data_file:
               json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open(r"day_30\data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:        
            input_password.delete(0, END)
            input_website.delete(0, END)
            input_website.focus()
            messagebox.showinfo(title="Confirmation", message="Data saved.")

# ---------------------------- Search Password ------------------------------- #
def search():
    website_data = input_website.get()
    try: 
        with open(r"day_30\data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website_data in data:
            email_data = data[website_data]['email']
            password_data = data[website_data]['password']
            pyperclip.copy(password_data)
            messagebox.showinfo(title=website_data, message=f"Email: {email_data} \nPassword: {password_data} \nPassword copied")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_data} exist")
        
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file=r"day_29\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)
input_website = Entry(width=34)
input_website.grid(column=1, row=1, columnspan=2, sticky="EW")
input_website.focus()

email = Label(text="Email/Username:")
email.grid(column=0, row=2)
input_email = Entry(width=35)
input_email.grid(column=1, row=2, columnspan=2, sticky="EW")
input_email.insert(0, "matheus.jcs@gmail.com")

password = Label(text="Password:")
password.grid(column=0, row=3, sticky="EW")
input_password = Entry(width=34)
input_password.grid(column=1, row=3)


button_generate_password = Button(text="Generate Password", command=generate_password, width=15)
button_generate_password.grid(column=2, row=3)

button_add = Button(text="Add", command=save, width=30)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")

button_search = Button(text="Search", command=search, width=15)
button_search.grid(column=2, row=1)



window.mainloop()
