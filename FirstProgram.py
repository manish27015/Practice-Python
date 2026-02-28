# print ("namesty youtube we are learning python")
# # Hello, i am manish.
# """Hello, This is multipleline."""
# a = 2
# sher = "Raushan"
# SheryiansSchool = "students" # pascal case

# sheryiansSchool = "students" # Camel case

# sheyians_school = "students" # snake case
# # DATA TYPES

# a = 12  # (......-3,-2,-1,0,1,2,3,4......) = intergers
# b = 56.8 # decimal = float
# c= 12/3 # p/q = float
# v = 34j
# st = "qwerty 1234567 ~!@#$%" # string is store anything in python
# b = True # Boolean
# t = False

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(v))
# print(type(st))
# print(type(t))

# # STRING
# d = "A" # All charecter , number ,emoji everything have own UNICODE.
# print(ord(d)) # chek UNIDODE
# e = 65
# print(chr(e)) # chek Charecter

# f = "SHER"
# print(f[3])
# print(f[-1])# Negative index
# g = "SHER CODER"
# print(g[0:4:1])
# print(g[5:10:1]) # print(G[5::1])
# print(g[1:4:1])
# print(g[5:7:1])

# # Data Type Conversion
# # There are 7 values convertert into false | o, o.o,  empty string, empty list[], empty tuppel(), empty dictionary{} |
# h = 26
# i = str(h)# Explicit = User use in bulid fuction to convert one data type to another
# print(type(i))

# k = 0
# l = 12
# print(bool(k))
# print(bool(l))

# print(12/3) # Implicit = automatically converts data from one data type to another

# name = "manish"
# age = "23"
# print("hello my name is ",name,"and my age is",age) # 
# print(f"my name is {name} and my name is {age}")  # formatted string

# age = input("hello what is your age")
# print(age)

# print (5**2)# square of 2
# print(32%5)
# # python follow BODMAS
# print(12 > 20 and 123 > 100 and 34 == 34 and 45 < 90)
# print(12 > 20 or 123 > 100 and 34 == 34 and 45 < 90)
# print(not 12 == 12)

# IF else
# a = 6

# if a > 0: 
#     print("I will do task A")
# else:
#     print ("I will not do anything")

# money = int(input("Please provide me the money "))
# if money == 10:
#     print("I eat chocobar")
# elif money == 20:
#     print("i eat cone")
# elif money ==30:
#     print ("i eat frosty ")
# else:
#     print(" i eat mango dolly")

# age = int(input("Enter the age "))
# if age >= 18:
#     print("Eligible for vote")
# else:
#     print("Not eligible for vote")

# mathMarks = int(input("Enter Maths marks Number"))
# phyMarks = int(input("Enter Phy marks Number"))
# engMarks = int(input("Enter eng marks Number"))

# if mathMarks >= 33:
#     print("Pass in Math Subject") 
# else:
#     print("failed in math")
# if phyMarks >= 33:
#     print("Pass in the Phy Subject")
# else:
#     print("failed in phy ")
# if engMarks >= 33:
#     print ("pass in the eng subject")
# else:
#     print("Failed in eng")

# if mathMarks >= 33 and phyMarks >=33 and engMarks >=33:
#     print("Pass in all Subject")
# else :
#     print ("Failed")
# a=10//3
# print(a)
#Write a program that takes an integer as input from the user and prints whether the number is even or odd.
# num = int(input("Write a number"))
# if num % 2 == 0:
#     print("This number is even")
# else:
#     print("This number is odd")
#Q. Get a number from the user and check if it is positive, negative, or zero using if-elif-else statements.
# num = int (input("Write the number"))
# if num > 0:
#     print("This number is Positive value")
# elif num < 0:
#     print("This is numbr is negative")
# else:
#     print ("This number is Zero ")
# Q. Write a program to check if a single character entered by a user is a vowel or a consonant. 
# str = input("Enter an Alphabate ")
# if str == "a" or str == "e"  or str == "i" or str == "o" or str == "u":
#     print("This is a vowel")
# else:
#     print("This is a consonant")

"""Q. Take a student's marks in several subjects as input and calculate their percentage. 
 Then, use if-elif-else to print their corresponding grade (e.g., A, B, C, F)."""
# Math_marks = float(input("Enter the marks"))
# Science_marks = float(input("Enter the marks"))
# Sst_marks = float(input("Enter the marks"))
# Hindi_marks = float(input("Enter the marks"))
# English_marks = float(input("Enter the marks"))
# sum = Math_marks + Science_marks + Sst_marks + Hindi_marks + English_marks
# print(sum)
# percent = sum/5
# print(percent)

