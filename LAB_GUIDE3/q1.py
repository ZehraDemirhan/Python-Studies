def ineteger_check(m,n):
    t = min (m,n)
    while t!= 0:
       
        if(m % t == 0):
            if(n % t == 0):
                return t

        t = t - 1

num1 = int(input("No1:"))
num2 = int(input("No2:"))

print("GCD: ", ineteger_check(num1,num2))