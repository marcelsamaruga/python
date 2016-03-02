# https://docs.python.org/2.7/library/functions.html


print "hello world"

# check the type
x=5
print type(x)

# convert to float
print float(x)

# convert to int
print int(x)
print help(int)


# gets user input. Always returns string value
hours = raw_input('How many hours do you have?')
pay = float(hours) * 10
print 'You have ', pay, ' dollars'
print '\n'

print round(1.65)
print round(1.65, 2)
print round(1.65, 3)
print round(1.65678, 3)

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
    
# all the list of exceptions https://docs.python.org/2/tutorial/errors.html#handling-exceptions
try:
    txtFile= open('c:\texto_nao_existe.txt')
except IOError:
    print("Such file doesn't exist")
except ValueError:
    print "Could not convert data to an integer."
    # throw new exception
    raise IOError

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
print 'Position index()', nome.index('Mar')
print 'Replace()', nome.replace('M', 'm')
print 'Trim strip()', nome.strip()
print 'title marcel samaruga da costa ----> ', 'marcel samaruga da costa'.title()
print ' split ', nome.split('M')[1]
print ' split ', 'Marcel Samaruga da Costa'.split()[1]
print 'Comparison a > b and a > A', ('a' > 'b'), ('a' > 'A') 
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

breakLine()


# function using overload parameters
# the default value will always be used and concatenated with the value sent in the invoke
def addr(domain='/', path='/', querystring='?', hash='/'):
    return 'http://%s%s%s%s' % (domain,path,querystring,hash)

print addr('tableless.com.br')
print addr('tableless.com.br','code/css')
print addr('tableless.com.br','code/css','parameter=1')
# invoke a parameter in the middle of the function
print addr('tableless.com.br', querystring='s=python')


breakLine()

def testVarArgs(first, second, *all):
    print first
    print second
    print list(all)

testVarArgs(1, 2, 3, 4, 5, 6, 7)    


breakLine()

# the last parameter indicates some kind of map. So it's possible to use the get function whenever parameter value used
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print "The sum is: %d" % (first + second + third)

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print "Result: %d" % result

breakLine()

# var args
# invoke the function and send none or ilimited parameters in the end
def div(content, **attributes):
    html="<div"
    
    for attribute in attributes.iteritems():
        html+=' %s="%s"' % attribute
        
    html+=">"+content+"</div>"
    return html

print div("Hello")
print div("Hello",id="blue")
print div("Hello",id="blue",contenteditable="true",title="Edite como quiser.")


#
import random
l = [ random.randint(0, 100) for i in range(20) ]
print l
print 'First', l[0] # Primeiro elemento
print 'Last', l[-1]
print 'Before Last', l[-2]
print 'First 5 ', l[0:5] # Primeiros cinco elementos
print 'First 5 ', l[:5] # Primeiros cinco elementos
print 'Last 5', l[-5:] #Ultimos 5 elementos
print 'First 5 in back order', l[4::-1] # primeiros 5 de tras para frente

l="abcdefghijklmnopqrstuvwxyz"
print l[1] # Segundo elemento
print l[:5] # Primeiros cinco elementos
print l[-5:] # primeros cincos elementos
print l[4::-1] # primeiros 5 de tras para frente


# formatting numbers
print('The order total comes to %.2f' % 123.4494444) # 123.45