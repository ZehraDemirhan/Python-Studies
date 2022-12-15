import pandas as pd

fruits = ['apples','oranges','cherries','pears']
quantites = [20,33,52,10]

S=pd.Series(quantites,fruits)
print(S)
print(S['apples':'cherries'])
print(S[0:2])
