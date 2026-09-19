#       Inheritance - Inheritance is a way of creating a new class from an existing class
'''
class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")
"""        
class Programmer:
    company = "ITC Infotech"
    def show(self):
        print(f"The name is {self.name} and the salry is {self.salary}")
        
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")
        """
class Programmer(Employee):
    company = 'ITC Infotech'
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")
        
        
a = Employee()
b = Programmer()

print(a.company, b.company)
'''
#multiple inheritance
"""
class Employee:
    company = "ITC"
    name = "Default Name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")
        
class coder:
    language = "Python"
    def printLanguages(self):
        print(F"Out of all the languages here is your languages: {self.language}")
        
        
class Programmer(Employee, coder):
    company = 'ITC Infotech'
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")
        
        
a = Employee()
b = Programmer()

a.show()
b.show()
b.printLanguages()
b.showLanguage()
"""

#Multilevel inheritance

'''
class employee:
    a = 1
    
class programmer(employee):
    b = 2
    
class manager(programmer):
    c = 3
    
o = employee()
print(o.a) # Print the attribute
#Print(o.b)# Shows an error as there is no b attribute in employee class

o = programmer()
print(o.a, o.b)

o = manager()
print(o.a, o.b, o.c)
'''
# Super keyword
"""
class employee:
    def __init__(self):
        print("Constructor of employee")
    a = 1
    
class programmer(employee):
    def __init__(self):
         print("Constructor of Programmer")
    b = 2
    
class manager(programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manger")
    c = 3
    
# o = employee()
# print(o.a) # Print the attribute
#Print(o.b)# Shows an error as there is no b attribute in employee class

# o = programmer()
# print(o.a, o.b)

o = manager()
print(o.a, o.b, o.c)
"""

# Class Method
'''
class Employee():
    a = 1
    @classmethod
    def show(cls):
        print(f"The value of a is {cls.a}")
    
e =  Employee()
e.a = 45

e.show()
'''
#property decorator
'''
class Employee():
    a = 1
    @classmethod
    def show(cls):
        print(f"The value of a is {cls.a}")
        
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
    
e =  Employee()
e.a = 45

e.name = "Harry Khan"
print(e.name)
e.show()
'''
# operator overloading

'''
class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)
        
print(n + m)
''' 
#       Practice set

'''Create a class (2-D vector) and use it to create another class representing a 3-D 
vector. '''
"""
class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")


class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


a = TwoDVector(1, 2)
a.show()

b = ThreeDVector(1, 2, 3)
b.show()
"""
"""reate a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
‘Pets’. Add a method ‘bark’ to class ‘Dog’. 
"""
"""
class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    
    @staticmethod
    def bark():
        print("Bow Bow") 
        
d = Dog()
d.bark() 
"""

# Create a class ‘Employee’ and add salary and increment properties to it.
'''Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
which changes the value of increment based on the salary. '''
'''
class Employee:
    salary = 234
    increment = 20
    
    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment/100)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary)-1)*100

e= Employee()
# print(e.salaryAfterIncrement)

e.salaryAfterIncrement = 280
print(e.increment)
'''
"""Write a class ‘Complex’ to represent complex numbers, along with overloaded 
operators ‘+’ and ‘*’ which adds and multiplies them. """
"""
class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    # Addition
    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)

    # Multiplication
    def __mul__(self, c2):
        real = self.r * c2.r - self.i * c2.i
        imaginary = self.r * c2.i + self.i * c2.r

        return Complex(real, imaginary)

    def __str__(self):
        return f"{self.r} + {self.i}i"


c1 = Complex(1, 2)
c2 = Complex(3, 4)

print("Addition:", c1 + c2)
print("Multiplication:", c1 * c2)
"""

""" Write a class vector representing a vector of n dimensions. Overload the + and * 
operator which calculates the sum and the dot(.) product of them. """
'''
class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )
        return result

    def __mul__(self, other):
        result = (
            self.x * other.x +
            self.y * other.y +
            self.z * other.z
        )
        return result

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


# Test the implementation

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)'''

""" Write __str__() method to print the vector as follows: 
7i + 8j +10k  Assume vector of dimension 3 for this problem """
'''
class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )
        return result

    def __mul__(self, other):
        result = (
            self.x * other.x +
            self.y * other.y +
            self.z * other.z
        )
        return result

    def __str__(self):
        return f"Vector({self.x}i + {self.y}j + {self.z}k)"


# Test the implementation

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)
'''

""" Override the __len__() method on vector of problem 5 to display the dimension of the 
vector. 
"""

class Vector:
    def __init__(self, l):
        self.l = l
        
    def __len__(self):
        return len(self.l) 
    
v1 = Vector([1,2,3])
print(len(v1))