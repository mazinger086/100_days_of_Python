from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=150)
window.config(padx=10, pady=10)



#Input Entry
input = Entry(width=8)
input.grid(column=1, row=0)
input.insert(END, string="0")

#Labels
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

value_label = Label(text="0")
value_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)



def calcular_ml_to_km():
    miles = float(input.get())
    kilometers = round(miles * 1.609, 2)
    value_label.config(text=kilometers)

def calcular_km_to_ml():
    kilometros = float(input.get())
    millas = round(kilometros * 0.6213, 2)
    value_label.config(text=millas)

def check_mode():
    state = radio_state.get()
    if state == 1:
        km_label.config(text="Ml")
        mile_label.config(text="Kilometers")
        value_label.config(text="0")
        input.delete(0, END)
        calculate_btn.config(text="Calculate Km", command=calcular_km_to_ml)
    else:
        km_label.config(text="Km")
        mile_label.config(text="Miles")
        value_label.config(text="0")
        input.delete(0, END)
        calculate_btn.config(text="Calculate Ml", command=calcular_ml_to_km)



#Radio
radio_state = IntVar()
ml_mode = Radiobutton(text="Ml to Km", value=0, variable=radio_state, command=check_mode)
km_mode = Radiobutton(text="Km to Ml", value=1, variable=radio_state, command=check_mode)

ml_mode.grid(column=0, row=2)
km_mode.grid(column=0, row=3)




#Button
calculate_btn = Button(text="Calculate Ml", command=calcular_ml_to_km, pady=5, padx=5)
calculate_btn.grid(row=2, column=1, pady=5)


window.mainloop()