import pandas as pd

fruits1 = ['peaches','oranges','cherries','pears']
fruits2 = ['raspberries','oranges','cherries','pears']
s1 = pd.Series([20,33,52,10],index=fruits1)
s2 = pd.Series([17,13,31,31],index=fruits2)


s3=s1+s2
print(s1)
print(s2)
print("--------")

print(s1+s2)
print("--------")
s3=s3.fillna(10)
#s3 = s3.dropna()
print(s3)
s3 = s3.drop(labels = ["pears","peaches"]) 
print("after drop")
print("------")
print(s3)


'''
s3=s3.dropna()
print(s3)
'''






