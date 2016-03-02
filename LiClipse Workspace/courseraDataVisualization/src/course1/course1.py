# to install new package: after installing Anaconde
# go to the Andaconda prompt control and type conda install PACKAGE
# to update a package type conda update PACKAGE

import pandas
import numpy


pandas.set_option( 'display.float_format', lambda x: '%f' %x )
#pandas.set_option( 'display.max_columns', None )
#pandas.set_option( 'display.max_rows', None )

data = pandas.read_csv( 'nesarc_pds.csv', low_memory=False )


print( len(data) )
print( len(data.columns) )

print('\n')

# value_counts group the value by the category
c1 = data['TAB12MDX'].value_counts(sort=False)
print (c1)

print('\n')

# it's recommended to convert the data into the desired TYPE
#data['TAB12MDX'] = pandas.to_numeric( data['TAB12MDX'] )
c1 = data['TAB12MDX'].value_counts(sort=False)
print(c1) 

# to convert the values into percentual, use the parameter normalized = True
c1 = data['TAB12MDX'].value_counts(sort=False, normalize=True)
print(c1) 


print('\nGroup by')

# groupby: group by according to the column
group1 = data.groupby('TAB12MDX')
print( group1.size() )
print( group1.size() * 100 / len(data) )

print('\n')

print('\n')
print('\n')


print('counts for S3AQ3B1')
c3 = data['S3AQ3B1'].value_counts(sort=False)
print(c3)
# the parameter dropna remove the NA (not available) values
c3 = data['S3AQ3B1'].value_counts(sort=False, dropna=True)
print(c3)


print('\n')

print('percentages for S3AQ3C1')

# check difference bwtween the next 2 prints using the convert pandas function
p4 = data['S3AQ3C1'].value_counts(sort=False, normalize=True)
print (p4)

data['S3AQ3C1'] = data['S3AQ3C1'].convert_objects( convert_numeric=True )
p4 = data['S3AQ3C1'].value_counts(sort=False, normalize=True)
print (p4)

print('\n')

# ##################
# subset the data
sub1 = data[ (data['REGION'] == 4) & (data['CYEAR'] >= 2001) ]
print( sub1['TAB12MDX'].value_counts( sort=False ) ) 

# copy a set using pandas
sub2 = sub1.copy()

print('\n')

# let all the columns in uppercase
data.columns = map( str.upper, data.columns )


print('Week2...\n')

# in the research, the variable S3AQ3B1 has value 9 from Unknown
# the function below replace the value 9 (unknown) to numpy.nan
sub1['S3AQ3B1'] = sub1['S3AQ3B1'].replace( 9, numpy.nan )

# replace using more than one values in the replace statement
# sub1['S3AQ3B1'] = sub1['S3AQ3B1'].replace( [9,9,9,9], numpy.nan )
varS3AQ3B1 = sub1['S3AQ3B1'].value_counts( sort=False )
print(varS3AQ3B1) # by default doesnt show nan values

varS3AQ3B1 = sub1['S3AQ3B1'].value_counts( sort=False, dropna=False )
print(varS3AQ3B1)

# if column1 has a value that doesnt necessary to answer the next question
# Question 1: Did you smoke in the last 12 months -> S2AQ3
# 1: Yes - 2: No - 9: Unknown
# Question 2: How often did you smoke in the last 12 months -> S2AQ8A

# in this case, replace the condition to a new value 
sub2.loc[ (sub2['S2AQ3'] != 9) & (sub2['S2AQ8A'].isnull()) , 'S2AQ8A' ] = 11
print('\nLocate')
print( sub2['S2AQ3'] )
print( sub2[['S2AQ8A']] )  

print('\n\n')

# creating a new column to interpret values from the dictionary used in the codebook
#recoding values for S3AQ3B1 into a new variable, USFREQ
# 1: Everyday
# 2: 5 to 6 days a week
# 3: 3 to 4 days a week
# 4: 1 to 2 days a week
# 5: 2 to 3 days a month
# 6: once a month
recode1 = {1.0: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1, None:9}
sub2['USFREQ']= sub2['S3AQ3B1'].map(recode1)

#recoding values for S3AQ3B1 into a new variable, USFREQMO
recode2 = {1: 30, 2: 22, 3: 14, 4: 5, 5: 2.5, 6: 1}
sub2['USFREQMO']= sub2['S3AQ3B1'].map(recode2)

# information about the columns
print('\n')
ds2= sub2["S2AQ8A"].describe()
print(ds2)


print('\n\nQcut')

# quartiles (split the values into new variable. This new variable indicates that age is divided in 4 groups (quarter) with percentiles )
sub2['AGE_GROUP'] = pandas.qcut( sub2.AGE, 4, ['1=25%tile', '2=50%tile', '3=75%tile', '4=100%tile'] )
print( sub2[['AGE']].head(25) )
print( sub2[['AGE_GROUP']].head(25) )


