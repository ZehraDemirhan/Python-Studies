import pandas as pd
import numpy as np

#read file content into the dataframe
DF14_15 = pd.read_excel('education_gdp_2014_15.xlsx')
DF_13 = pd.read_excel('education_gdp_2013.xlsx')

#print the data sets
print('2014_15 Data:')
print(DF14_15)

print('2013 Data:')
print(DF_13)

#join the data sets, to include 2013-2016 data, only for countries
#that appear in both sets.
#
data_all = pd.merge(left = DF_13, right = DF14_15, left_on = 'Country Name', right_on = 'Country Name')
print('\nMerged Data Set: ')
print(data_all)

#drop all countries with ... values
data_all = data_all.replace('..', np.NaN)

print("DATA")
print(data_all)
data_all['ZEROS'] = 0


print(data_all)

#add column - mean of 3 years
#print(data_all[['ZEROS','Country Name']])
data_all['Mean'] = np.mean(data_all[[int('2014'),int('2015')]], axis=1)
print('\nData Set with Mean: ')
print(data_all)

#sort data by the mean
data_all = data_all.sort_values('Mean')
print('\nSorted by Mean: ')
print(data_all)

'''
#changing a column to list
arr=data_all.get('Mean').tolist()
arr=data_all['Mean'].tolist()
print(arr)
'''








