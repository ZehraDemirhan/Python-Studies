import random

list = []
for i in range(0,1000):
    rand_num = random.randint(0,100)
    list.append(rand_num)

#print(list)

#Selection Sort 

for i in range(0,999):
    min = i
    for j in range(i + 1, 1000):
        if list[j] < list [min]:
            list[j], list[min] = list[min], list[j]

    
print(list)