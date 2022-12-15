import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

edu_2013 = pd.read_excel("education_gdp_2013.xlsx")
edu_2014_2015 = pd.read_excel("education_gdp_2014_15.xlsx")

print("EDUCATION 2013\n-------")
print(edu_2013)

print("\nEDUCATION 2014-2015\n-------")
print(edu_2014_2015)

#merged_df = pd.merge(edu_2013,edu_2014_2015,on="Country Name")
merged_df = pd.merge(edu_2013,edu_2014_2015,left_on="Country Name" ,right_on= "Country Name" , how="right")


print("MERGED")
print(merged_df)
merged_df = merged_df.replace("..",np.NaN)

print(merged_df)

merged_df = merged_df.dropna()
print(merged_df)

merged_df["Mean"] = np.mean(merged_df,axis=1)
print(merged_df)

print("\nSorted according to mean\n")
merged_df = merged_df.sort_values('Mean')
print(merged_df)

merged_df["Total Sum"] = np.sum(merged_df , axis =1) - merged_df['Mean']
print("With Sums")
print(merged_df)

#print(merged_df["Country Name"].tolist().index("Poland"))
merged_df = merged_df.drop(5,axis=0)

print(merged_df)

merged_df = merged_df.drop('Total Sum', axis = 1)
print(merged_df)
merged_df = merged_df.drop("Mean",axis =1)


turkey =  merged_df.loc[0 , : ].drop("Country Name" )
poland =  merged_df.loc[4 , : ].drop("Country Name" )

print(turkey)
print(poland)
 

plt.clf()

index = turkey.keys()
bar_width = 0.25
plt.hist(turkey,5,histtype='step')
plt.show()
#turkey =  merged_df.loc["Turkey"]
