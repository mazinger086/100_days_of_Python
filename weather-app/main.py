from tkinter import *
from tkinter import ttk
import pycountry
import requests

OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "302f1b05e0760472c8931d3bd7b16ca6"


countries = list(pycountry.countries)
iso_alpha2_countries = [(country.alpha_2, country.name) for country in countries]

main_data = []

try:
    weather_data = main_data["weather"][0]
    weather_id = weather_data["id"]
    weather_description = weather_data["description"]
    weather_icon = f"http://openweathermap.org/img/w/{weather_data['icon']}.png"

    main_data = main_data["main"]
    temp = main_data["temp"]
    s_termica = main_data["feels_like"]
    temp_max = main_data["temp_max"]
    temp_min = main_data["temp_min"]
except:
    pass




def show_selected():
    city_name = city.get()
    dropdown = combobox.get().split(" ")
    nom = dropdown[0]
    result = f"{city_name},{nom}"
    call_api(result)


def call_api(query):
    # LLAMADO A LA API

    weather_params = {
        "q": f"{query}",
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(OWM_endpoint, params=weather_params)
    response.raise_for_status()
    data = response.json()
    main_data.append(data)
    print(main_data)






window = Tk()
window.minsize(width=300, height=300)
window.title("Weather App")

titulo = Label(text="Weather app", padx=10, pady=10, font=('Arial', 20, "bold"))
titulo.grid(row=0, column=0, columnspan=2)

city_label = Label(text="Ciudad:")
city_label.grid(row=1, column=0, padx=5)

city = Entry()
city.grid(row=1, column=1, pady=5)

country_label = Label(text="Pais/Nom:")
country_label.grid(row=2, column=0)

# Crear el combobox (menú desplegable) y asignar la lista de nombres
combobox = ttk.Combobox(window, values=iso_alpha2_countries, state="readonly", )
combobox.grid(row=2, column=1, pady=5)

search_btn = Button(text="Buscar", command=show_selected)
search_btn.grid(row=3, column=0, padx=10, pady=3, columnspan=1)


if len(main_data) > 1:
    # Mostrar la imagen en tkinter
    photo = PhotoImage(weather_icon)
    image_label = Label(window, image=photo)
    image_label.grid(row=4, column=0, columnspan=1)















# # Asignar una función que se ejecutará cuando se seleccione un nombre en el combobox
# combobox.bind("<<ComboboxSelected>>", on_select)






window.mainloop()
