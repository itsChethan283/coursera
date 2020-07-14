from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import sqlite3
import re



url = "https://www.tnagrisnet.tn.gov.in/Contact.php"
document = urllib.request.urlopen(url, None)
text = document.read().decode()

print(text)
