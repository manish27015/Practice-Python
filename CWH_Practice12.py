"""     Walrus Operator :-

The walrus operator (:=), introduced in Python 3.8, allows you to assign values to 
variables as part of an expression. This operator, named for its resemblance to the eyes 
and tusks of a walrus, is officially called the "assignment expression." """
'''
# Using walrus operator 

if (n := len([1, 2, 3, 4, 5])) > 3: 
    
    print(f"List is too long ({n} elements, expected <= 3)") 
    
#   Output: List is too long (5 elements, expected <= 3) 
'''
"""
Types Definition :-
Type hints are added using the colon (:) syntax for variables and the -> syntax for 
function return types. """
'''
n : int = 5

name : str = "Harry"

def sum(a: int, b: int) -> int:
    return a+b
'''
""" Match case:-    
The basic syntax of the match statement involves matching a variable against several 
cases using the case keyword. 
""" 
'''
def http_status(status): 
    match status: 
        case 200: 
            return "OK" 
        case 404: 
            return "Not Found" 
        case 500: 
            return "Internal Server Error" 
        case _: 
            return "Unknown status" 
# Usage 
print(http_status(200))  # Output: OK 
print(http_status(404))  # Output: Not Found 
print(http_status(500))  # Output: Internal Server Error 
print(http_status(403))  # Output: Unknown status 

'''
#       Exception Handling
"""
try:
    a = int(input("Hey, Enter a number"))
    print(a)
    
except Exception as e:
    print(e)
    """
#   raising exception
"""
a = int(input("enter a number: "))
b = int(input("Enter the second number"))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divided numbers by zero")
else:
    print(f"The division a/b is {a/b}")
"""
# try else
'''
try:
    a = int(input("Hey, Enter a number"))
    print(a)
        
except Exception as e:
    print(e)
    
else:
    print("I am inside else")
    '''
    
# try finally
'''
def main():
    try:
        a = int(input("Hey, Enter a number"))
        print(a)
        return
        
    except Exception as e:
        print(e)
        return
    
    finally:
        print("I am inside of finally")
    
main()
'''
# module

# from function import myFunc

#       global
"""
a = 89
def fun():
    global a
    a = 3
    print(a)
     


fun ()
print(a)

"""

#           Enumerate

l = [3, 445, 635, 765]

# index = 0
# for item in l:
#     print(f" The item number at index {index} is {item}")
#     index += 1

#This cam be simplyfied using enumerate function

# for index, item in enumerate(l):
#     print(f"The item at index {index} is {item}")


#               List comprehensions

# myList = [1, 2, 9, 5, 3, 5]
"""
squaredList = []
for item in myList:
    squaredList.append(item*item)
"""

# squaredList = [i*i for i in myList]

# print(squaredList)


#__________Practice set____________________________________

#CHAPTER 12 – PRACTICE SET 
'''
Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not 
present, a message without exiting the program must be printed prompting the same.
''' 
"""
try:
    with open ("1.txt" , "r")as f:
        print(f.read())
except Exception as e:
        print(e)

try:
    with open ("2.txt" , "r")as f:
        print(f.read())
except Exception as e:
        print(e)

try:
    with open ("3.txt" , "r")as f:
        print(f.read())
except Exception as e:
        print(e)

print("Thank You")
"""
 
""" Write a program to print third, fifth and seventh element from a list using enumerate 
function."""
'''
l = [1, 2, 3, 4, 5, 6, 7, 8]

for i, item in enumerate(l):
    if i ==2 or i == 4 or i == 6:
        print(item)
'''
"""
Write a list comprehension to print a list which contains the multiplication table of a 
user entered number."""
'''
n = 5
table = [n*i for i in range(1, 11)]
print(table)
'''

""" Write a program to display a/b where a and b are integers. If b=0, display infinite by 
handling the ‘ZeroDivisionError’. """
"""
try:
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    print(a/b)
except ZeroDivisionError as v:
    print("Infinte")
"""
"""
Store the multiplication tables generated in problem 3
in a file named Tables.txt"""

n = int(input("Enter a number: "))

table = [n*i for i in range(1,11)]
with open ("table.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)} \n")
