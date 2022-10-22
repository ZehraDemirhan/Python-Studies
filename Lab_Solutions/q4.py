# -*- coding: utf-8 -*-
"""
This is a temporary script file.
"""
#Purpose: Program gets the name and surname of the user
#then genarates password for that user,
#getting the characters from the 3,6 then put a generated number(1-999) to the end

#import random module to generate a random number
import random
#get the name of the user
name = input("Enter your name and surname to password:")
print(name)

#get the part1 by slicing the string name
part1 = name[3:7]
print("Slicing the name (3,6):",part1)

#generate random number
rand_num = random.randint(1,900)
print("Random number (1-900):",rand_num)
password = part1 + str(rand_num)
print("Generated password",password)