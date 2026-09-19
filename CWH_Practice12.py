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
from function import hello


