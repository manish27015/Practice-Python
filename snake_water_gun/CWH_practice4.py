#Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up! \
"""
words = {
    "madad" : "help",
    "kursi" : "chair",
    "billi" : "cat",
}
word = input("Enter the word you wany meaning of ")
print(words[word])
"""

#Write a program to input eight numbers from the user and display all the unique numbers (once). 

"""
s = set()
n= input("Enter number: ")
s.add(int(n))
n= input("Enter number: ")
s.add(int(n))
n= input("Enter number: ")
s.add(int(n))
n= input("Enter number: ")
s.add(int(n))
n= input("Enter number: ")
s.add(int(n))
n= input("Enter number: ")
s.add(int(n))
n= input("Enter number: ")
s.add(int(n))
n= input("Enter number: ")
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
print(len(s))

"""
# What is the type of 's'? 

"""
s = {}
print(type(s)) 

"""
#Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique. 

"""
d = {}
name = input("Enter friends name :-")
lang  = input("Enter language name :-")
d.update({name:lang})

name = input("Enter friends name :-")
lang  = input("Enter language name :-")
d.update({name:lang})

name = input("Enter friends name :-")
lang  = input("Enter language name :-")
d.update({name:lang})

name = input("Enter friends name :-")
lang  = input("Enter language name :-")
d.update({name:lang})

print(d)

"""
#if the names of 2 friends are same; what will happen to the program in problem 6? 

"""
d = {}
name = input("Enter friends name :-")
lang  = input("Enter language name :-")
d.update({name:lang})

name = input("Enter friends name :-")
lang  = input("Enter language name :-")
d.update({name:lang})

name = input("Enter friends name :-")
lang  = input("Enter language name :-")
d.update({name:lang})

name = input("Enter friends name :-")
lang  = input("Enter language name :-")
d.update({name:lang})

print(d)

"""
# If languages of two friends are same; what will happen to the program in problem 6? 
"""
d = {}
name = input("Enter friends name :-")
lang  = input("Enter language name :-")
d.update({name:lang})

name = input("Enter friends name :-")
lang  = input("Enter language name :-")
d.update({name:lang})

name = input("Enter friends name :-")
lang  = input("Enter language name :-")
d.update({name:lang})

name = input("Enter friends name :-")
lang  = input("Enter language name :-")
d.update({name:lang})

print(d)
#Nothing will happen. The values can be same
"""

#Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]} 
"""
 No , WE cannot change the value inside a list contained in a set .
 In Fact , we cannot even have list as an element in a set because sets 
in python require alls their elements to be immutablea nd hashable.
"""

s = ()
print(type(s))