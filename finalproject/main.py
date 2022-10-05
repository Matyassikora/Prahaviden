import json
import urllib.request as urllib2
import requests


# People in space
response = requests.get("http://api.open-notify.org/astros.json")
astros = response.json()

# Current position and Timestamp
req = urllib2.Request("http://api.open-notify.org/iss-now.json")
response = urllib2.urlopen(req)
obj = json.loads(response.read())

# Current position
# print obj['iss_position']['latitude'], obj['data']['iss_position']['latitude']

print(f"\nAstronauts")
print(f"There are currently {astros['number']} astronauts in space.\n")

print(f"\nTimestamp")
print(f"Current timestamp is {obj['timestamp']}\n")

#print(f"Latitude {obj['latitude']}")
