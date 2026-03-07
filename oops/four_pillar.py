#Inheritance-
""" 
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

"""
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
"""
#Polymorphism-
"""Polymorphism is a core concept in OOps. The word means "Many forms"
 and in programming, it allows the same interface or method name to behave
 differently depending on the object or context"""

# class Animal:
#     def show(self):
#         print("Hello, ia am Manish")
    
# class Human(Animal):
#     def show(self): #Method overriding
#         print("How are you")

# obj = Human()
# obj.show()
"""
#Duck typing
class Animal1:
    def show(self):
        print("I am showing")

class Human1:
    def show(self):
        print("Hello i am also showing")

obj = Animal1()
obj2 = Human1()

obj.show()
obj2.show()
"""

#Encapsulation
"""
It means putting dat (variables) and code (function) together in one
place - inside a class.
- It also means hiding the internal details of how things work, and
only showing what is needed.
- it keeps data safe from beong changed by mistake
- it makes your code clean and easy to use
- it gives control over what others can access or change
"""
"""
class Factory:
    a = "pune"
    def show(self):
        print("hello I am a pune factory")

class Bhopal(Factory):
    def show2(self):
        print(super().a)

obj = Bhopal()
obj.show2()
 
# obj = Factory()
# print(obj.a)
# obj.a = "Bopal"
# print(obj.a)
"""
# Acess Modifier
"""
class Factory:
    __a = "pune"
    def show(self):
        print(Factory.__a)

obj = Factory()
obj.show()

class Demo:
    def __init__(self):
        self.name = "Public Member"     #PUBLIC
        self._age = 21                  #PROTECTED
        self.__salary = 50000           #PRIVATE

    def show(self):
        print("Inside the class")
        print("public:",self.name)
        print("Protected:", self._age)
        print("Private", self.__salary) 
        
obj = Demo()
obj.show()
print("\nOutside the class:")
print("Public:", obj.name)        
print("Protected:", obj._age) 
print("Private:", obj._Demo__salary)
"""
#Abstraction 
"""
Abstraction does not exit in python "we can achives it using a library we will
see what is a library later."
- Abstraction is used to simplifying complex systems by focusing on essential
features and hiding unnecessary details.
-It is used to define a common interface for different subclasses."""

from abc import ABC, abstractmethod

class Abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square(Abstract):
    def __init__(self,side):
        self.side = side
    
class Circle(Abstract):
    def __init__(self,radius):
        self.radius = radius

    def perimeter(self):
        print("I have created")
        
    def area(self):
        print("I have created this")

obj = Circle(7)