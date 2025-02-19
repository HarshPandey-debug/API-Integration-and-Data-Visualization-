import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# OpenWeatherMap API key (Replace 'YOUR_API_KEY' with your actual API key)
API_KEY = "5069a1eb9e8e980190c97e01806dc50d"
CITY = "New Delhi"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

# Fetch data from OpenWeatherMap API
params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric",  # Use 'imperial' for Fahrenheit
    "cnt": 10  # Number of forecasts to retrieve
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if response.status_code == 200:
    # Extract time and temperature
    times = [datetime.datetime.fromtimestamp(entry["dt"]) for entry in data["list"]]
    temperatures = [entry["main"]["temp"] for entry in data["list"]]

    # Plot the data
    sns.set_style("darkgrid")
    plt.figure(figsize=(10, 5))
    plt.plot(times, temperatures, marker="o", linestyle="-", color="b", label="Temperature (°C)")

    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.title(f"Temperature Forecast for {CITY}")
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

else:
    print("Error:", data.get("message", "Failed to fetch data."))
