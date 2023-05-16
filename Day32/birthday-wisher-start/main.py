##################### Extra Hard Starting Project ######################
import random
import pandas as pd
import datetime as dt
import smtplib

MY_EMAIL = "bhattarainick@gmail.com"
MY_PASSWORD = "!"

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pd.read_csv("birthdays.csv")

birthdays_dict ={(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        print(contents)
    
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(MY_EMAIL, MY_PASSWORD)
    #     connection.sendmail(
    #         from_addr=MY_EMAIL,
    #         to_addrs=birthday_person["email"],
    #         msg=f"Subject: Happy Birthday!\n\n{contents}"
    #         )



