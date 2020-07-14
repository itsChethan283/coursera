import sqlite3
from urllib.request import urlopen
from bs4 import BeautifulSoup

conn = sqlite3.connect("Email.sqlite")
cur = conn.cursor()

url = "https://www.tnagrisnet.tn.gov.in/Contact.php"

opener = urlopen(url)
html = opener.read()
opener.close()

soup = BeautifulSoup(html, "html.parser")

tag = soup.findAll("div", {"class":"dataTables_paginate paging_simple_numbers"})
print(tag)
