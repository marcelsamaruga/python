import pandas
import numpy
import matplotlib.pyplot as plt
from ggplot.geoms.geom_line import geom_line

# read csv file
try:
    _data = pandas.read_csv("file.csv")
except:
    print('Error reading')

# writing csv file
try:
    _data.to_csv("new_file.csv")
except:
    print('Error writing')

# create randomly DataFrame 10 rows and 4 columns
data = pandas.DataFrame( numpy.random.randn( 10, 4 ) )

# rename columns in the file
data.rename(columns = lambda x: str(x).replace(' ', '_').lower(), inplace=True)

########################
# MERGING

# cutting the dataframe into pieces
dataCut = [ data[:2], data[8:] ]
print( '\n', dataCut )

# merging
left  = pandas.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pandas.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
joint = pandas.merge(left, right, on='key')
print( '\n', joint )

# append on the dataframe
data  = pandas.DataFrame( numpy.random.randn( 10, 4 ), columns=['A', 'B', 'C', 'D'] )
data2 = pandas.DataFrame( numpy.random.randn( 6, 4 ),  columns=['A', 'B', 'C', 'D'] )

data3 = data.append(data2, ignore_index=True)
print( '\n', data3.head() )

############
df = pandas.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                       'B' : ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                       'C' : numpy.random.randn(8),
                       'D' : numpy.random.randn(8)
                       })

print( '\n', df.groupby('A').sum() )
print( '\n', df.groupby(['A', 'B']).sum() )

###########

# The stack function “compresses” a level in the DataFrame’s columns.
print( '\nStack\n', df.stack() )
print( '\nStack\n', df.unstack() )


############
# categorize
data = pandas.DataFrame({ 'date':[1,5,40,1236,1456,1872,2016], 'id_category':[1,2,3,4,1,1,4] })
data['category_description'] = data['id_category'].astype('category')
data['category_description'].cat.categories = ['Ancient Times', 'Medieval Times', 'Old Times', 'Recent Times']
print( '\n', data.sort_values(by='category_description') )
print( '\nCount', data.groupby('category_description').size() )
print( '\nUnique Elements', data.id_category.unique() )

# print the row/columns in a tuple element 
print( '\nShape (row/column)', data.shape )

###########
ts = pandas.Series(numpy.random.randn(1000), index=pandas.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
df = pandas.DataFrame(numpy.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
#plt.figure() 
df.plot()
plt.legend(loc='best')
plt.show()



############# 
# Microsoft Excel
df.to_excel('foo.xlsx', sheet_name='Sheet_1')

#############

# t-test means if two set of lists are significantly comparable. In other words, it tests the null hypothesis 

print('\n')

#dates = [datetime(2012, 5, 1), datetime(2012, 5, 2), datetime(2012, 5, 3)]
data = pandas.read_csv('baseball_stats.csv', low_memory=False)
lHanded = data[ data['handedness'] == 'L' ]
rHanded = data[ data['handedness'] == 'R' ]

from scipy import stats

dataTTest = stats.ttest_ind( lHanded['avg'].dropna(), rHanded['avg'].dropna() , equal_var=False)
print( '\nP_Value:' , dataTTest[1] )

pValue = dataTTest[1]

if (float(pValue) < 0.05):
    print('Alternative Hypothesis Accepted')
else:
    print('Null Hypothesis Rejected')
    

################

# E= (value-AVG(value))²
SST = numpy.sum( (lHanded['avg'].dropna() - numpy.mean(lHanded['avg'].dropna())) ** 2 )
print( 'Math with numpy', SST )





#################
# conda install -c https://conda.binstar.org/bokeh ggplot
# pip install ggplot
from ggplot import *

data = pandas.DataFrame( {'Winning':numpy.random.randn(10)*6+30, 'Year':[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]} )
print(data)

#geom_line() draws the line chart
plot = ggplot (data, aes(x='Year', y='Winning')) + geom_point() + geom_line()
print(plot)

# loess line indicates long term trend
plot = ggplot (data, aes(x='Year', y='Winning')) + geom_point() + geom_line()
print(plot)



################
import logging
logging.info('Info message for log')