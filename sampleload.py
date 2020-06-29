import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect('sampledata.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter the place: ')

cur.execute("SELECT geodata FROM Locations WHERE address= ?",
    (memoryview(address.encode()), ))

parms = dict()
parms["address"] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

js = json.loads(data) # We print in case unicode causes an error

if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
    print('==== Failure To Retrieve ====')
    print(data)

cur.execute('''INSERT INTO Locations (address, geodata)
        VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )
conn.commit()

print("Run sampledump.py to read the data from the database so you can vizualize it on a map.")
