#Purpose: Program finds the solution of the sum by using the formula
#then see the time efficiency
import time

#Function to find the sum of n consecutive numbers
def sum_of_n(n):
   the_sum=0
   start = time.time()
   for i in range (n+1):
      the_sum = the_sum+i
   end = time.time()
   return(the_sum,end-start)

#main
for i in range(5):
   print("Sum is %d required %10.7f seconds"%sum_of_n(100000))
   
#find the solution of summation by using formulae
start = time.time()
the_sum = 100000*(100000+1)/2
end = time.time()
print("Sum is", the_sum, " required" ,  end-start, "seconds if we use formulae")

