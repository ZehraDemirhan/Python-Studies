import random

string = input("Enter your name and surname to password:")
print(string)
slice = string[3:6]
print("Slicing the name (3,7)",slice)
rand_num = random.randint(1,900)
print("Random number: ", rand_num)
password = slice + str(rand_num)

print(password)