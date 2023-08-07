import requests
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "302f1b05e0760472c8931d3bd7b16ca6"

account_sid = "AC2b740648567de7e9e1dbc870440a8afc"
auth_token = "6c0520d6dc6f889744ca34f18aa6f80b"

my_lat = -34.479270
my_lon = -58.699060

rainy_lat = 26.599689
rainy_lon = 127.976830

weather_params = {
    "lat": rainy_lat,
    "lon": rainy_lon,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}


response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

weather_hours_list = weather_data["hourly"][:11]


will_rain = False

for hours in weather_hours_list:
    condition_code = hours["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☂️",
        from_='+12058394949',
        to='+541136086250'
    )

print(message.status)






