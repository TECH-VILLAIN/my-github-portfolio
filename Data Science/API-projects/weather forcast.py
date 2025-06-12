import requests
API_KEY = "8c28a04fab606d0bdb006609726337a9"
CITY = input("enter city name:")
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid=8c28a04fab606d0bdb006609726337a9&units=metric"
response = requests.get(URL)
data = response.json()
if response.status_code == 200:
    print(f"Weather in {CITY}:")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Description: {data['weather'][0]['description']}")
else:
    print("Failed to retrieve data:", data.get("message"))