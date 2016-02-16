class Person:
    age = 0
    name  = ''
    
    # constructor. Not necessary        
    def __init__(self, name):
        self.name = name
        
    # destructor. Not necessary
    def __del__(self):
        print 'Calling the destructor'
    
    def party(self):
        self.age = self.age + 1
        
    def counter(self):
        print self.age
    
    def namer(self):
        print self.name
        

me = Person('Marcel')
me.party()
me.party()
me.counter()
me.namer()

print dir(me) #age, counter, party
print type(me) #instance

print '\n'
# ---------------------------------------

#inherance
class Developer(Person):
    programmingLanguage = ''
    
    def setProgramminLanguage(self, language):
        self.programmingLanguage = language
        
    def getProgrammingLanguage(self):
        print 'Your programming language is', self.programmingLanguage


developer = Developer('Marcel')
developer.setProgramminLanguage('Python')
developer.namer()
developer.getProgrammingLanguage()

print '\n'
# ---------------------------------------


print '\n'
# ---------------------------------------
