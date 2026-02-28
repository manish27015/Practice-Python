"""Inheritance- 
Inheritance is a concept of Object-Oriented Programming (OOP)
where one class (child) gets properties and methods of another class
(parent).
"""
"""
class Factorymumbai:        #parent class/super class
    a = "I am an attribute mentioned inside Factory"
    def hello(self):
        print("Hello i am a method mentioned inside Factory")

class FactoryPune(Factorymumbai):   #Chlid class
    pass

obj = Factorymumbai()
print(obj.a)

obj2 = FactoryPune()
print(obj.a)
obj2.hello()

"""
"""
class Animal:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"Hello your name is {self.name}")

class Human(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
 
    def show(self):
        print(f"hello your name is {self.name},{self.age}")

person1 = Human("Manish",23)
person1.show()
animal1 = Animal("cat")
animal1.show()
"""
"""
class Animal:
    def __init__(self,name):
        pass

class Human:
    def __init__(self,name,age):
       pass

class Robots(Human,Animal):
    name3 = "charli123"

obj = Robots("Raushan",28)
"""

"""Note:- The constructor function will be inherited of the first class
that has been inherited. This is MRO (Method Resolution Order) followed by python"""

class Factory:  #Grandparent
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips

class BhopalFactory(Factory):   #Parent
    def __init__(self, material, zips,color):
        super().__init__(material, zips)
        self.color = color

class punefactory(BhopalFactory):   #Child
    def __init__(self, material, zips, color, pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets
    
obj = punefactory("nylon",2,"black",12)
# print(obj.material)
# print(obj.zips)
# print(obj.color)
# print(obj.pockets)
print(vars(obj))