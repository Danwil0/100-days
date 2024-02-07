import smtplib
#
my_email = "dan207066@gmail.com"
password = "szuwksaccowaxvia"

import random

import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(year)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15)
# print(date_of_birth)

with open("quotes.txt") as data:
    lists = [quotes.strip() for quotes in data]
quote = random.choice(lists)

now = dt.datetime.now()
day_of_the_week = now.weekday()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="earlyfinesshappiness@gmail.com",
                        msg=f"Subject:Daily Quotes to keep u going\n\n{quote}")



