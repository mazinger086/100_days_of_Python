from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

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

    if len(website_input.get()) == 0 or len(password_input.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please don´t leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These details entered: \n"
                                                  f"Email: {email} \n"
                                                  f"Password: {password}\n"
                                                  f"Is it ok to save")
        if is_ok:
            #Save data.txt
            with open("data.txt", mode="a") as data:
                data.write(f"{website} | {email} | {password}\n")
                # Clear the values
                website_input.delete(0, END)
                # email_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()









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

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_input.insert(0, "danlsk1986@gmail.com")

password_input = Entry(width=21, show="*")
password_input.grid(column=1, row=3, sticky="EW", pady=3)

#BUTTONS

generate_password = Button(text="Generate Password", bd=0.5, command=generate_password)
generate_password.grid(column=2, row=3, padx=3, pady=3)

add_button = Button(text="Add", width=36, bd=0.5, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")








window.mainloop()