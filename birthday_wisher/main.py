##################### Extra Hard Starting Project ######################
import datetime as dt
from statistics import mode
from numpy import mask_indices
import pandas as pd
import random
import smtplib

my_email = "hyungjin9758@gmail.com"
my_password = "Gudwls5864-"
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today_month = dt.datetime.today().month
today_day = dt.datetime.today().day 

data = pd.read_csv("birthday_wisher/birthdays.csv")
for (index, row) in data.iterrows():
    if today_month == row['month'] and today_day == row['day']:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(file=f"birthday_wisher/letter_templates/letter_{random.randint(1, 3)}.txt", mode="r") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", row['name'])
        # 4. Send the letter generated in step 3 to that person's email address.    
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)    
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row['email'],
                msg=f"Subject:Happy birthday {row['name']}\n\n{letter}"
            )




