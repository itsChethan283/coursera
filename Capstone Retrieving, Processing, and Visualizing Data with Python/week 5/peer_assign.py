import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.tnagrisnet.tn.gov.in/Contact.php"
op = urlopen(url)
text = op.read()
#print(text)
html = op.read()
soup = BeautifulSoup(html.content, 'html.parser')

tabel = soup.findAll("table", {"id": "DataTables_Table_1"})
#print(BeautifulSoup.prettify(tabel))

print(tabel[0].td.text)
