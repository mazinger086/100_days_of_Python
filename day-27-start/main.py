
from tkinter import *

def button_clicked():
    print("I got clicked")
    # message = input.get()
    # my_label.config(text=message)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(pady=20, padx=20)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 18, "bold"))  # Create
my_label.config(text="New Text")
# my_label.pack()  # Show in window
# my_label.place(x=100, y=0)
my_label.grid(column=0, row=0)
my_label.config(pady=20)

#Buttons
my_button = Button(text="Click Me", command=button_clicked)
my_button.grid(column=1, row=1)

new_button= Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)


# Entry
input = Entry(width=10)
input.grid(column=4, row=3, pady=10)





window.mainloop()  # Mantiene la ventana abierta has que haya interaccion con el usuario
