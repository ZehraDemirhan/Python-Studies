import numpy as np 

random_array = np.random.randint(0,100,1000)

def selectionSort(array):
    for i in range(0, len(array)-2):
        min = i
        for j in range(i+1, len(array) -1):
            if array[j] < array[min]:
                min = j
        
        array[i] , array[min] = array[min], array[i]



print(random_array)
selectionSort(random_array)
print(random_array)
        
