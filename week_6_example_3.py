import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrived', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if js is None or 'status' not in js or js['status'] != 'OK' :
        print('=====Fail=====')
        print(data)
        continue
    lat = js["results"]["geometry"]["location"]["lat"]
    lng = js["results"]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results']['formatted_address']
    print(location)
