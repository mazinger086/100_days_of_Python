##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import smtplib
import random

MY_EMAIL = "danlsk1986@gmail.com"
MY_PASSWORD = "rqpdqaoepbfmaglu"

# 1. Update the birthdays.csv

data = pd.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")
data_list = [item for item in data_dict]

# 2. Check if today matches a birthday in the birthdays.csv

today = dt.datetime.now()
day_birth = today.day
month_birth = today.month

for index in range(len(data_list)):
    datos = data_list[index]
    dia = datos['day']
    mes = datos['month']
    nombre = datos['name']
    email = datos['email']
    if day_birth == dia and month_birth == mes:
        # print(f"Feliz cumpleaños {nombre}!!!")

        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        rand_letter = str(random.randint(1, 3))
        rand_path = f"letter_templates/letter_{rand_letter}.txt"

        with open(rand_path, "r") as letters:
            template = letters.read().splitlines()
            invitacion = [line.replace('[NAME]', nombre) for line in template]


        with open(rand_path, "w") as invitacion_file:
            invitacion_file.write('\n'.join(invitacion))

        # 4. Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    contenido = '\n'.join(invitacion)
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=email,
                        msg="Subject: Happy Birthday {}\n\n{}".format(nombre, contenido)
                    )


        break  # Exit the loop after finding the birthday to avoid unnecessary iterations







