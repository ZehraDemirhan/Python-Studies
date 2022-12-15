import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

world_area = pd.read_excel("worldArea.xlsx")
world_pop = pd.read_excel("worldPop.xlsx")

print(world_area)
print(world_pop)

merged_df = pd.merge(world_area,world_pop, on="Country")
print("Merged")
print(merged_df)

#print(merged_df.iloc[:,2].tolist())
#merged_df = merged_df.dropna()

merged_df = merged_df.fillna(0)
print(merged_df)

countryNames = merged_df['Country'].tolist()[0:10]
print(countryNames)

area = merged_df['Area(sqm)'].tolist()[0:10]
population = merged_df['Population'].tolist()[0:10]
population = population *10
print(population)

plt.clf()
n_groups = 10
index = np.arange(10)


bar_width = 0.25


plt.figure(2)
plt.hist(population,5,histtype='step')
plt.show()
