import time
def findSum():
    sum=0
  
    for i in range(0,10000000):
        sum = sum + i

   



start =  time.time()
findSum()
end = time.time()

print(end- start)