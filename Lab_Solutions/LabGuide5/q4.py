import random
import time

list = []
for i in range(0,1000):
    rand_num = random.randint(0,10000)
    list.append(rand_num)


p = list[0]
power = 1
print("q4")
start = time.time() 
for i in range (1,999):
   
    power = power * 2
    p = p + list[i] * power


end = time.time()
print(p)
print(end - start , "Seconds")