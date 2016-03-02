import pandas as pd
import urllib.request as req

#fileReader = req.urlopen('http://dadosabertos.rio.rj.gov.br/apiCOR/apresentacao/csv/nivel_dos_rios/nivel_rios_2014_03.csv')
#csvFile = fileReader.read()

riverLevels = pd.read_csv('nivel_rios_2014_03.csv')

# index_col: indexing the csv file by a column
# low_memory: pandas doenst read all the type of the columns in the file. So increase the performance of the program
riverLevels = pd.read_csv('nivel_rios_2014_03.csv', index_col=0, low_memory=False)
#print(help(pd.read_csv))

#The single bracket version gives a Pandas Series, the double bracket version gives a Pandas DataFrame.
print( riverLevels['Local'] )
print( riverLevels[['Local']] )

print('\n')
print('\n')

# loc retrieves all the content by index
print(  riverLevels.loc['MARACANA'] ) # returns a vertical frame
print(  riverLevels.loc[['MARACANA']] ) # returns a horizontal frame

print('\n')

print(  riverLevels.loc[['MARACANA','GRANDE']] ) # returns a horizontal frame with two lines
print(  riverLevels.loc[['MARACANA','GRANDE'] , ['Apelido','Latitude','Longitude'] ] ) 

print('\n')



print('\n')