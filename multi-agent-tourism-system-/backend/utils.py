import requests

def get_coordinates(place: str):
    """
    Uses Nominatim API to convert place name -> (lat, lon).
    Returns (None, None) if not found or on error.
    """
    try:
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": place,
            "format": "json",
            "limit": 1
        }
        # Nominatim requires a User-Agent header
        resp = requests.get(url, params=params, headers={"User-Agent": "multi-agent-tourism-app"}, timeout=10)
        data = resp.json()
        if not data:
            return None, None
        lat = float(data[0]["lat"])
        lon = float(data[0]["lon"])
        return lat, lon
    except Exception:
        return None, None
