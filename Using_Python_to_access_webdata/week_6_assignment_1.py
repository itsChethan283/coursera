import urllib.request, urllib.parse, urllib.error
import json

while True:

    address = input("Enter location: ")
    if len(address) < 1 : break

    print("Retrieving", address)
    uh = urllib.request.urlopen(address)
    data = uh.read().decode()
    print("Retrived", len(data), "characters")
    js = json.loads(data)

    print("count:", len(js["comments"]))
    sum = 0

    for item in js['comments']:
        sum = sum + int(item['count'])
    print("sum:",sum)
