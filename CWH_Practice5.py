"""Q. Write a program to create a dictionary of Hindi words with values as their English 
translation. Provide user with an option to look it up!"""
"""

words = {
    "madad": "help",
    "kurshi": "chair",
    "billi": "cat"
}

word = input("Enter the word you want meaning of: ")
print(words[word])
"""

"""Q. Write a program to input eight numbers from the user and display all the unique 
numbers (once). """
"""
s = set()

n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))

print(s)

"""
#Can we have a set with 18 (int) and '18' (str) as a value in it? 
"""
s = set()
s.add(18)
s.add("18")

print(s)
"""

# What will be the length of following set s: 
"""
s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations? 
print(s)
"""
# What is the type of 's'? 
# s = {} 
# print(type(s))
 
"""Create an empty dictionary. Allow 4 friends to enter their favorite language as 
value and use key as their names. Assume that the names are unique."""

d = {}

name = input("Enter friends name: ")
lang = input("Enter Language name: ")

d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")

d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")

d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Language name: ")

d.update({name: lang})
print(d)
# If the names of 2 friends are same; what will happen to the program in problem 6?
"""Update the lauguages""" #keys are not same.

# If languages of two friends are same; what will happen to the program in problem 6? 
"""Nothing will happen. Values are same """


# Can you change the values inside a list which is contained in set S? 

"""
s = {8, 7, 12, "Harry", [1,2]}
No, because a list cannot be contained inside a set in Python in the 
first place."""