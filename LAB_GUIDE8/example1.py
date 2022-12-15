import pandas as pd
fruits=['apples','oranges','cherries','pears']
quan=[20,33,52,10]
S=pd.Series(quan,index=fruits)
print(S)

print('Fruits between 30 and 40')
print(S[(S>30) & (S<40)])


print('Fruits not between (20 and 50)')
print(S[(S<=20) | (S>50)])

print('Fruits not equal to 10')
print(S[S!=10])

