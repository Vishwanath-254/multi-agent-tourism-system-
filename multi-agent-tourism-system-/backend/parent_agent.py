from weather_agent import WeatherAgent
from places_agent import PlacesAgent

class TourismAgent:
    def __init__(self):
        self.weather_agent = WeatherAgent()
        self.places_agent = PlacesAgent()

    def generate_response(self, place: str, want_weather: bool = True, want_places: bool = True) -> str:
        # First check if place is valid via geocoding (indirectly via agents)
        weather_text = None
        places_list = None

        if want_weather:
            weather_text = self.weather_agent.get_weather(place)
            if weather_text is None:
                return f"Sorry, I don't recognize the place '{place}'."

        if want_places:
            places_list = self.places_agent.get_places(place)
            if places_list is None:
                return f"Sorry, I don't recognize the place '{place}'."

        parts = []
        if want_weather and weather_text:
            parts.append(weather_text)

        if want_places:
            if places_list:
                place_lines = "\n".join(f"- {p}" for p in places_list)
                parts.append(f"Here are some places you can visit in {place}:\n{place_lines}")
            else:
                parts.append(f"I couldn't find attractions for {place}, but the place seems valid.")

        return " ".join(parts)
