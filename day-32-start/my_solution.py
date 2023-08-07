import smtplib
import datetime as dt
import random

my_email = "danlsk1986@gmail.com"
password = "rqpdqaoepbfmaglu"

"""STEP 1: Use datetime library to get the current day of the week"""

now = dt.datetime.now()
day_of_the_week = now.weekday()


def get_quote():
    with open("quotes.txt") as file:
        quotes = file.readlines()
        """STEP 3: Use random module to pick a random quote from your list"""
        quote_of_the_day = random.choice(quotes)
        return quote_of_the_day

"""STEP 4: Use smtplib to send an email to yourself"""
def check_day(current_day):
    today = dt.datetime.now()
    day_week = today.weekday()
    if day_week == current_day:
        quote = get_quote()
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls() # Secure connection
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="mazinger_086@yahoo.com",
                                msg=f"Subject:New Quote of the day\n\n{quote}")

check_day(6)












