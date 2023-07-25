from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Dependiendo el randint se va repetir el for la cantidad de letras usanso un choice para elegirlas

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    #Get the values
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don´t leave any fields empty!")
    else:
        try:
            # Save data.json
            with open("data.json", "r") as data_file:
                # Read JSON
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                print("Create a new file because did not exist")
        else:
            # Update JSON with the new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Write JSON with the data info in case it have it
                json.dump(data, data_file, indent=4)

                print("Append the new item in the dictionary")
        finally:
            # Clear the values
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()


def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        website = website_input.get()
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showerror(title="Error", message=f"There is no {website} saved previously")
    finally:
        website_input.delete(0, END)










# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

#SET IMAGE & CANVAS
lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)


#LABELS

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, pady=3)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, pady=3)


#ENTRIES/INPUTS

website_input = Entry(width=21)
website_input.grid(column=1, row=1, sticky="EW")
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_input.insert(0, "danlsk1986@gmail.com")

password_input = Entry(width=21, show="*")
password_input.grid(column=1, row=3, sticky="EW", pady=3)

#BUTTONS

search_btn = Button(text="Search", bd=0.5, command=find_password)
search_btn.grid(column=2, row=1, padx=3, pady=3, sticky="EW")

generate_password = Button(text="Generate Password", bd=0.5, command=generate_password)
generate_password.grid(column=2, row=3, padx=3, pady=3)

add_button = Button(text="Add", width=36, bd=0.5, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")










window.mainloop()