import requests
from datetime import datetime
import time
import smtplib

my_email = "danlsk1986@gmail.com"
password = "rqpdqaoepbfmaglu"
MY_LAT = -34.482668 # Your latitude
MY_LONG = 301.304260 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 3
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 3

    time_now = datetime.now().hour

    # Check is its night or not
    if time_now >= sunset or time.now() <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night_time():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="danlasauskas@gmail.com",
                msg=f"Subject: Check the sky Up\n\n Probably you can see the ISS at night sky"
            )



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.





