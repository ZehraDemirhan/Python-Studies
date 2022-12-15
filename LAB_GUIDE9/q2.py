def HeapBottomUp(H,n):
    start = n//2
    for i in range(start,0,-1):
        k = i 
        v = H[k]
        heap = False
        while not heap and k*2<=n:
            j = 2*k
            if j < n :
                if H[j] < H[j+1]:
                    j = j + 1

            if  v >= H[j]:
                heap = True
            else:
                H[k] = H[j]
                k = j


        H[k] = v

    return H


def heapSort(arr):
    n = len(arr)
    HeapBottomUp(arr, n-1)
    for i in range(n-1,1,-1):
        arr[i], arr[1] = arr[1], arr[i]
        HeapBottomUp(arr,i-1)


#main
HArr = [0,2,9,7,6,5,8,10]
print("Beginning Array", HArr)
n = len(HArr)
print("Array after Hepify:",HeapBottomUp(HArr,n -1))

print("Root:", HArr[1])
i = 2
j = 2
while i<=n:
    print(j,". level nodes")
    print(HArr[i :i*2])
    i = i*2
    j = j + 1

heapSort(HArr)
print("After sort: ", HArr)