import pandas as pd
import numpy as np

years = range(2015,2019)

product1 = pd.Series([2409.14, 2941.01, 3496.83, 3119.55], index = years)
product2 = pd.Series([1203.45, 3441.62, 3007.83, 3619.53], index = years)
product3 = pd.Series([3412.12, 3491.16, 3457.19, 1963.10], index = years)

product_data = pd.DataFrame({'P1':product1,'P2':product2,'P3':product3})
print(product_data)
print(product_data.values[0])
print(product_data['P1'])

print(product_data[['P1','P3']])
'''
print(product_data.values[0])


print(product_data.values[1,0])

product_data.values[1,0]=999

print(product_data.values[1,0])

print(product_data['P1'])

print(product_data[['P1','P3']])
'''


'''
product_data['P4']=10
print(product_data)

product_data['P5']=(2000,3000,4000,5000)
print(product_data)

product_data['P6']=[1000,6000,7000,8000]
print(product_data)

product_data['P7']=product_data['P6']*1.5
print(product_data)

product_data['TOTAL']=np.sum(product_data,axis=1)
print(product_data)

product_data=product_data.drop([2017],axis=0)
print(product_data)

product_data=product_data.drop([2015,2018],axis=0)
print(product_data)

'''
