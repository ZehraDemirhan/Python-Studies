
month = input("Enter a word")
list = []
while month != 'STOP':
    if len(month) > 5 :
        list.append(month)

    month = input("Enter a word:")
    

print(list)


