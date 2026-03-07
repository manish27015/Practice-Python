#Dunder method
"""
Dunder methods are special methods in python that start and
end with double underscores, like __init__,___str__,__add__,
etc.
- They automatically get called when you perform certain action on 
an objects.
-Customize behaivor of class
-Make class objects behave like bulit-in-data types
(like string,lists etc)"""

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return(f"hello how are you and your name is {self.name}")
    
    def __add__(self, other):
        sum = 0
        for i in other:
            sum = sum + i.age

        return(f"Your sum of ages are {self.age + sum}")
        
obj = Animal("lion",12)
obj1 = Animal("Dolphin",14)
obj2 = Animal("Tiger",12)
print(obj + (obj1,obj2))  
print(obj)
print(obj1)