# if percent >= 90 and percent <=100:
#     print("This student gets 'A' Grade")
# elif percent >= 80 and percent <=90:
#     print("This student gets 'B' Grade")
# elif percent >= 60 and percent <=80:
#     print ("This student gets 'C' Grade")
# elif percent >= 40 and percent <=60:
#     print ("This student gets 'D' Grade")
# elif percent >=34 and percent <= 40:
#     print ("This student gets 'E' Grade")
# else:
#     print("This Students gets 'F' Grade (FAIL)")

"""Q. Write a program that determines if a year entered by the user is a leap year. 
A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400."""
# year = float(input("Enter the year"))
# leap_year = year%4
# leap_year1 = year % 400
# Not_leap_year = year % 100

# if (leap_year1 == 0) or (leap_year == 0 and Not_leap_year != 0):
#     print("This year is Leap year")
# else:
#     print("This year is not leap year")

"""Q. Write a program that takes a string as input and checks if the string is a palindrome (reads the same forwards and backward)."""
# str = input("Enter a string")
# if str == str[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
"""Q. Take the lengths of three sides of a triangle as input and determine if it is an equilateral, isosceles, or scalene triangle."""

# len = float(input("Write the length of the Triangle"))
# wid = float(input("Write the width of the Triangle"))
# hig = float(input("Write the height of the Triangle"))

# angle1 = float(input("Write the angle of the Triangle"))
# angle2= float(input("Write the angle of the Triangle"))
# angle3 = float(input("Write the angle of the Triangle"))

# if (len == wid and wid == hig and len ==hig) and (angle1 == angle2 and angle2 == angle3 and angle1 == angle3):
#     print("This is an equilateral Triangle ")
# elif ((len == wid and len == hig) or (wid == len and wid == hig) or (hig == len and hig == wid) or (len == hig and hig == len) or
#     (wid == len and len == wid) or (hig == wid and wid==hig)) and ((angle1 == angle2 and angle1 ==angle3) or 
#     (angle2 ==angle1 and angle2 == angle3) or (angle3 == angle1 and angle3 == angle2) or (angle1 == angle2 and angle2 == angle1) or 
#     (angle2== angle3 and angle3 == angle2) or (angle3 == angle1 and angle1 == angle3)):
#     print("This is an isosceles traingle ")
# else:
#     print("This is a scalene triangle")


"""                                                or                                             """

# a = float(input("Enter first side: "))
# b = float(input("Enter second side: "))
# c = float(input("Enter third side: "))

# ang1 = float(input("Enter first angle: "))
# ang2 = float(input("Enter second angle: "))
# ang3 = float(input("Enter third angle: "))

# Triangle validity
# if a + b > c and a + c > b and b + c > a and ang1 + ang2 + ang3 == 180:

#     if a == b == c and ang1 == ang2 == ang3:
#         print("Equilateral Triangle")

#     elif (a == b or b == c or a == c) and (ang1 == ang2 or ang2 == ang3 or ang1 == ang3):
#         print("Isosceles Triangle")

#     else:
#         print("Scalene Triangle")

# else:
#     print("Not a valid triangle")


"""Q. Create a program that simulates a login process. Check if the entered username and password are correct 
using logical operators (and, or) and potentially nested if statements. """

# User_name = input("Enter Username")
# Pass_word = int(input("Enter password"))
# Corect_username = "Manish"
# Correct_password = 123456
# if User_name == Corect_username and Pass_word == Correct_password :
#     print("Login Successfully")
# else:
#     print("Invalid Username Or Password! Login failed")

"""This is a classic coding challenge. Write a program that iterates from 1 to a given number. For each number, 
print "Fizz" if the number is divisible by 3, "Buzz" if it's divisible by 5, and "FizzBuzz" if it's divisible
 by both 3 and 5. Otherwise, just print the number. This problem often uses loops along with if-elif-else. But i don't use loops ."""

# num1 = int(input("enter the number"))
# a = num1 % 3
# b = num1 % 5
# if a == 0 and b ==0:
#     print("FizzBuzz")
# elif b == 0 :
#     print ("Buzz")
# elif a == 0  :
#     print("FIzz")
# else:
#     print(f"Print {num1}")

"""Q. to chek temperature"""

