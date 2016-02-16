import new
def breakLine():
    print '\n'


# LISTS
lista = []
lista = [1, 1.2, 'Salary']
print lista[0]
print 'Size of the list', len(lista)

for item in lista:
    print item

breakLine()

for i in range(len(lista)):
    print lista[i]
    
breakLine()

print lista[0:2]
print lista[:2]
print lista[1:]
print lista[:]
#remover
del(lista[-1])

breakLine()

# advanced functions to deal with lists
#create empty list
newList = list()
# function of an object
print dir(newList)
newList.append("Marcel")
newList.append(2016)
print "Marcel" in newList
print not "Samaruga" in newList
print 2015 in newList

breakLine()

sortedList = []
sortedList = ['H','A','L','O','A']
sortedList.sort()
print sortedList

breakLine()

# create a new list copying from another one
newSortedList = list(sortedList)
# or 
newSortedList = sortedList[:]
# using equals it will copy the reference not the values

breakLine()

print 'Max ', max(sortedList)
print 'Min ', min(sortedList)
print 'Index ', sortedList.index('H', )
print 'Count (how many times repeat)', sortedList.count('A')

breakLine()

# DICTONATIRES / mapas
map = dict()
map['Name'] = 'Marcel'
map['Age'] = 31
map['Phone'] = 123123123
print map

breakLine()

map=[]
map = {'Name':'Marcel', 'Age': 31}
print map

breakLine()

map = dict()
for word in ['A', 'E', 'S', 'A', 'A', 'S']:
    if word not in map:
        print 'First time of', word
    map[word] = map.get(word, 0) + 1
    #get(value) retrieve the value of the key get(value, default) -> default is the default value if the key has not found

print map, 'A', map.get('A')
        
breakLine()

#loop into a map: shows the key and the value separated
for key in map:
    print 'Key:',key, 'Value:', map[key]
    
print map.keys()
print map.values()

for key,value in map.items():
    print 'Key:',key, 'Value:', value
    
# sorted list items by key value
for key,value in sorted(map.items()) :
    print 'Key:',key, 'Value:', value
    
breakLine()
    
# initiate list uses [], dict uses {}
lista = ['A', 'B', 'C']
dictonary = { 'A':1, 'B':2, 'C':3 }
print str(type(lista)) + " - " + str(type(dictonary))

breakLine()

#tuple are Immutable
#list of tuple
lista = []
lista.append( ('A',1) )
lista.append( ('B',2) )
print lista

breakLine()

lista = []
for (k,v) in map.items():
    lista.append( (k,v) )
    
# now lista it's key value list as well
for k,v in lista:
    print k,v

breakLine()
    
# print an ordened list by value
lista = list()
lista = { 'a':10, 'b':1, 'c':5, 'd':2 }
print sorted(  [ (v,k) for (k,v) in lista.items() ]  )

breakLine()

# common elements in a list
l1 = [1,2,3,4,5,6,7,8,9]
l2 = [1,3,5,7,9,10]
print set(l1) & set(l2) #set([1, 3, 9, 5, 7])

# remover duplicate elements
#E como remover de uma lista os elementos que existem em outra:
print set(l1)-set(l2) # set([10])
print set(l2)-set(l1) #set([10])

breakLine()

# test all the possibilities
import itertools
for i in itertools.permutations('abc'):
    print ''.join(i) #abc, acb, bac, bca, cab, cba

for i in itertools.combinations('abc',2):
    print ''.join(i) #ab, ac, bc
