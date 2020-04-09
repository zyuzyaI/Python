import json, requests
from geopy.geocoders import Nominatim 

client_id = "{client_id}" # https://ru.foursquare.com/developers/apps
client_secret = "{client_secret}" # https://ru.foursquare.com/developers/apps
location = "49, 28"
categoryId = "52e928d0bcbc57f1066b7e96" #https://developer.foursquare.com/docs/build-with-foursquare/categories

geolocator = Nominatim(user_agent="specify_your_app_name_here")

URL = "https://api.foursquare.com/v2/venues/search"
param = {
    "ll": location,
    "categoryId": categoryId,
    "client_id": client_id,
    "client_secret": client_secret,
    "v": 20200409
}

response = requests.get(URL, params=param)
print(response)
response_json = response.json()

for places in response_json["response"]["venues"]:
    place_name = places["name"]
    lat_lng = ",".join([str(places["location"]["lat"]), str(places["location"]["lng"])])
    place_address = geolocator.reverse(lat_lng)
    print(f"Place name:\n\t{place_name}\naddress:\n\t{place_address}")
    print("---------------------------------------------------------")