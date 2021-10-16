import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -28.262350
MY_LNG = -52.408989

MY_EMAIL = "matheus.pytests@gmail.com"
PASSWORD = "smfc65wk%kf"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LNG -5 <= iss_longitude <= MY_LNG +5):
        return True
# Your position is within +5 or -5 degrees of the ISS position 
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng":MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 2
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    hour_now = datetime.now().hour
    if hour_now > sunset or hour_now < sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Look Up\n\nThe ISS is above you in the sky."
                )

