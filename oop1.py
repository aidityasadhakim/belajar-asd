# class Employee:
#     def __init__(self, name, age): # Constructor
#         self.__name =  name
#         self.__email = email
#         self.__address = address
#         self.__age = age

# class Manager(Employee):
#     def __init__(self):
#         self.name = "saddsa"
#         self.age = 12
#         self.email = "saddsa@gmail.com"

# james = Employee("James", 23)
# mike = Employee("Mike", 25)
# amy = Employee("Amy", 21)

# class
# object
# method
# attributes

#inheritance
# override
# encapsulation

class Dog:
    weight = 5

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __str__(self):
        return f'This dog name is {self.name} and age {self.age}, the species is {self.species}'
    
    def bark(self):
        print("Wuff wufff...")

    def getAge(self, token):
        if(token == 123):
            return self.__age
        else:
            return "invalid token"
    
class BullDog(Dog):
    
    def bite(self):
        print("Bulldog bite very hard")

class Husky(Dog):
    
    def bite(self):
        print("Husky Bite not so hard")

class Samoyed(Dog):
    def bark(self):
        print("Bark bark...")

    def parentBark(self):
        return super().bark()

husky = Husky("Bob", 3)
bulldog = BullDog("Steven", 2)
samoyed = Samoyed("Mochi", 4)

samoyed.bark()
samoyed.parentBark()
print(husky.weight)

dog1 = Dog("Bob",3)
dog2 = Dog("Steven",3)
dog2.name = "Charlie"

print(dog2.name)
