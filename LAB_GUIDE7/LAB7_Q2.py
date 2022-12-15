import random
import datetime

def insertionSort(array):
    for i in range(1,len(array)- 1):
        pivot = array[i]
        j = i - 1
        while j >= 0 and array[j] > pivot:
            array[j+1] = array [j]
            j = j - 1

        array[j+1] = pivot 


start = datetime.datetime.now()

array = []
for i in range(0,1000):
    array.append(random.randint(1,1000))



insertionSort(array)

end = datetime.datetime.now()
print(end-start, "seconds")
print(array)

i
array= np.rand.randint(0,100,1000)


