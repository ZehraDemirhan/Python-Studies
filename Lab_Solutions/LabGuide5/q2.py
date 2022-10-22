
import random

list = []
for i in range(0,1000):
    rand_num = random.randint(0,100)
    list.append(rand_num)

print("before sort")
print(list)


for i in range (0, 999):
        for j in range(0,999-i):
            if list[j+1] < list[j]:
               list[j+1] ,  list[j] = list[j],  list[j+1]


print("after sort")
print(list)

def BubbleSort(arrayInput):
    for i in range(0 ,1000):
        for j in range(0,999-i):
            if arrayInput[j+1] < arrayInput[j]:
               arrayInput[j+1] ,  arrayInput[j] = arrayInput[j],  arrayInput[j+1]


BubbleSort(list)
print(list)