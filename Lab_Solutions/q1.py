#Purpose: Program gets 5 integer from the user
#finds the avg of these numbers, then put the numbers
#into a list which are below the avg
sum = 0;
list = []
#getting 5 numbers and put them to list
for i in range(0,5):
    num = int(input("Enter a number:"))
    sum += num
    list.append(num)

#calculating avg of these 5 numbers
avg = sum / 5;
#displaying the avg and list content
print("Average is",avg)
print("List of numbers ",list)

list.sort()
print("Sorted format of the list ",list)
list.reverse()
print("Reverse format of the list ",list)
#removing the first number which are below the average

for i in list:
    if i < avg:
        list.remove(i)
        break;
      
#displaying the final format of the list
print("Final format of list:",list)
    
