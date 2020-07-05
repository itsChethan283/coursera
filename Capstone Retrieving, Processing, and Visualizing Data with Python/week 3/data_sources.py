from bs4 import BeautifulSoup
from urllib.request import urlopen
import sqlite3
import re

conn = sqlite3.connect("courses.sqlite")
cur = conn.cursor()
cur.executescript('''
    DROP TABLE IF EXISTS Course;

    CREATE TABLE Course(
    Name TEXT,
    Partner TEXT,
    Learning_Product TEXT,
    Level TEXT,
    Students INTEGER,
    Rating INTEGER,
    Reviews INTEGER
        )
''')

url = "https://www.coursera.org/search?query=python"
fopen = urlopen(url)
html = fopen.read()
fopen.close()

soup = BeautifulSoup(html, "html.parser")

nameu = soup.findAll("li", {"class": "ais-InfiniteHits-item"})

for row in range(len(nameu)):
    name = nameu[row].div.h2.text
    partner = nameu[row].div.span.text
    learning = nameu[row].findAll("div", {"class": "_jen3vs _1d8rgfy3"})
    lear = learning[0].text
    level = nameu[row].findAll("span", {"class": "difficulty"})
    lev = level[0].text
    stud = nameu[row].findAll("span", {"class": "enrollment-number"})
    students = stud[0].text
    if students[3] == "m":
        m = students[0:3]
        q = float(m) * 10**6
    if students[3] == "k":
        m = students[0:3]
        q = float(m) * 10**3
    rating = nameu[row].findAll("span", {"class": "ratings-text"})
    rate = rating[0].text
    reviews = nameu[row].findAll("span", {"class": "ratings-count"})
    rw = reviews[0].text
    r = rw[1:len(rw)-1]

    cur.execute(''' INSERT INTO Course (Name, Partner, Learning_Product, Level, Students, Rating, Reviews)
    VALUES (?, ?, ?, ?, ?, ?, ?)''', (name, partner, lear, lev, q, rate, r))
conn.commit()
