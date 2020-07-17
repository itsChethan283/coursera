import sqlite3
import ssl
import urllib.request, urllib.parse, urllib.error
from urllib.parse import urljoin
from urllib.parse import urlparse
import re
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('content.sqlite')
cur = conn.cursor()

baseurl = "https://engineering.careers360.com/articles/tnea-cutoff"

cur.execute('''CREATE TABLE IF NOT EXISTS Messages
    (id INTEGER UNIQUE,district TEXT, email TEXT, designation TEXT, mobile INTEGER UNIQUE)''')

url = baseurl 

text = "None"

# Open with a timeout of 30 seconds
document = urllib.request.urlopen(url)
text = document.read()
  
html = BeautifulSoup(text, "html.parser")
#print(html)
tabel = html.findAll("div", {"class": "story-responsive"})
#tab = html.findAll("p", {"dir": "ltr"})
#print(tab)
#len(tab)
#print(len(tabel))
#print(tabel[2])
ta = BeautifulSoup.prettify(tabel[2])
m = re.findall("^<p [.+]>(.*)", ta)
print(m)
#print(ta)
print(len(tabel[2].td))
x = tabel[2].table.td.text
print(x)
#print(text)
    
print(url,len(text))

    

