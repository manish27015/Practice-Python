# lamda function - Function created using an expression using ' lambda' keyword


# def square(n):
#     return n*n
square = lambda X: X*X
print(square(5))

# Join method

a = ["Harry", "Rohan", "sohan"]
final = "::".join(a)
print(final)

# format

a = "{} is a good {}".format("harry", "boy")    
print(a)
# "{1} is a good {0}".format("harry", "boy") 

# Map- it applies a function to all the items in an input_list

l = [1, 2, 3, 4, 5]
square = lambda x: x*x
sqList = map(square, l)
# print(sqList)
print(list(sqList))


# filter- Filter creates a list of items for which the function returns true. 

def even(n):
    if n%2 == 0:
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))


# reduce- Reduce applies a rolling computation to sequential pair of elements. 

from functools import reduce

def sum(a, b):
    return a+b

mul = lambda x,y:x*y

print(reduce(sum, l))
print(reduce(mul,l))

# ----------Practice-----------------
"""Write a program to input name, marks and phone number of a student and format it 
using the format function like below:"""
'''
name = input("enter name: ")
marks = int(input("Enter marks: "))
phone = int(input("Enter phone number: "))

s = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone) 

print(s)
'''
"""A list contains the multiplication table of 7. write a program to convert it to vertical 
string of same numbers."""
'''
table = [str(7*i) for i in range (1,11)]

s = "\n".join(table)
print(s)
'''
# Write a program to filter a list of numbers which are divisible by 5. 
def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1, 2, 23, 543, 3423, 65, 345, 85, 55]
f = list(filter(divisible5, a))
print(f)

#Write a program to find the maximum of the numbers in a list using the reduce function. 

l = [111, 2, 65, 53, 655, 75, 45, 56]

def greater(a, b):
    if(a>b):
        return a
    return b

print(reduce(greater, l))
