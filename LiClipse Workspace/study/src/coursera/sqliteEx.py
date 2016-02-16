import re
import sqlite3
import urllib


conn = sqlite3.connect('C:\Users\Marcel\Documents\Ferramentas\SQLiteDatabaseBrowserPortable\Data\mooc.sqlite')
cur = conn.cursor()

cur.execute('''
    DROP TABLE IF EXISTS Counts
''')

cur.execute('''
    CREATE TABLE Counts ("count", "org")
''')

fileHandle = urllib.urlopen("http://www.pythonlearn.com/code/mbox.txt")

for line in fileHandle:
    
    if not line.startswith('From: ') :
        continue
    
    email = line.rstrip().split()[1]
    email = email.split('@')[1].strip()
    
    
    row = cur.execute('SELECT count FROM Counts WHERE org = ?', (email, ) )
    
    try:
        count = row.fetchone()
        if count is None:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (email,) )
        else:            
            cur.execute('UPDATE Counts SET count = count+1 WHERE org = ?', (email,) )        
    except:
        print 'Error'
    
conn.commit()

for row in cur.execute('SELECT count, org FROM Counts ORDER BY count DESC LIMIT 100'):
    print str( row[1] ), row[0]