import requests
import matplotlib.pyplot as plt
API_KEY = ""
LAT = input("enter latitude")
LON = input("enter longitude")
URL = "https://api.openweathermap.org/data/2.5/onecall?lat={LAT}&lon={LON}&exclude=current,minutely,hourly,alerts&units=metric&appid="
response = requests.get(URL)
data = response.json()
days= []
temps= []
for day in data["daily"]:
    days.append(day["dt"])
    temps.append(day["temp"]["day"])
from datetime import datetime
days = [datetime.fromtimestamp(d).strftime('%a %d') for d in days]
plt.figure(figsize=(10, 5))
plt.plot(days, temps, marker='o', color='skyblue')
plt.title("7-Day Weather Forecast for Lagos 🌤️")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()