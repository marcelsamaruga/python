# https://docs.python.org/2.7/library/functions.html


print "hello world"

# check the type
x=5
print type(x)

# convert to float
print float(x)

# convert to int
print int(x)

# gets user input. Always returns string value
hours = raw_input('How many hours do you have?')
pay = float(hours) * 10
print 'You have ', pay, ' dollars'

print '\n'

# conditionals
salary = float(raw_input('Type your salary: '))
if salary <= 1000.0:
	print 'Low salary. No rates'

print '\n'

if salary > 1000.0 and salary <= 2000.0:
	print 'Medium salary. Rates is 10%'
	print 'New salary', salary * 0.9
elif salary > 2000:
	print 'High salary. Rates 15%'
	print 'New salary', salary * 0.85
	
print '\n'

print 'Equals is represented by signal == ', 1==1

print '\n'

# repetition
for i in range(10):
	if i % 2 == 0:
		print i, ' Even'
	else:
		print i, ' Odd'
		
print '\n'


# try / except
try:
	x = int( raw_input('Type an input number ') )
except:
	x = 0
	print 'Invalid Number'
	
print x

# functions

def breakLine():
	print '\n'
	
def breakLine2(value):
	print value, '\n'

def add(a, b):
	return a + b
	
breakLine()
breakLine2('bye')
print add(2, 4)

breakLine()

# loops
while True:
	line = raw_input('>')	
	if line == 'done' or line == '' :
		break		
	if line[0] == '#':
		continue		
	print line
	
breakLine()	

for i in range(5):
	print i
	
breakLine()
	
for i in [1,2,3,4,5]:
	print i

# STRINGS
breakLine()
breakLine()

# set of string values
# use is to equal None, True or False
for name in ['M','A','R','C','E','L']:
	if name is not None:
		print name, ' not None'
	print name
	
breakLine()

nome = 'Marcel'
print 'First letter',nome[0]
print 'Size:',len(nome)
print 'Substring string[initial : final (excluded) ]----->', nome[0:3]
print 'Check string whithin a string string1 in strin2: Ma in Marcel ----->', 'Ma' in nome
print 'lower and upper', nome.lower(), nome.upper() 
print 'Position find()', nome.find('M')
print 'Replace()', nome.replace('M', 'm')
print 'Trim strip()', nome.strip()
print 'title marcel samaruga da costa ----> ', 'marcel samaruga da costa'.title()
print ' split ', nome.split('M')[1]
print 'Others valuables functions: startswith, endswith, capitalize, splitlines, isdigit'

# https://docs.python.org/2/library/stdtypes.html#string-methods

breakLine()

for letter in nome:
	print letter
	

breakLine()
breakLine()

	
# FILES
# reading a simple file
file = open('file.txt')

for line in file:
	print line.rstrip() # rstrip replace new line

breakLine()

file = open('file.txt')
for line in file:
	if not 'Name' in line:
		continue
	print line.rstrip() # rstrip replace new line
	
breakLine()
	
# read all the content into a single variable
file = open('file.txt')
allContext = file.read()
print allContext