print('\n\nCut and crosstab function')

# to customize the new group use the panda cut Function. Remembering starts at zero (0)
# in the case below we are creating groups: 0-18, 18-21, 21-23, 23-25 (st
sub2['AGE_GROUP2'] = pandas.cut( sub2.AGE , [ 17, 20, 22, 25 ] )
# the crosstab functions shows the relationship between 2 variables
print( pandas.crosstab( sub2['AGE_GROUP2'], sub2['AGE'] ) )



##################################
# ploting
import seaborn
import matplotlib.pyplot as plt

# indicates the variable as type categorial variable to plot
sub2['TAB12MDX'] = sub2['TAB12MDX'].astype('category')

seaborn.countplot( x='TAB12MDX', data=sub2 )
plt.title('Nicotine dependence in the past 12 months among young adults smokers in the NESARC study')
plt.xlabel('Nicotine dependence in the past 12 months')
plt.show()

# histogram: distribuiton plot

# define by lamba function
def NUMCIGMO_EST(row):
    if (row['S3AQ3B1'] is None or row['S3AQ3B1'] == ''):
        return 0
    
    # S3AQ3B1: Everyday
    elif (row['S3AQ3B1'] == '1'):
        return 30 * row['S3AQ3C1']
    
    # S3AQ3B1: 5/6 per week
    elif (row['S3AQ3B1'] == '2'):
        return 22 * row['S3AQ3C1']
    
    # S3AQ3B1: 3/4 per week
    elif (row['S3AQ3B1'] == '3'):
        return 18 * row['S3AQ3C1']

    # S3AQ3B1: 1/2 per week
    elif (row['S3AQ3B1'] == '4'):
        return 14 * row['S3AQ3C1']
    
    # S3AQ3B1: 2/3 per month
    elif (row['S3AQ3B1'] == '5'):
        return 3 * row['S3AQ3C1']
    
    # S3AQ3B1: 1 per month
    elif (row['S3AQ3B1'] == '6'):
        return 1 * row['S3AQ3C1']
    
    # S3AQ3B1: 1 per month
    else:
        return 0
    
print('\nHistogram')
sub2['NUMCIGMO_EST'] = sub2.apply( lambda row: NUMCIGMO_EST(row), axis=1 )
seaborn.distplot( sub2['NUMCIGMO_EST'].dropna(), kde=False )
plt.title('Estimated numbers of cigarettes among young adults smokers in the NESARC study')
plt.xlabel('Numbers of cigarettes')
plt.show()

print('\nDescribe')

# 3 measures: mean, medium and mode
# mean: the sum of the values divided of the quantity
# medium: the middle of the list in ascending order. If the list has even numbers of items, sum the two in the middle and divide by 2
# mode: is the most frequent value in the List
# e.g.: 2, 3, 3, 3, 12, 13
# mean: (2 + 3 + 3 + 3 + 12 + 13)/6 -> 36/6 -> 6
# medium: (3+3)/2 -> 3 . If the list is 2, 4, 6 the medium is 4
# mode: 3

# python has the describe function to give statistical informations about a list of Values
describeTAB12MDX = sub2['NUMCIGMO_EST'].describe()
print( describeTAB12MDX )

# describe has different informations if the type of the variable is numerical or categorical
print( sub2['TAB12MDX'].describe() ) 

# the appropriate use of the graphs is:
# for quantitative variable, use histogram and measures (medium, mean, mode, etc)
# categorical variables use BarChart and Frequency Distributions


# the appropriate type of graph to use between two variables 
# In this case there will be a exploratory variable and the response variable
# The exploratory variable is independent and the response variable is dependent
# To investigate if the smoking cigarette causes nicotine dependency: the exploratory variable is the cigarette and the response is the nicotine dependence
# Check the Graphing_Flowchart_for_Printing.png file for more information about the type of graph to draw

# the bar char graph can have three types: 
# modal: there is a peak in the middle of the graph ..|..
# bimodal: there are two peaks in the graph ..|..|.. 
# linear: all the columns are similar ||||||

# how many packs per months. One pack has 20 cigars
sub2['PACKSPERMONTH'] = sub2['NUMCIGMO_EST'] / 20
print( sub2.groupby('PACKSPERMONTH').size() )

# types of pack
# 1-5 per month
# 6-10 per month
# 11-20 per month
# 21-30 per month
# 30+ per month

sub2['PACKCATEGORY'] = pandas.cut( sub2.PACKSPERMONTH, [0, 5, 10, 20, 30, 999] )
sub2['PACKCATEGORY'] = sub2['PACKCATEGORY'].astype( 'category' )

