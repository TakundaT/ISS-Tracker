import requests
from datetime import datetime
import smtplib
import time

EMAIL = "insert your email here " 
PASSWORD = "insert your password here"

MY_LAT = 43.255722 # Your latitude
MY_LONG = -79.871101 # Your longitude
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
#Your position is within +6 or -6 degrees of the ISS position.
    if MY_LAT-6 <= iss_latitude <= MY_LAT + 6 and MY_LONG -6 <= iss_longitude <= MY_LONG +6:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 4
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 4

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

#If the ISS is close to my current position
# and it is currently dark

while True:
    time.sleep(200)
    if is_iss_overhead and is_night:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=("Subject:Check the sky\n\n The International Space Station is Flying above you now")
        )

