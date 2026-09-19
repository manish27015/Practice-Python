# Write a program to find the greatest of four numbers entered by the user. 
"""
a1 = int(input("Enter number 1 : "))
a2 = int(input("Enter number 2 : "))
a3 = int(input("Enter number 3 : "))
a4 = int(input("Enter number 4 : "))

if (a1>a2 and a1>a3 and a1>a4):
    print("Greater number is a1 :", a1)

elif (a2>a1 and a2>a3 and a2>a4):
    print ("Greater number is a2 :", a2)

elif (a3>a1 and a3>a2 and a3>a4):
    print("Greater number is a3 :", a3)
    
elif(a4>a1 and a4>a2 and a4>a3):
    print("Greater number is a4 :", a4)
"""

""" Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user.  """
"""
n1 = int(input("Enter Math Marks : "))
n2 = int(input("Enter English Marks : "))
n3 = int(input("Enter Hindi Marks : "))

n = (100*(n1+n2+n3))/300
print(n)

if (n>=40 and n1>=33 and n2>=33 and n3>=33):
    print("passed")
else:
    print("failed")

"""

"""A spam comment is defined as a text containing following keywords: 
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
to detect these spams. """
"""
p1 = "Make a lot of money"
p2 = "buy now"
p3= "subscribe this"
p4= "click this"

message = input("Enter your comment: ")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")

"""

"""Write a program to find whether a given username contains less than 10 
characters or not."""

"""
username = input("Enter username")
if(len(username)<10):
    print("Your username contains less than 10 characters")
else:
    print("Your username contains more than or equal to 10 characters")
"""
#Write a program which finds out whether a given name is present in a list or not. 
"""
l = ["Aman", "Ashwani", "Divey", "Subham", "Akash"]
name = input("Enter your name: ")

if(name in l):
    print("Your name is Present in the list.")
else:
    print("This name is not present in the list.")

"""

"""Write a program to calculate the grade of a student from his marks from the 
following scheme: 
90 – 100 => Ex 
80 – 90 => A 
70 – 80 => B 
60 – 70  =>C 
50 – 60 => D 
<50     => F """

"""
marks =int(input("Enter the percentage of marks student got "))

if(marks>=90 and marks<=100):
    print("Students Got 'EX' Grade")
elif(marks>=80 and marks<=90):
    print("Student Got 'A' Grade")
elif(marks>=70 and marks<=80):
    print("Student Got 'B' Grade")
elif(marks>=60 and marks<=70):
    print("Student Got 'c' Grade")
elif(marks>=50 and marks<=60):
    print("Student Got 'D' Grade")
else:
    print("Student Got 'F' Grade")
    
"""
#                   or

marks = int(input("Enter your marks: "))

if(marks<=100 and marks >=90):
    grade = 'Ex'
elif(marks<=90 and marks >=80):
    grade = 'A'
elif(marks<=80 and marks >=70):
    grade = 'B'
elif(marks<=70 and marks >=60):
    grade = 'C'
elif(marks<=60 and marks >=50):
    grade = 'D'
elif(marks<50):
    grade = "F"

print("Your grade is:", grade)
    

# Write a program to find out whether a given post is talking about “Harry” or not. 

post = input("Enter the post : ")
if("Harry".lower() in post.lower()):
    print("This post is taking about harry")
else:
    print("This post is not taking about harry")
    