import pandas as pd
import matplotlib.pyplot as plt

#data frame
df_score = pd.read_csv('scores.csv')
print(df_score)
df_score['NEW GRADES'] = df_score['grades'] + df_score['grades'] * 0.23
print(df_score)
for i in range(0,len(df_score)):
    if df_score.values[i,1] < 15:
        df_score.iloc[i,1]=6
print(df_score)

plt.figure() #opens a new active figure window
plt.clf() #clears the figure window

plt.figure(figsize = (11,4))

plt.subplot(1,2,1)
print("GRADES")
print(df_score['grades'])
print(df_score['grades'].tolist())
plt.hist(df_score['grades'].tolist(),5,histtype='step') #plots scores with 5 bins/buckets
plt.xlabel('Bins set to 5')
plt.title('Grades set to 5 range')

plt.subplot(1,2,2)
plt.hist(df_score['grades'],color = 'red',edgecolor="black") 
plt.xlabel('Bins not specified (default:10)')
plt.title('Grades set to 10 range')
plt.show()
