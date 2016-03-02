def breakLine():
    print '\n'


# regular expression
import re
# ^ starts with
# . any character
# ? regularly re finds until the last possibility. Using ? stops in the first time that have found
# [0-9]
# \S any non-spacing character
# + one or more times
# * none or more times 

# ^    Matches the beginning of a line
# $    Matches the end of the line
# .    Matches any character
# \s    Matches whitespace
# \S    Matches any non-whitespace character
# *    Repeats a character zero or more times
# *?    Repeats a character zero or more times (non-greedy)
# +    Repeats a character one or more times
# +?    Repeats a character one or more times (non-greedy)
# [aeiou]    Matches a single character in the listed set
# [^XYZ]    Matches a single character not in the listed set
# [a-z0-9]    The set of characters can include a range
# (    Indicates where string extraction is to start
# )    Indicates where string extraction is to end

# [^] ^ within [] it means NOT (negative)


#search returns true or false
if re.search('M', 'Marcel'):
    print 'True'  #true
if re.search('^From:', 'From:marcelsamaruga@gmail.com'):
    print 'True' #true

# find all return a list of character if pattern matches
print re.findall('^F.+:', 'From:marcelsamaruga@gmail.com') # From
print re.findall('^F\S+:', 'From:marcelsamaruga@gmail.com') # From
print re.findall('[0-9]', '09/01/2016') # 09
print re.findall('[0-9]+', '09/01/2016') # 09,01,2016
print re.findall('[0-9]+?', '09/01/2016') # 0,9,0,1,2,0,1,6
print re.findall('^F.+?:', 'From: Using the : character') #From:
print re.findall('^F.+:', 'From: Using the : character') #From: Using the :

# extract domain from an email
print re.findall('^From: .*@(\S[^.]+)', 'From: marcelsamaruga@gmail.com') #gmail
# RE: begins with From: finds until @, extract any non-spacing character one or more times that is not dot(.)

print re.findall('([0-9.]+)', 'Value is 0.98765') #0.98765
# RE: begins with Value and extract numbers and dot

breakLine()

# assignment. Sum all the numbers in the file
print sum( [int(value) for value in re.findall( '([0-9]+)', open('assignment.txt').read() ) ] )

breakLine() 

# url

import urllib
file = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in file:
    print line.strip()


import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data;

mysock.close()


#using BeautifulSoup 
from BeautifulSoup import *

url = "http://python-data.dr-chuck.net/comments_221001.html"
# opens url
html = urllib.urlopen(url).read()
#load the lib
soup = BeautifulSoup(html)

# get all the <a>
for tag in soup('a'):
    # retrieve href 
    print tag.get('href')
    #print 'Contents:',tag.contents[0]
    print 'Attrs:',tag.attrs
    
    
breakLine()    
  
    
url = "http://python-data.dr-chuck.net/comments_221001.html"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

sumValue = 0

for tag in soup('span'):
    # get the value inside the tag
    sumValue = sumValue + int(tag.contents[0])
    
print sumValue


breakLine()


breaker= 1
countOut = 0
newUrl = None

while True:
    
    if newUrl is None:
        url = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Precious.html"
    else:
        url = newUrl
        
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    
    count = 0

    for tag in soup('a'):
        count = count + 1
    
        if int(count) == 18:
            countOut = countOut + 1
            newUrl = tag.get('href')
            print newUrl
            break
                    
    if countOut == breaker:
        break
    

breakLine()

#XML
import xml.etree.ElementTree as ET

# using triple quotes gives the String that it's possible to break the lines
data = '''
    <person>
        <name>Marcel Samaruga</name>
        <phone type="intl">
            +55 21 89723423
        </phone>
        <email hide="no">marcelsamaruga@gmail.com</email>
    </person>
'''

tree = ET.fromstring( data )
print 'Name in the XML node', tree.find('name').text
print 'Should hide the email', tree.find('email').get('hide')


data = '''<persons>
        <person id="1">
            <name>Marcel Samaruga</name>
            <phone type="intl">
                +55 21 89723423
            </phone>
            <email hide="no">marcelsamaruga@gmail.com</email>
        </person>
        
        <person id="2">
            <name>Costa</name>
            <phone type="intl">
                +55 21 009
            </phone>
            <email hide="no">marcelsamaruga@yahooo.com</email>
        </person>
    </persons>
'''
print data
tree = ET.fromstring( data )
listOfNodes = tree.findall('person')

breakLine()

print 'Size of the list of person', len(listOfNodes)

for node in listOfNodes:
    print node.find('name').text + " - " + node.find('email').text
    print node.find('phone').get('type')
    print node.get('id')
    
breakLine()

value = 0
commentInfoTree = ET.fromstring( urllib.urlopen('http://python-data.dr-chuck.net/comments_220998.xml').read() )
for node in commentInfoTree.findall('comments/comment'):
    value = value + int( node.find('count').text )
print value

breakLine()

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)


    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print 'lat',lat,'lng',lng
    print location
    
    
    
    
# JSON
# in json the data is represented by {}
# and the list is represented by []
data = '''
    {
        "name": "Marcel",
        "phone": {
            "type":"int",
            "number":"0111406"
        },
        "email": {
            "hide":"yes"
        }
    }
'''

import json
jsonPerson = json.loads( data )
print jsonPerson["name"]
print jsonPerson["phone"]["number"]
    
breakLine()

list = '''
        [
            {
                "id": "1",
                "name":"Marcel"
            }, 
            {
                "id": "2",
                "name":"Costa"
            }        
        ]
'''
    
jsonList = json.loads(list)
for value in jsonList:
    print value["id"], value["name"]
    
breakLine()


# to transform json object into a string object use the dumps method
json_string = json.dumps( jsonList )
print 'Json String \n', json_string

breakLine()

# to serializa the json file use the cPickle library
import cPickle
pickled_string = cPickle.dumps([1, 2, 3, "a", "b", "c"])
print cPickle.loads(pickled_string)

breakLine()



while True:
    location = raw_input("Location:")
    if len(location) < 1:
        break;
    
    mapUrl = "http://maps.googleapis.com/maps/api/geocode/json?"
    mapUrl = mapUrl + urllib.urlencode({
                                        'sensor': 'false',
                                        'address': location
                                       })
    
    jsonReturn = urllib.urlopen( mapUrl ).read()
    
    try:
        jsonMap = json.loads( jsonReturn )
        
        if 'status' not in jsonMap or jsonMap['status'].upper() != 'OK':
            print 'Error. Try again...'
            continue
        
        firstResult = jsonMap['results'][0]
        print firstResult['place_id']
        print firstResult['formatted_address']
        print firstResult['address_component'][3]['short_name']
        print firstResult['geometry']['bounds']['northeast']['lat'] + firstResult['geometry']['bounds']['northeast']['lng']
        print firstResult['geometry']['bounds']['southwest']['lat'] + firstResult['geometry']['bounds']['southwest']['lng']
        
        
    except:
        print 'Error. Try again...'
        
    #print jsonReturn
    
    
    
#
url = raw_input('Url:')

if len(url) < 1:
    url = 'http://python-data.dr-chuck.net/comments_221002.json'
    
data = urllib.urlopen( url ).read()

try:
    jsonReturn = json.loads(data)    
    
    total = 0

    for item in jsonReturn['comments']:
        total = total + int( item['count'] )

    print 'Total', total
    
except:
    print 'Error reading JSON file'

