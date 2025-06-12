import requests
url = "https://catfact.ninja/fact"
response = requests.get(url)
print(response)
data = response.json()
print("🐱 Cat Fact:", data['fact'])