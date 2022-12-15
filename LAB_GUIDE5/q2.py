import numpy as np

random_array = np.random.randint(0,100,1000)

def BubbleSort(array):
    size = len(array)
    for i in range(0,size-2):
        for j in range(0 ,size-2):
            if array[j+1] < array[j]:
                array[j+1], array[j] = array[j], array[j+1]


print("Bubble sort")
print(random_array)
BubbleSort(random_array)
print(random_array)