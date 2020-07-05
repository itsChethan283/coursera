import sqlite3

conn = sqlite3.connect('courses.sqlite')
cur = conn.cursor()

cur.execute('''SELECT * FROM Course ORDER BY Students DESC''')
print("Creating JSON output on spider.js...")
fhand = open('courses.js', 'w')
l = list()

for row in cur :
    l.append(row)
    print(row[4])
