import requests
from utils import get_coordinates

class PlacesAgent:
    def get_places(self, place: str):
        """
        Returns a list of up to 5 attraction names near the place.
        Uses Overpass API. Falls back to hardcoded lists for some cities if API fails.
        """
        lat, lon = get_coordinates(place)
        if lat is None or lon is None:
            return None  # Parent will treat as unknown place

        # Helper: fallback static suggestions
        def fallback_places():
            name = place.lower()
            if "bangalore" in name or "bengaluru" in name:
                return [
                    "Lalbagh Botanical Garden",
                    "Cubbon Park",
                    "Bangalore Palace",
                    "Bannerghatta National Park",
                    "Jawaharlal Nehru Planetarium",
                ]
            if "delhi" in name:
                return [
                    "India Gate",
                    "Red Fort",
                    "Qutub Minar",
                    "Humayun's Tomb",
                    "Lotus Temple",
                ]
            return []

        try:
            query = f"""
            [out:json][timeout:25];
            (
              node["tourism"="attraction"](around:6000,{lat},{lon});
              way["tourism"="attraction"](around:6000,{lat},{lon});
              rel["tourism"="attraction"](around:6000,{lat},{lon});
            );
            out center;
            """

            resp = requests.post(
                "https://overpass-api.de/api/interpreter",
                data={"data": query},
                timeout=25
            )
            data = resp.json()

            names = []
            for el in data.get("elements", []):
                tags = el.get("tags", {})
                name = tags.get("name")
                if name and name not in names:
                    names.append(name)

            if not names:
                # use fallback list if Overpass returns nothing
                names = fallback_places()

            return names[:5]
        except Exception:
            # If Overpass fails completely, still don't crash
            return fallback_places()
