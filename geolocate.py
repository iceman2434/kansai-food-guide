from geopy.geocoders import GoogleV3
from config import API_KEY

def get_coordinates(address):
    geolocator = GoogleV3(api_key=API_KEY)
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
    except:
        pass
    return None, None