from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests


def get_latest_value():
    url = "https://api.bluelytics.com.ar/v2/latest"
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as error:
        messagebox.showerror(title="Error", message=error)
    else:
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            messagebox.showerror(title="Error", message=f"Error al obtener los datos del usuario {response.status_code}")



latest_data = get_latest_value()

oficial_dolar = latest_data['oficial']
blue_dolar = latest_data['blue']
oficial_euro = latest_data['oficial_euro']
blue_euro = latest_data['blue_euro']
last_update = latest_data['last_update']
fecha= f"{last_update[8:10]}/{last_update[5:7]}/{last_update[:4]}"
hora = f"{last_update[11:16]}"

window = Tk()
window.minsize(width=250, height=300)
window.config(pady=50, padx=50)
window.title("Dolar Hoy App")

# Labels

# Dolar Blue
dolar_blue_title = Label(text="Dólar Blue", font=('Arial', 20, "bold"))
dolar_blue_title.grid(column=0, row=0, columnspan=2)

dolar_blue_compra = Label(text="Compra", font=('Arial', 10))
dolar_blue_compra.grid(column=0, row=1, padx=10)

dolar_blue_venta = Label(text="Venta", font=('Arial', 10))
dolar_blue_venta.grid(column="1", row=1, padx=10)

dolar_compra_price = Label(text=f"${blue_dolar['value_buy']}", font=("Monokai", 16, "normal"))
dolar_compra_price.grid(column=0, row=2)

dolar_venta_price = Label(text=f"${blue_dolar['value_sell']}", font=("Monokai", 16, "normal"))
dolar_venta_price.grid(column=1, row=2)

# Crear un divisor horizontal
separator = ttk.Separator(window, orient="horizontal")
separator.grid(row=3, column=0, padx=10, pady=20, columnspan=2)


#Euro Blue
euro_blue_title = Label(text="Euro Blue", font=('Arial', 20, "bold"))
euro_blue_title.grid(column=0, row=4, columnspan=2)

euro_blue_compra = Label(text="Compra", font=('Arial', 10))
euro_blue_compra.grid(column=0, row=5, padx=10)

euro_blue_venta = Label(text="Venta", font=('Arial', 10))
euro_blue_venta.grid(column="1", row=5, padx=10)

euro_compra_price = Label(text=f"${blue_euro['value_buy']}", font=("Monokai", 16, "normal"))
euro_compra_price.grid(column=0, row=6)

euro_venta_price = Label(text=f"${blue_euro['value_sell']}", font=("Monokai", 16, "normal"))
euro_venta_price.grid(column=1, row=6)

ultima_actualizacion = Label(text=f"Actualizado: {fecha}, {hora}")
ultima_actualizacion.grid(column=0, row=7, columnspan=2, pady=20)




window.mainloop()
