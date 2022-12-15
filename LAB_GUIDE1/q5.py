string  = input("Enter your name: ")
print("Your nama has ", len(string), " characters")
print("Your name contains ", string.count("a"), " 'a' characters")
print("Position of blank from start: ", string.find(' '))
print("Surname is ", string[string.find(' '):])
print("Position of your surname from beginning", string.find(string[string.find(' '):])+1)

print("Your name in lowercase", string.lower())
print("Your name in upper case", string.upper())
print("Length of the name is", len(string[0 : string.find(' ')])-1)
print("Length of the surname is", len(string[string.find(' ') : ])-1)
print("After replace all 'e' to 'w", string.replace('e', 'w'))

 
 