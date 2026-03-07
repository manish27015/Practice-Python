# Decorator
# class Animal:
#     @property
#     def show(self):
#         print("Hello how are you")
    
# obj = Animal()
# obj.show
"""
def decorate(func):
    def wrapper():
        print("I will Print myself before the function hello")
        func()
        print("I will print after the function")
    return wrapper
@decorate
def Hello():
    print("hello I am manish ")
Hello()
"""
# For Addition
"""
def decorate(func):
    def wrapper(a,b):
        print("The addition to your number")
        func(a,b)
        print("thankyou I hope you liked it")
    return wrapper

@decorate
def addition(a,b):
    print(f"Your total is {a + b}")
    
addition(12,20)
"""

# Args and Kwargs
#for args used *
#for Kwargs used **
#Args- Args used for multiple positional arguments, and kwargs are used for multiple key word arguments.
"""def addition(*args):
    sum = 0
    for i in args:
        sum = sum + i
   
    print(sum)


addition(12,12,12,13)

def information(**kwargs):
    print("Your information is :-\n")
    for i in kwargs:
        print(f"{i}:{kwargs[i]}")


information(name = "Manish", age = 23, designation = "AI Devops Analyst")

def decorate(func):
    def wrapper(*a,**k):
        print("The addition to your number")
        func(*a,**k)
        print("thankyou I hope you liked it")
    return wrapper

@decorate
def addition(a,b):
    print(f"Your total is {a + b}")
    
addition(12,20)
"""
#List, Dictionary and set comphrehension

# l = [i for i in range(1,21) if i % 2 == 0]  # List comp
# print(l)

# l = {i : i**2 for i in range(1,10)} #Dictionary comp
# print(l)

# Lambda function
"""
-A lambda function is an anonymous, inline function defined using the 
lambda keyword.
-It's often used for short, simple function that are used only once or temporarily"""

# addition = lambda a,b : a+b
# print(addition(12,13))

# obj = lambda a: "even" if a % 2 == 0 else "odd"
# print(obj(13))

#    Map         
"""
a = [1,2,3,4,5]
# result = map(lambda x: x*2,a)
# print(list(result))

def double (x):  # Also do like this
    return x*2
result = map(double,a)
print(list(result))
"""

#             Filter              
"""
def even(x):
    if x%2 ==0:
        return True
    else:
        return False

a = [1,2,3,4,5,6,7,8,9]
result = filter(even , a)
print(list(result))

result = filter (lambda x : True if x%2 == 0 else False , a)    # Also do like this 
print(list(result))
"""
# Package & Modules
import modelss.maths as maths

print(maths.addition(12,12))
print(maths.multiplication(2,6))

from modelss import hello, maths # this is the way import file


