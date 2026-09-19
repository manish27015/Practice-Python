"""
Function = A function is a block of code that performs a specific task 
and can be reused whenever needed.
                Function Definition
Syntax= def hello():
            print("hello")
        
        hello()   # Function call
        
Q. Write a program to greet a user with “Good day” using functions. 

def goodDay():
    print("Good Day")
    
goodDay()

            Recursion
->  It is a function which call itself. 

def factorial(n):
    if(n==0 or n==1):
        return 1  
    return  n* factorial(n-1)

n = int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")

"""

# Write a program using functions to find greatest of three numbers.

'''
def greatest (a, b, c):
    if(a>b and a>c):
        return a
    elif(b>c and b>c):
        return b
    elif (c>a and c>b):
        return c 
    
a = 1
b = 23
c = 3

print(greatest(a, b, c))
'''

#Write a python program using function to convert Celsius to Fahrenheit. 

'''
def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter tempertaure in F: "))
c = f_to_c(f)
print(f"{round(c, 2)}  °C")
'''

# How do you prevent a python print() function to print a new line at the end. 
'''
print("Hello", end="\n")  # new line
print("Hello", end="")    # no new line
'''
# Write a recursive function to calculate the sum of first n natural numbers. 
'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4 
sum(5) = 1 +2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + 4....(n-1) + n
sum(n) = sum(n-1) + n

'''
'''
def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

print(sum(4))
'''
"""
Write a python function to print first n lines of the following pattern: 
    *** 
    **               
    *       - for n = 3
"""
'''
def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(3)
'''
# Write a python function which converts inches to cms.

'''
def inch_to_cms(inch):
    return inch *2.54

n = float(input("Enter value in inches: "))
print(f"The corresponding value in cms is {inch_to_cms(n)}")
'''
#Write a python function to remove a given word from a list ad strip it at the same time. 

'''
def rem(l, word):
    n  = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n 
l = ["Aman", "Rohan", "Shubham", "an"]

print(rem(l, "an"))
'''
#Write a python function to print multiplication table of a given number. 

def multiply(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")
        
multiply(5)