# t = int(input("Please tell the temperature :- "))
# if t<0:
#     print("Frezing cold")
# elif t >=0 and t <10:
#     print("Very cold")
# elif t >=10 and t<20:
#     print ("Cold")
# elif t >=20 and t <30:
#     print("Plesant")
# elif t >=30 and t <40:
#     print("Hot")
# else:
#     print("Temprature is very hot")

# Accept an integer and print hello world n times
"""n = int(input("please tell your number"))
for i in range (n):
    print("hello world")
"""
#Print natural number up to n
"""
n = int(input("Please tell the number"))
for i in range (1,n+1):
    print(i)
"""
#Reverse for loop. print n to 1
"""
n = int(input("Plese tell the number"))
for i in range (n,0,-1):
    print(i)
"""
#Take a number as input and print its table
"""
n = int(input("Which table you Want :-"))

# for i in range(n,n*11,n):
#     print(i)
for i in range (1,11):
    print(f"{n} * {i} = {n*i}")
"""
# Sum up to n terms
"""
n = int(input("Please tell the number"))
sum = 0
for i in range (1, n+1):
    sum = sum + i
print("your sum is ",sum)
"""
# factorial upto n terms
"""
n = int(input("Please tell the number"))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print("Your factorial is ",fact)
"""
#Print the sum of all even & odd numbers in s range separately
"""
n = int(input("Plese tell the number :-"))
even = 0
odd = 0
for i in range (1, n+1):
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i
3
print(f"Your even and odd sum are {even}, {odd}")
"""
# Print all the factors of a number
"""
n = int(input("Which number factors you want:-"))

for i in range(1,n+1):
    if n%i == 0:
        print(i)
"""
# Accept a number and check if it a perfect number or not. A number whose sum of factors is equal to the number itself
"""
n = int(input("Plese give the number you want to check "))
sum = 0
for i in range(1,n):
    if n%i == 0:
        sum = sum + i

if sum == n :
    print("This is a perfect number")
else:
    print("This is not perfect number")
"""
# Check wether the number is prime or not
"""
n = int(input("Check the number is prime or not : -"))
count = 0
for i in range(1,n+1):
    if n%i == 0:
        count = count + 1

if count ==2:
    print("This number is prime")
else:
    print("This number is not prime")
"""
# Reverse a string without using in bulid function
"""
a = "SHERYIANS"
b = ""
for i in range(len(a)-1,-1,-1):
    b = b + a[i]

print(b)
"""
# Check the given String is Palindrom or not?
"""
str = input("Write the Word Which you want to check")
str1 = ""
for i in range(len(str)-1,-1,-1):
    str1 = str1 + str[i]
if str1 == str:
    print("This string is Pallindrome")
else:
    print("It's Not a pallindrome")
"""
# Count all letters, digits, and special symbols from a given string
"""
a = "23qwert@#$%^"
char = 0
dig = 0
spchr = 0
for i in a:
    if i.isdigit():
        dig = dig + 1
    elif i.isalpha():
        char = char + 1
    else:
        spchr += 1
print(f"Your digits are {dig}\nyour alphabets are {char}\nyour special charaters are {spchr}") 
"""
# Accept a number and print its reverse
"""
a = int (input("tel the number which you want "))
rev = 0
while a > 0:
    rev = rev *10 + a % 10
    a = a//10
print(rev)
"""
# Check the number is palindrome
"""
a = int (input("tel the number which you want "))
copy = a
rev = 0
while a > 0:
    rev = rev *10 + a % 10
    a = a//10
print(rev)
if rev == copy :
    print("This is pallindrom")
else:
    print("This is not pallindrom")
"""
# Create a random number guessing gamewith python
"""
import random 
num = random.randint(1,10)
tries = 0
while True:   
    guess = int(input("Plese guess your number 1 and 10 :- "))

    if num == guess :
        tries += 1
        print(f"Your are right you gussed the number is {tries} tries")
        break
    elif num < guess:
        print("go a little lower")
        tries += 1
    elif num > guess:
        print("go a litle higher")
        tries +=1
else:
    tries += 1
    print("Sorry you are wrong")
"""
#Check using fuction given string is pallindrom or not?
"""
def pallindrome(st):
    rev =""
    for i in range(len(st)-1,-1,-1):
        rev = rev + st[i]
    if rev ==st:
        print(f"{st} is a Pallindrome")
    else:
        print(f"{st} is Not a pallindrome")

pallindrome("madam")
pallindrome("cursor")
pallindrome("kite")
pallindrome("naman")
 """