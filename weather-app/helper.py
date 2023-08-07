import requests


OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "302f1b05e0760472c8931d3bd7b16ca6"
#
# weather_params = {
#     "q": "Malvinas Argentinas,Ar",
#     "appid": api_key
# }
#
#
#
# weather = data["weather"][0]["icon"]

# print(weather)
#
# for key, value in data.items():
#     print(key, value)


class weather:
    def __init__(self, city, nom):
        self.OWM_endpoint = f"https://api.openweathermap.org/data/2.5/weather?q={city},{nom}&appid={api_key}"
        self.api_key = "302f1b05e0760472c8931d3bd7b16ca6"
        self.city = city
        self.nom = nom
        self.call_api()

    def call_api(self):
        response = requests.get(self.OWM_endpoint)
        response.raise_for_status()
        data = response.json()
        return data



