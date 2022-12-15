class Dog:
    species = "mammal"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def desc(self):
        return ("{} is a good boy and he is {} years old amk".format(self.name, self.age))

class Golden(Dog):
    def bark(self, sound):
        return "{} is a good boy and {} diye bağırır".format(self.name, sound)

rex = Dog("rex",31)

print(rex.desc())

if rex.species  == "mammal":
    print("ürer")
else:
    print("yumurtlar")

oc = Golden("qral", 31)

print(oc.desc())

print(oc.bark("siuuuuuu"))



