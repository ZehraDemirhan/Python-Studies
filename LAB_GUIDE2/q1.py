
list = []
sum = 0
for i in range(0,5):
    list.append(int(input("Enter a number:")))
    sum+=list[i]

print("Avarage is ", sum/5)
print("List of numbers ", list)
list.sort()
print("Sorted format ",list )
list.reverse()
print("Reverse format of the list",list )

for i in range(0,len(list)):
    if list[i] < sum/5:
        list.remove(list[i])
        break


print("Final format of list:" , list)

