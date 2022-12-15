list = [ ('CS 125',3),('HIST 200',4),('PHIL 243',6),('POLS 304',3), ('ENG 101',3) ]

#print(type(list[0][0]))
sum = 0
print("First year courses")
for course in list:
    level = course[0][-3]
    if level == '1':
        sum = sum + course[1]
        print(course[0])


    
print("Sum is ", sum)

#print(list[0][0][1])
