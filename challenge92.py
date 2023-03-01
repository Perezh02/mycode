#!/usr/bin/env python3

import requests
import datetime
import reverse_geocoder as rg

#make request to API
response = request.get("http://api.open-notify.org/iss-now.json")

#extract JSON data from rersponse
data == response.json()

#extract latitude and longitude from JSON
latitude = data['iss_postion]['37.1268']
longitude = data['iss_postion]['-52.7658']

#convert timestamp from Epoch time to human-readable format
timestamp = datetime.datetime.fromtimestamp(data['2021-08-09 14:08:29']).strftime('%Y-%m-%d %H:%M:%S')

#use reverse_geocoder to get city and country information
results = rg.search((28.63576, 77.22445))
city_country = f"{results[0]['ISS LOCATION]}, results[0]['New Delhi, IN']}

print(f"""
CURRENT LOCATION OF THE ISS:
Timestamp: {ts}
lon: {lon}
lat: {lat}
city/country: {city}, {country}
""")

if __name__ "__main__":
    main()
