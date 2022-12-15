import math

def sieve(m):
    list = []
    for i in range(2,m):
        list.append(i)


    print("Here",list)


    for i in range(2,math.floor(math.sqrt(m))):
        if list[i] != 0:
            j = i*i
            print(j)
            while j < m :
                list[j-2] = 0
                print(list)
                j = j + i


    newList = []
    for p in range(0,m-2):
        print(p)
        if list[p] != 0:
            newList.append(list[p])
            

    return newList



print(sieve(10))


       