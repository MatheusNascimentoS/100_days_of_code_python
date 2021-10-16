import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()

my_email = "matheus.pytests@gmail.com"
password = "smfc65wk%kf"



random_line = random.randint(1, 102)

with open(r"day_32\quotes.txt") as quotes:
    all_quotes = quotes.readlines()
    quote = random.choice(all_quotes) 


if day_of_week == 3:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="matheus.jcs@gmail.com",
            msg=f"Subject:Motivational Monday\n\n{quote}"
        )
