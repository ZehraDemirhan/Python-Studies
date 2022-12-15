import numpy as np

A = np.random.randint(0,10,10)
B = np.random.randint(0,10,10)

wins = A > B
print(A)
print(B)

print("Team A has won", (np.sum(wins)) , "games")
print(B[np.where(wins)])


print(np.max(A))
print((np.sum(A)+np.sum(B) )/ len(A)+len(B)  )
print("Point difference for each game", print(abs(A-B)))
