import random
import smtplib
import datetime as dt

MY_EMAIL = "bhattarainick@gmail.com"
MY_PASSWORD = "!"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt") as quotes_file:
        data = quotes_file.readlines()
        quote_of_the_day = random.choice(data)
        
    print(quote_of_the_day)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote_of_the_day}"
        )