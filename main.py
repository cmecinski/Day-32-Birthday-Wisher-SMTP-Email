#  Test sending emails using SMTP
# import smtplib
#
# my_email = ""
# password = ""
#
# test_email = ""
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user="", password="")
#     connection.sendmail(from_addr=my_email, to_addrs=test_email, msg="Subject:Hello World\n\nHello World")
#     # connection.close() needed if you don't use with
#
#

###################

# Testing datetime Module from python
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
#
# day_of_weak = now.weekday()
#
# print(now)
#
# date_of_birth = dt.datetime(year=1900, month=12 , day=12)
# print(date_of_birth)

###################

#  Testing Automatic Monday Quote Emailer
# import smtplib
# import datetime as dt
# import random
#
# MY_EMAIL = ""
# MY_PASSWORD = ""
#
# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 0: #weekday 0 is monday
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)
#
#     print(quote)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=MY_EMAIL,
#             msg=f"Subject:Monday Motivation\n\n{quote}"
#         )

import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
