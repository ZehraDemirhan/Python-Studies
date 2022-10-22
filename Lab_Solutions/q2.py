#Purpose: Program defines a tuple with the given courses
#then finds the courses in the first year.

#defining list of tuple
courses = [('CS 125',3),('HIST 200',4),('PHIL 243',6),('POLS 304',3), ('ENG 101',3)]

#if the course code begin with the '1'
#display the course and also find the total of credits
total_credits = 0
print('First year courses:')
for course in courses:
    level = course[0][-3]
    if level == '1':
        print(course[0])
        total_credits += course[1]

#display the total credits for the first year
print('\nTotal credits for first year courses:',total_credits)
