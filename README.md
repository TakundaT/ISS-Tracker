# ISS Tracker

## Description
This Python script checks whether the International Space Station (ISS) is currently overhead at your location and whether it is nighttime. If both conditions are met, the script sends an email notification to alert you to check the sky.

## Features
- Retrieves real-time ISS position data from [Open Notify API](http://api.open-notify.org/iss-now.json).
- Determines sunset and sunrise times for your location using [Sunrise-Sunset API](https://sunrise-sunset.org/api).
- Compares your location with the ISS location to check proximity.
- Sends an email notification when the ISS is overhead and it is nighttime.

## Requirements
Ensure you have the following Python modules installed:
```sh
pip install requests
```

## Configuration
Before running the script, update the following variables with your details:
- `EMAIL`: Your email address (Gmail recommended)
- `PASSWORD`: Your email password (Consider using an app password for security)
- `MY_LAT`: Your latitude coordinate
- `MY_LONG`: Your longitude coordinate

## How It Works
1. The script fetches the ISS's current latitude and longitude.
2. It checks if the ISS is within ±6 degrees of your latitude and longitude.
3. It retrieves local sunset and sunrise times and determines if it is currently nighttime.
4. If both conditions are met, the script sends an email notification.
5. The script runs in a loop, checking every 200 seconds.

## Usage
Run the script using:
```sh
python iss_tracker.py
```

## Important Notes
- Ensure "Less Secure Apps" is enabled in your Gmail account or use an App Password.

## License
This project is open-source and free to use.

## Author
Takunda Christian Takaindisa

