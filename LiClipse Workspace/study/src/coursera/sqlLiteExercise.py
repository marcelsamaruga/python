import sqlite3

import xml.etree.ElementTree as ET


conn = sqlite3.connect('mooc.sqlite')
cur = conn.cursor()

cur.executescript('''

    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;

    CREATE TABLE Artist (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );
    
    CREATE TABLE Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );
    
    CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title   TEXT UNIQUE
    );
    
    CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY 
            AUTOINCREMENT UNIQUE,
        title TEXT  UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    );

''')


def lookup(node, key):
    found = False
    for child in node:
        if found:
            return child.text

        #tag Name is the name inside the tag value: eg <Key> == tag 'Key'
        if child.tag == 'key' and child.text == key:
            found = True

    return None


# reading XML file
url = 'Library.xml'
xmlFile = ET.parse(url)

allNodes = xmlFile.findall('dict/dict/dict')

for node in allNodes:
    if lookup(node, 'Track ID') is None:
        continue

    artist = lookup(node, 'Artist')
    album = lookup(node, 'Album')
    genre = lookup(node, 'Genre')
    
    name = lookup(node, 'Name')
    count = lookup(node, 'Track Count')
    len = lookup(node, 'Size')
    rating = lookup(node, 'Content Rating')
    
    if name is None or genre is None or artist is None or album is None:
        continue
    

    cur.execute('INSERT OR IGNORE INTO artist (name) VALUES (?)', (artist, ) )
    cur.execute('SELECT id FROM artist WHERE name = ?', (artist, ) )
    artistId = cur.fetchone()[0]
    
    cur.execute('INSERT OR IGNORE INTO genre (name) VALUES (?)', (genre, ) )
    cur.execute('SELECT id FROM genre WHERE name = ?', (genre, ) )
    print genre
    genreId = cur.fetchone()[0]

    cur.execute('INSERT OR REPLACE INTO album (title, artist_id) VALUES (?, ?)', ( album, artistId ) )
    cur.execute('SELECT id FROM album WHERE title = ?', (album, ) )
    albumId = cur.fetchone()[0]
    
    cur.execute('INSERT OR REPLACE INTO track (title, album_id, genre_id, len, count) VALUES (?, ?, ?, ?, ?)', ( album, albumId, genreId, len, count ) )

    print 'Album', albumId, album, ' - Artist ', artistId, artist


conn.commit()

