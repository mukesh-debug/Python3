#!/usr/bin/env python3
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    #Breaking condition - when user doesn't enter address
    if len(address) < 1:
        break
    url = serviceurl + urllib.parse.urlencode({'address': address})
    # here address needs to be converted in the form like
    # 'address=Ann+Arbor%2C+MI' when address given is 'Ann Arbor, MI, USA'

    print('Retrieving data from :', url)

    urlhandle = urllib.request.urlopen(url)  # To request data
    data = urlhandle.read().decode()  # Receive data as stream and decode from utf-8
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)  # Convert json to python data structures: list, dict
    except:
        js = None

    # If js is None or incomplete retrieval due to any reason 
    # To avoid errors while accessing data from json object
    if not js or 'status' not in js or js['status'] != 'OK':
        print('----Failure To Retrieve JSON----')
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("latitude: ", lat)
    print("longitude: ", lng)
