import requests
from utils import get_coordinates

class WeatherAgent:
    def get_weather(self, place: str):
        """
        Returns a human-readable weather string.
        If API fails, returns a graceful message instead of crashing.
        """
        lat, lon = get_coordinates(place)
        if lat is None or lon is None:
            return None  # Parent will treat as unknown place

        try:
            url = "https://api.open-meteo.com/v1/forecast"
            params = {
                "latitude": lat,
                "longitude": lon,
                "current_weather": True
            }
            resp = requests.get(url, params=params, timeout=10)
            data = resp.json()

            current = data.get("current_weather")
            if not current:
                return f"Location '{place}' is valid, but live weather data is not available right now."

            temp = current.get("temperature")
            wind = current.get("windspeed")

            return f"In {place}, it's currently {temp}°C with wind speed {wind} km/h."
        except Exception:
            return f"Could not fetch live weather for {place} due to a network or API error."
