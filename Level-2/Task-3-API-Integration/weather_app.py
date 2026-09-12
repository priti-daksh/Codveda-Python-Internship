import requests


def get_weather(city):
    try:
        # Get city coordinates
        geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"

        params = {
            "name": city,
            "count": 1
        }

        response = requests.get(geocoding_url, params=params)
        response.raise_for_status()

        data = response.json()

        if "results" not in data:
            print("City not found!")
            return

        location = data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]
        city_name = location["name"]
        country = location["country"]

        # Get weather data
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,apparent_temperature,wind_speed_10m"
        }

        weather_response = requests.get(
            weather_url,
            params=weather_params
        )

        weather_response.raise_for_status()

        weather_data = weather_response.json()
        current = weather_data["current"]

        print("\n===== WEATHER INFORMATION =====")
        print(f"City: {city_name}")
        print(f"Country: {country}")
        print(f"Temperature: {current['temperature_2m']} °C")
        print(f"Feels Like: {current['apparent_temperature']} °C")
        print(f"Wind Speed: {current['wind_speed_10m']} km/h")

    except requests.exceptions.RequestException:
        print("Error connecting to the Weather API!")

    except Exception as error:
        print("An error occurred:", error)


city = input("Enter city name: ")
get_weather(city)