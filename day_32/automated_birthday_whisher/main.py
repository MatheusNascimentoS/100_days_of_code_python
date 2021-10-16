##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import random
import csv

my_email = "matheus.pytests@gmail.com"
password = "smfc65wk%kf"

now = dt.datetime.now()
month = now.month
day = now.day
hour = now.hour


# birthdays = pandas.read_csv(r"day_32\automated_birthday_whisher\birthdays.csv")

letter_list = [
    r"day_32\automated_birthday_whisher\letter_templates\letter_1.txt",
    r"day_32\automated_birthday_whisher\letter_templates\letter_2.txt",
    r"day_32\automated_birthday_whisher\letter_templates\letter_3.txt"
    ]
chosen_letter = random.choice(letter_list)

with open(chosen_letter) as letter:
    message = letter.read()
    


# mesage.replace("[NAME]", birthdays["name"])

with open(r"day_32\automated_birthday_whisher\birthdays.csv") as birthdays:
    list_of_birthdays = csv.reader(birthdays)
    for row in list_of_birthdays:
        if row[0] != "name":
            if int(row[3]) == month and int(row[4]) == day:
                message = message.replace('[NAME]', row[0])
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(
                        from_addr=my_email,
                        to_addrs=row[1],
                        msg=f"Subject:Happy Birthday\n\n{message}"
                        )