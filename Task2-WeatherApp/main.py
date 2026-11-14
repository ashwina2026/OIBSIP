
import tkinter as tk
from tkinter import messagebox
import requests


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def get_weather_info(code):
    conditions = {
        0: ("Clear Sky", "☀️"),
        1: ("Mainly Clear", "🌤️"),
        2: ("Partly Cloudy", "⛅"),
        3: ("Overcast", "☁️"),
        45: ("Foggy", "🌫️"),
        48: ("Foggy", "🌫️"),
        51: ("Light Drizzle", "🌦️"),
        53: ("Moderate Drizzle", "🌦️"),
        55: ("Heavy Drizzle", "🌧️"),
        61: ("Light Rain", "🌧️"),
        63: ("Moderate Rain", "🌧️"),
        65: ("Heavy Rain", "🌧️"),
        71: ("Light Snow", "❄️"),
        73: ("Moderate Snow", "❄️"),
        75: ("Heavy Snow", "❄️"),
        80: ("Rain Showers", "🌦️"),
        81: ("Moderate Showers", "🌧️"),
        82: ("Heavy Showers", "⛈️"),
        95: ("Thunderstorm", "⛈️"),
        96: ("Thunderstorm with Hail", "⛈️"),
        99: ("Heavy Thunderstorm with Hail", "⛈️")
    }

    return conditions.get(code, ("Unknown Weather", "🌡️"))


def search_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showwarning(
            "Empty City",
            "Please enter a city name."
        )
        return

    search_button.config(state="disabled")
    status_label.config(
        text="Fetching weather information...",
        fg="#607D98"
    )

    try:
        # Get city coordinates
        geo_response = requests.get(
            GEOCODING_URL,
            params={
                "name": city,
                "count": 1,
                "language": "en",
                "format": "json"
            },
            timeout=15
        )

        geo_response.raise_for_status()
        geo_data = geo_response.json()

        locations = geo_data.get("results")

        if not locations:
            raise ValueError(
                "City not found. Please check the spelling."
            )

        location = locations[0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        city_name = location["name"]
        country = location.get("country", "")

        # Get current weather
        weather_response = requests.get(
            WEATHER_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": (
                    "temperature_2m,"
                    "relative_humidity_2m,"
                    "weather_code,"
                    "wind_speed_10m"
                ),
                "temperature_unit": "celsius",
                "wind_speed_unit": "kmh",
                "timezone": "auto"
            },
            timeout=15
        )

        weather_response.raise_for_status()
        weather_data = weather_response.json()

        current = weather_data["current"]

        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        wind_speed = current["wind_speed_10m"]
        weather_code = current["weather_code"]

        condition, icon = get_weather_info(weather_code)

        # Display weather information
        location_label.config(
            text=f"{city_name}, {country}"
        )

        icon_label.config(text=icon)

        temperature_label.config(
            text=f"{temperature}°C"
        )

        condition_label.config(
            text=condition
        )

        humidity_label.config(
            text=f"Humidity: {humidity}%"
        )

        wind_label.config(
            text=f"Wind Speed: {wind_speed} km/h"
        )

        status_label.config(
            text="Weather updated successfully!",
            fg="#27834A"
        )

    except ValueError as error:
        status_label.config(
            text="Unable to find this city.",
            fg="#C0392B"
        )

        messagebox.showerror("Search Error", str(error))

    except requests.exceptions.Timeout:
        status_label.config(
            text="Request timed out.",
            fg="#C0392B"
        )

        messagebox.showerror(
            "Connection Error",
            "The request took too long. Please try again."
        )

    except requests.exceptions.RequestException:
        status_label.config(
            text="Connection failed.",
            fg="#C0392B"
        )

        messagebox.showerror(
            "Internet Error",
            "Please check your internet connection."
        )

    except (KeyError, TypeError):
        status_label.config(
            text="Weather data unavailable.",
            fg="#C0392B"
        )

        messagebox.showerror(
            "Data Error",
            "The weather service returned unexpected data."
        )

    finally:
        search_button.config(state="normal")


# Main window
root = tk.Tk()
root.title("Weather Application")
root.geometry("460x600")
root.resizable(False, False)
root.configure(bg="#EAF4FF")


# Fonts
heading_font = ("Helvetica Neue", 23, "bold")
normal_font = ("Helvetica Neue", 11)
label_font = ("Helvetica Neue", 12, "bold")


# Heading
tk.Label(
    root,
    text="Weather App",
    font=heading_font,
    bg="#EAF4FF",
    fg="#244B73"
).pack(pady=(14, 2))


tk.Label(
    root,
    text="Check the current weather of any city",
    font=normal_font,
    bg="#EAF4FF",
    fg="#607D98"
).pack(pady=(0, 12))


# City input
tk.Label(
    root,
    text="Enter City Name",
    font=label_font,
    bg="#EAF4FF",
    fg="#244B73"
).pack(pady=3)


city_entry = tk.Entry(
    root,
    width=27,
    font=("Helvetica Neue", 12),
    justify="center",
    bg="white",
    fg="#244B73",
    relief="flat",
    bd=0,
    highlightthickness=1,
    highlightbackground="#B8D5F0",
    highlightcolor="#4386C6"
)
city_entry.pack(pady=7, ipady=7)


# Search button
search_button = tk.Button(
    root,
    text="Search Weather",
    command=search_weather,
    font=("Helvetica Neue", 11, "bold"),
    bg="#D1E7FF",
    fg="#244B73",
    activebackground="#B8D5F0",
    activeforeground="#244B73",
    relief="flat",
    bd=0,
    cursor="hand2",
    width=23,
    pady=7
)
search_button.pack(pady=5)


# Status message
status_label = tk.Label(
    root,
    text="Ready to search",
    font=("Helvetica Neue", 9),
    bg="#EAF4FF",
    fg="#607D98"
)
status_label.pack(pady=3)


# Location
location_label = tk.Label(
    root,
    text="Search for a city",
    font=("Helvetica Neue", 14, "bold"),
    bg="#EAF4FF",
    fg="#244B73"
)
location_label.pack(pady=(8, 2))


# Weather icon
icon_label = tk.Label(
    root,
    text="🌤️",
    font=("Arial", 38),
    bg="#EAF4FF"
)
icon_label.pack(pady=1)


# Temperature
temperature_label = tk.Label(
    root,
    text="--°C",
    font=("Helvetica Neue", 34, "bold"),
    bg="#EAF4FF",
    fg="#244B73"
)
temperature_label.pack(pady=1)


# Weather condition
condition_label = tk.Label(
    root,
    text="Weather Condition",
    font=label_font,
    bg="#EAF4FF",
    fg="#607D98"
)
condition_label.pack(pady=3)


# Humidity
humidity_label = tk.Label(
    root,
    text="Humidity: --%",
    font=normal_font,
    bg="#EAF4FF",
    fg="#244B73"
)
humidity_label.pack(pady=3)


# Wind speed
wind_label = tk.Label(
    root,
    text="Wind Speed: -- km/h",
    font=normal_font,
    bg="#EAF4FF",
    fg="#244B73"
)
wind_label.pack(pady=3)


# Enter key to search
city_entry.bind(
    "<Return>",
    lambda event: search_weather()
)


# Start application
root.mainloop()