print('\n\nPack Category')
print( sub2['PACKCATEGORY'].describe() )
print( sub2['PACKCATEGORY'].value_counts( dropna=True, sort=False ) )

print('\n\nPrinting bar chart ')
# in order to print in bar chart graph, replace the TAB12MDX to numeric: where 1 is nicotine dependent and 0 is nicotine independent  
#sub2['TAB12MDX'] = sub2['TAB12MDX'].convert_objects( convert_numeric=True )
sub2['TAB12MDX'] = pandas.to_numeric( sub2['TAB12MDX'] )

seaborn.factorplot( x="PACKCATEGORY", y="TAB12MDX", data=sub2, kind='bar', ci=None )
plt.title('Indicates that more dependents in nicotine more the people smokes')
plt.xlabel('Packs per month')
plt.ylabel('Proportion nicotine dependence')
plt.plot()
plt.show()


# creating plot between 2 categorical Variable
# creating new group:
# 1- Nicotine Dependent
# 2- Daily Smokers
# 3- Non-daily Smokers

def GROUP_DEPENDENCE(row):
    # if the person smokes more than 10 packs per month, consider nicotine dependent
    if (row['PACKSPERMONTH'] > 10 ):
        return 1
    # daily smoker smokes more than 1 and less than 10 packs of cigarettes per day
    elif ( row['PACKSPERMONTH'] < 10 and row['PACKSPERMONTH'] > 1 ):
        return 2
    # non-daily smoker
    else:
        return 3


# creating new group:
# 1- Daily Smokers
# 2- Non-daily Smokers
def DAILY(row):
    # daily smokers
    if (row['PACKSPERMONTH'] < 10 ):
        return 1
    # non-daily smokers
    else:
        return 2


sub2['DAILY'] = sub2.apply( lambda row: DAILY(row), axis=1 )

# renaming categorial variables
#ETHRACE2A
#1. White, Not Hispanic or Latino
#2. Black, Not Hispanic or Latino
#3. American Indian/Alaska Native, Not Hispanic or Latino
#4. Asian/Native Hawaiian/Pacific Islander, Not Hispanic or Latino
#5. Hispanic or Latino

sub2['ETHRACE2A'] = sub2['ETHRACE2A'].astype('category')
sub2['ETHRACE2A'] = sub2['ETHRACE2A'].cat.rename_categories( ['White', 'Black', 'Native American', 'Asian', 'Hispanic'] )


# to plot 2 categorical variable the response variable should have only two values (daily smokers and non-daily smokers)
seaborn.factorplot( x="ETHRACE2A", y="DAILY", data=sub2, kind='bar', ci=None )
plt.title('Indicates that more dependents in nicotine more the people smokes')
plt.xlabel('Packs per month')
plt.ylabel('Proportion nicotine dependence')
plt.plot()
plt.show()



#
# scatter Plot
# formed when is used two numerical or quantitative variables
# Can be positive when the middle line increase, negative when the middle line decrease or neither (non-positive and non-negative)
# when the plots are closer to the middle line there is a strong relationship between the 2 variables
# when the plots are further to the middle line there is a weaker relationship between the 2 variables

print('\n\nScatter Plot')
dataGapMinder = pandas.read_csv( 'Gapminder.csv', low_memory=False )

dataGapMinder['IncomePerPerson'] = dataGapMinder['IncomePerPerson'].convert_objects( convert_numeric=True )
dataGapMinder['ChildrenPerWoman'] = dataGapMinder['ChildrenPerWoman'].convert_objects( convert_numeric=True )

seaborn.regplot( data=dataGapMinder, x="IncomePerPerson", y="ChildrenPerWoman" )
plt.title('Relationship between HIV Rate and the Income per Person')
plt.xlabel('Income per person')
plt.ylabel('Children Per Woman')
plt.plot()
plt.show()

print('\nIncome Per Person - Group')
dataGapMinder['IncomePerPersonGroup'] = pandas.qcut( dataGapMinder.IncomePerPerson, 4, labels=['1=25%', '2=50%', '3=75%', '4=100%'] )
dataGapMinder['IncomePerPersonGroup'] = dataGapMinder['IncomePerPersonGroup'].astype('category')
print( dataGapMinder['IncomePerPersonGroup'].value_counts( sort=False, dropna=True ) )

# bar chart of the new Group
seaborn.factorplot(data=dataGapMinder, x="IncomePerPersonGroup", y="ChildrenPerWoman", kind="bar", ci=None)
plt.title('Income Per Person Grouped x Children Per Woman')
plt.xlabel('Income Per Person (Grouped)')
plt.ylabel('Children Per Woman')
plt.plot()
plt.show()