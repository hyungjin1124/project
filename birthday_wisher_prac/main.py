import smtplib
import datetime as dt
import random

my_email = "hyungjin9758@gmail.com"
my_password = "Gudwls5864-"

current_day = dt.datetime.today().weekday()

if current_day == 2:
    with open(file="birthday_wisher/quotes.txt", mode="r") as file:
        quotes_list = file.readlines()
        today_quote = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="hyungjin5864@gmail.com",
            msg=f'Subject:Monday Motivation\n\n{today_quote}')
    

