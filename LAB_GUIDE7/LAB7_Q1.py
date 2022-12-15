import random
import datetime
def mergesort(array):
    B = []
    C = []
B = C[0:size/2]
    size = len(array)
    if size > 1:
        for i in range(size//2): B.append(array[i])
     

        for i in range(size//2,size):
            C.append(array[i])

        #print(B)
        #print(C)
        mergesort(B)
        mergesort(C)
        merge(B,C,array)
  

def merge(B, C, A):
    i = 0
    j = 0
    k = 0
    while (i < len(B) and j < len(C)):
        if B[i] <= C[j]:
            A[k] = B[i]
            i = i + 1
            #print(i)
        else :
            A[k] = C[j]
            j = j + 1 
            #print(j)
        
        k = k + 1

    
    if i == len(B):
        for remain in range(j,len(C)):
            A.append(array[remain])

    else:
        for remain in range(j,len(C)):
            A.append(array[remain])


start = datetime.datetime.now()

array = []
for i in range(0,1000):
    array.append(random.randint(1,1000))



mergesort(array)

end = datetime.datetime.now()
print(end-start, "seconds")
print(array)


