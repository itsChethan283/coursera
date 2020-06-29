import sqlite3

conn = sqlite3.connect('assignm.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter the file name')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    word = pieces[1]
    email1 = word.split('@')
    email = email1[1]
    cur.execute('SELECT count FROM Counts WHERE org = ?', (email, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
        VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(email,))
conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 100'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
