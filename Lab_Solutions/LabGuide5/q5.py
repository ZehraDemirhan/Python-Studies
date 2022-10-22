import random
import time

list = []
print("q5")
for i in range(0,1000):
    rand_num = random.randint(0,10000)
    list.append(rand_num)


p = 0
start = time.time()
for i in range(999, 0, -1):
    power = 1
    for j in range(1, i):
        power = power * 2

    p = p + list[i] *power

end = time.time()

print(p)
print(end-start, "seconds")
