import pandas as pd
import numpy as np

DF_area =  pd.read_excel("worldArea.xlsx")
DF_pop = pd.read_excel("worldPop.xlsx")


print(DF_area)
print("----------")
print(DF_pop)


'''
merger = pd.merge(left=DF_area,right=DF_pop,left_on='Country',right_on='Country')
print(merger)

merger=merger.fillna(0)
print(merger)

merger['Density']=merger['Population']/merger['Area(sqm)']
print(merger)


merger = merger.replace(np.inf,np.NaN)
merger = merger.dropna()
print(merger)

merger = merger.sort_values('Density')
print(merger)

'''

