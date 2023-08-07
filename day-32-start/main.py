import smtplib
import datetime as dt
import random

my_email = "danlsk1986@gmail.com"
password = "rqpdqaoepbfmaglu"

"""STEP 1: Use datetime library to get the current day of the week"""

now = dt.datetime.now()
day_of_the_week = now.weekday()


"""STEP 2: Open quotes.txt file and obtain a list of quites"""
if day_of_the_week == 6:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        """STEP 3: Use random module to pick a random quote from your list"""
        quote = random.choice(quotes)
        print(quote)
        """STEP 4: Use Smtplib to send an random quote"""
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="mazinger_086@yahoo.com",
                msg=f"Subject: Quote of the day\n\n{quote}"
            )


# #YAHOO
# # my_email = "mazinger_086@yahoo.com"
# # password = "" #Check the app password on yahoo
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:









