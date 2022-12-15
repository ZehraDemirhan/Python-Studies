def euclids_algorithm(n,m):
    if n == 0 :
        return m
    while n != 0:
        r = m % n 
        m = n
        n = r

    return m 


num1 = int(input("No1:"))
num2 = int(input("No2:"))

print("GCD: ", euclids_algorithm(num1,num2))
