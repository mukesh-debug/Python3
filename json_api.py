#!/usr/bin/env python3
import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'
found = []
while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break
    url = serviceurl + urllib.parse.urlencode({"key" : 42, "address" : address})
    print('Retrieving ', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved ', len(data), 'characters')
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('-'*50)
        print('Failed To Retrieve for key=', key)
        continue
    
    #print(json.dumps(js, indent=4))
    print("Place id: ", js["results"][0]["place_id"])
