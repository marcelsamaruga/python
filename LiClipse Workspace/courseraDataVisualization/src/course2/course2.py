# to install new package: after installing Anaconde
# go to the Andaconda prompt control and type conda install PACKAGE
# to update a package type conda update PACKAGE


# null hypothesis(H0): there no relationship between 2 variables. They are unrelated
# alternative hypothesis(H1 or Ha): there is relationship between 2 variables. They are related

# reject the null hypothesis = accept the alternative hypothesis

# p value = probability value: the value is greater to reject the null hypothesis is 5%
# Significant Level of a Test: 5%
# It means the relationship between the two variables are greater than 5% of change to happen 
#     it's possible to accept the null hypothesis. In other words the variables are not related

#  reject the null hypothesis or considering the variable are related, the p-value is the number of times
#  statistically the research is wrong in 100 samples. 
#  p-value is 0.15 or 15% means statistically the research has 15 error in 100 samples
# the p-value .15 the do not reject the null hypothesis and the variables are not related

# young adults smokers with depression X  young adults smokers without depression
# the p-value of the samples is 0.02 which means reject the null hypothesis and accept the alternative 
# In other words, it's true that young adults smokers with depression smoke more than young adults smokers without depression
 


import pandas
import numpy
import statsmodels.formula.api as smf

# reading the csv file
fullData = pandas.read_csv('nesarc_pds.csv', low_memory=False)

# filtering the dataset according to the desire values
subData = fullData[ (fullData['AGE'] >= 18) & (fullData['AGE'] <= 21) ]

# converting the values in order to retrieve correct values
subData['S3AQ3B1']  = subData['S3AQ3B1'].convert_objects( convert_numeric=True )
subData['S3AQ3C1']  = subData['S3AQ3C1'].convert_objects( convert_numeric=True )
subData['CHECK321'] = subData['CHECK321'].convert_objects( convert_numeric=True ) 

# replacing the values in the research named to Unknown or NA
subData['S3AQ3B1'] = subData['S3AQ3B1'].replace( 9 , numpy.nan )
subData['S3AQ3C1'] = subData['S3AQ3C1'].replace( 99, numpy.nan )

# estimated value of smoked cigarretes in the past 12 months 
estimatedValues = { 1: 30, 2: 22, 3: 14, 4: 5, 5:2.5, 6:1 }
subData['USFREQMO'] = subData['S3AQ3B1'].map( estimatedValues )

subData['USFREQMO'] = subData['USFREQMO'].convert_objects( convert_numeric=True )

# creating new variable, number of cigarette estimated in the month
subData['NUMCIGMO_EST'] = subData['USFREQMO'] * subData['S3AQ3C1']
subData['NUMCIGMO_EST'] = subData['NUMCIGMO_EST'].convert_objects( convert_numeric=True )

print( subData.groupby('NUMCIGMO_EST').size() )
print('\n')

####################
# using the ols function to calculate F-Statistic and p-value
# within the formula: the response variable ~ and explanatory variable -> it's necessary to use C() if the variable is categorical
model = smf.ols( formula='NUMCIGMO_EST ~ C(MAJORDEPLIFE)', data=subData )
results = model.fit()
print('\nSummary of the OLS function\n')
print( results.summary() )

## Prob (F-statistic): 0.604
# The probability of 6% it means: if considering the p-value of 5%, it's false to affirm that young adults smokers with depression
#     tend to smoke more than young adult smokers without depression. So the null hypothesis is acceptable.
#     On the other hand, if considering the alternative hypothesis or affirming there is a relation between the two variables, 
#     the research will be wrong in 6 of 100 cases
#     

#
subFilteredData = subData[[ 'NUMCIGMO_EST', 'MAJORDEPLIFE' ]].dropna()
print('\nMean')
print( subFilteredData.groupby('MAJORDEPLIFE').mean() )
print('\nStandart Deviation')
print( subFilteredData.groupby('MAJORDEPLIFE').std() )


############
# when the explanatory categorical variable has more than 2 groups, like ethnicity (white, black, hispanic, etc)
# creating a new DataFrame
subEthnicity = subData[[ 'NUMCIGMO_EST', 'ETHRACE2A' ]].dropna()

modelEthnicity = smf.ols( data=subEthnicity, formula='NUMCIGMO_EST ~ C(ETHRACE2A)' )
resultsEthnicity = modelEthnicity.fit()
print( resultsEthnicity.summary() )

# when the result indicates 4.30e-8 it means, 4.30 and the decimal point 8 times for the left:
# 4.30e-8 = 0.0000000430

print('\nGroup Ethnicity')
print( subEthnicity.groupby('ETHRACE2A').mean() )
print( subEthnicity.groupby('ETHRACE2A').std() )

# when there are more than two levels of the categorical explanatory variable, it's possible to classify differences among the groups
# using the post hoc test gives the knowledge to test the null hypothesis per group
# there are lots of post hoc tests. In below it will use the Tukey HSD

import statsmodels.stats.multicomp as multi

mc = multi.MultiComparison( subEthnicity['NUMCIGMO_EST'], subEthnicity['ETHRACE2A'] )
results = mc.tukeyhsd()
print( '\nTukey HSD' )
print( results.summary() )