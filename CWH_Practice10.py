#       Class - A class is a blueprint for creating object.
"""""
class Employee:
    language = "Py" # This is a class attribute
    salary = 1200000
    

harry = Employee()
harry.name = "Harry"    # This is a instance attribute
print(harry.name, harry.language, harry.language)

rohan = Employee()
rohan.name = "Rohan Roro RObinson"
print(rohan.name, rohan.language, rohan.language)

'''Here name is instance attribute and salary and language are class 
attributes as they directly belong to the class.'''
"""
"""
class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000
    
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
        
    def greet(self):
        print("good Morning ")
        
    
harry = Employee()
harry.language= "Javascript"    # This is a instance attribute
# print(harry.language, harry.salary)
# Employee.getinfo(harry)
harry.getinfo()
harry.greet()
"""
"""
#           Static Method   
class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000
    
    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
        
    @staticmethod
    def greet():
        print("good Morning ")
        
        
harry = Employee()
harry.getinfo()
harry.greet()

"""
"""

#           constructor

class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000
    
    def __init__(self, name, salary, language): # Dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating a object")
    
    def getinfo(self):
        print(f"The language is {Employee.language}. The salary is {Employee.salary}")
        
    @staticmethod
    def greet():
        print("good Morning ")
        
        
harry = Employee("Harry",130000, "javaScript")
harry.getinfo()
harry.greet()
print(harry.name,harry.salary,harry.language)
# rohan = Employee()
"""
# Practice set
'''Create a class “Programmer” for storing information of few 
working at Microsoft.'''
'''
class Programmer:
    company = "Microsoft"
    
    def __init__(self, name, salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        
p = Programmer("Harry", 120000, 245001)
print(p.name, p.salary, p.pin, p.company)
'''


"""Write a class “Calculator” capable of finding square, cube and square root of a 
number. """
'''
class calculator:
    def __init__(self,n):
        self.n = n
        
    def square(self):
        print(f"The square is {self.n*self.n}")
        
    def cube(self):
        print(f"The cube is {self.n* self.n* self.n}")
        
    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")
        
a = calculator(4)
a.square()
a.squareroot()
a.cube()
'''

"""Create a class with a class attribute a; create an object from it and set ‘a’ 
directly using ‘object.a = 0’. Does this change the class attribute? """
#  NO
'''
class Demo:
    a = 4

o = Demo()
print(o.a)# Print the class attribute because instance attribute is not present

o.a = 0 # Instance is Set

print(o.a) # Print the instance attribute because instance attribute is not present
print(Demo.a)# Print the class attribute

'''
"""Add a static method in problem 2, to greet the user with hello. """
'''
class calculator:
    def __init__(self,n):
        self.n = n
        
    def square(self):
        print(f"The square is {self.n*self.n}")
        
    def cube(self):
        print(f"The cube is {self.n* self.n* self.n}")
        
    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")
        
    @staticmethod
    def hello():
        print("Hello there")
        
a = calculator(4)
a.hello()
a.square()
a.squareroot()
a.cube()
'''

""" Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways. """
'''
from random import randint

class Train:
    
    def __init__(self, trainNo):
        self.trainNo = trainNo
        
    def book(self, fro, to):
        print(F"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
        
    def getStatus(self):
        print(F"Train no : {self.trainNo} is running on time")
        
    def getFare(self, fro, to):
        print(F"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint
        (222, 5555)} ")
        
        
t =  Train(12387)
t.book("Rampur","Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")
'''
"""
from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo
        self.fare = randint(0, 5555)

    def book(self, fro, to):

        if self.fare == 0:
            print("Ticket is not booked")
        elif self.fare < 1000:
            self.classType = "Sleeper"
            print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
            print(f"Class: {self.classType}")
        elif 1500 <= self.fare < 2000:
            self.classType = "3AC"
            print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
            print(f"Class: {self.classType}")
        elif 2500 <= self.fare <= 3000:
            self.classType = "2AC"
            print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
            print(f"Class: {self.classType}")
        elif 3000 < self.fare <= 5555:
            self.classType = "1AC"
            print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
            print(f"Class: {self.classType}")
        else:
            print("Ticket is not available for this fare range")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {self.fare}")


t = Train(12387)

t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")
"""

"""Can you change the self-parameter inside a class to something else (say
“harry”). Try changing self to “slf” or “harry” and see the effects. 
"""

from random import randint

class Train:
    
    def __init__(slf, trainNo):
        slf.trainNo = trainNo
        
    def book(harry, fro, to):
        print(F"Ticket is booked in train no: {harry.trainNo} from {fro} to {to}")
        
    def getStatus(self):
        print(F"Train no : {self.trainNo} is running on time")
        
    def getFare(self, fro, to):
        print(F"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint
        (222, 5555)} ")
        
        
t =  Train(12387)
t.book("Rampur","Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")

#Nothing will be change.