'''

Usefull tool to download libs: Conda

installing package: use the newer Python version 3.4 or higher . 
Download get-pip.py 
Go to the prompt and type
python get-pip.py


After installing
prompt and type

- Upgrade pip
python -m pip install -U pip

- Installing a package
r
numpy is the desired package  

- From PyPi
pip install 'SomeProject>=1,<2'
e.g.: python -m pip install -U matplotlib
python -m pip install matplotlib
python -m pip install scikit

- From VCS
pip install -e git+https://git.repo/some_pkg.git#egg=SomeProject


Numpy so funcionou atraves do executavel 1.9.2 do SourceForge


scipy
scikit
matplotlib
pandas

@author: Marcel


NOTA IMPORTANTE
Só consegui utilizar o Numpy e Matplotlib atraves de um instalador chamado Anaconda
Add como um novo interprete Python
 
'''

import numpy as np

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])

z = x + y
print(z)

print("\n")

x = np.array( [ [1,2,3,4,5], [6,7,8,9,0] ] )
print( x[0][0] ) # print 1
print( x[0 , 4] ) # print 5 
print( x[ : , 1] ) # the second element of all rows: [2,7]
print( x[ : , 1:4 ] ) # second, third and fourth elements of all rows: [ [2,3,4], [7,8,9] ]
print( x[ 1 , 1:3 ] ) # second and third elements of the second row: [7,8]  

print("\n")

# simulating big array with numpy
# using np.random.normal where 1 param: mean, 2 param: standart dev., 3 param: number of samples
height = np.round( np.random.normal( 1.75, 0.2, 5000 ), 2 )
weight = np.round( np.random.normal( 75, 0.4, 5000 ), 2 )

# stick both array together
population = np.column_stack( (height, weight) )
#total_weight = population.sum(:,0)

print( population[:5] )
print("\n")

# sum is faster than Python sum function
print( 'Sum:', np.sum(population[ : , 0 ]) )
# average from the weight of the population
print( 'Average:', np.mean( population[:, 1] ) )
print( 'Medium:', np.median( population[:, 1] ) )
print( 'Deviation (sum of the distance between the difference of the mean and the array list:', np.std( population[:, 1] ) )
print( 'Correlation:', np.corrcoef( population[:, 0], population[:, 1] ) )

print("\n")

height = np.array( [182, 187, 197, 158,  189, 179] )
classification = np.array( ['A', 'B', 'C', 'C',  'A', 'A'] )
npCondition = height[ classification == 'A' ]
print(npCondition)


print('\n')
