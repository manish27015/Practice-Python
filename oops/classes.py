"""                         Class                        """
# A class is like a blueprint or template for creating objects.

class Car:
    brand = "Toyata"

# class Factory:
#     a = 12 # attribute

#     def hello(self): # Method
#         print("How are you")
    
#     print("Hello how are you i am getting initialized ")

# print(Factory().a)
# Factory().hello()

"""                         Objects                 """

# obj = Factory()
# print(obj.a)
# obj.hello()

"""                         Constructor                 """


# class Factory:
#     def __init__(self,material,zips,pockets):
#         self.material = material
#         self.zips = zips
#         self.pockets = pockets
    
#     def show(self):
#         print(f"Your object details are {self.material}, {self.pockets}, {self.zips}")

# reebok = Factory("leather",3,2)
# campus = Factory("nylon",3,3)

# reebok.show()

"""                 Attribute                   """
#Atrributes are just variables define inside the class those are attribute.
#Class attributes- A normal variables created inside a class is a class attributes
#Instance attribute- A attribute created using an instance like self.name,self.age etc.

# class Animal:
#     name = "lion"#Class attribute

#     def __init__(self,age):
#         self.age = age #instance attribute

"""                    Methods                      """
#instance method - An instance method works with instance(object) of the class. This mehod can access and modify instance attributes

class Animal:
    name = "lion"#Class attribute

    def __init__(self,age):
        self.age = age #instance attribute
    
    def show(self):#instance method
        print(f"How are you your age is {self.age}")
    
    @classmethod # class Method
    def hello(cls):
        print("How are you brother")

    @staticmethod
    def static():
        print("How are you")

obj = Animal(12)
obj.show()
obj.hello()
obj.static()