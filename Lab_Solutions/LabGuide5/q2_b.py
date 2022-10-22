from ctypes import sizeof
import random

list = []
for i in range(0,1000):
    rand_num = random.randint(0,100)
    list.append(rand_num)

exchange = True
i = 0
def BubbleSort(inputA):
    while exchange and i < sizeof(inputA)-1:
        exchange = False
        for j in range(0, sizeof(inputA)-1-i):
            if inputA[j+1] < inputA[j]:
                inputA[j+1] ,  inputA[j] = inputA[j],  inputA[j+1]
                exchange = True

        i = i+1

BubbleSort(list)
print(list)

