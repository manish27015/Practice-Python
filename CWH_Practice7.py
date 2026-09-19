# Write a program to print multiplication table of a given number using for loop.
'''
n = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")
'''
    
"""Write a program to greet all the person names stored in a list ‘l’ and which starts 
with S. 
"""
'''
l = ["Harry", "Soham", "Sachin", "Rahul"] 
for name in l:
    if(name.startswith("S")):
        print(f"hello {name}")
'''

# Attempt problem 1 using while loop. 
'''
n = int(input("Enter the number: "))
i=0
while(i<11):
    print(f"{n} X {i} = {n*i}")
    i= i+1
'''
    
#Write a program to find whether a given number is prime or not. 
'''
n = int(input("Enter the number: "))

for i in range(2,n):
    if(n%i==0):
        print("This number is not prime")
        break
else:
    print("Number is prime")
'''

#Write a program to find the sum of first n natural numbers using while loop. 
'''
n = int(input("Enter the number: "))
i = 1
sum = 0
while(i <= n):
    sum = sum + i
    i = i+1

print(sum)
'''

# 6. Write a program to calculate the factorial of a given number using for loop. \
'''   
n = int(input("Enter the number: "))

product = 1
for i in range(1,n+1):
   product = product*i

print(product)    
'''
"""
Write a program to print the following star pattern. 
  * 
 *** 
*****   for n = 3 

"""
'''
n = int(input("Enter the number :"))

for i in range(1, n+1):
    print(" " * (n-i), end="")
    print("*" * (2*i-1), end="")
    print("")

'''
"""
Write a program to print the following star pattern: 
* 
** 
***      for n = 3 
"""

'''
n = int(input("Enter the number :"))

for i in range(1,n+1):
    print("*" * i, end="")
    print("")
    
'''
"""

Write a program to print the following star pattern. 
* * * 
*   *   for n = 3 
* * *  

"""
'''
n= int(input("Enter the number :"))

for i in range(1, n+1):
    if(i==1 or i==n):
        print("*" * n, end="")
    else:
        print("*",end="")
        print(" " * (n-2), end="")
        print("*", end="")
    print("")
'''
"""
Write a program to print multiplication table of n using for loops in reversed 
order.
"""
'''
n= int(input("Enter the number: "))
for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")    
'''

"""Print even number"""

'''
n = int(input("Enter the number :"))

for i in range(1,n):
    if(i%2==0):
        print(i)
'''
"""
n = int(input("Enter the number :"))

for i in range(1,n):
    if(i%2!=0):
        print(i)
"""

"""firstly square the number then sum these number"""
'''
n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    sum = i * (i + 1) * (2 * i + 1) // 6

print(sum)
'''

"""Find the even number between 1 and n , sum the all even number"""

'''
n = int(input("Enter the number :"))
sum = 0
for i in range (1,n+1):
    if(i%2==0):
        sum = sum + i
print(sum)
'''    

'''
n = int(input("Enter the number :"))
i= 1
while(i<n+1):
    print(i)
    i = i + 1
'''
'''
n = int(input("Enter the number :"))
i = 0
while(i<n):
    print(n-i)
    i= i+1
'''
'''
n = int(input("Enter the number :"))
i = 1
sum = 0
while(i<n+1):
    sum = sum + i
    i = i + 1

print(sum)
'''
'''
n = input("Enter the number :")

count = 0

for i in n:

    count = count + 1

print(count)
'''
"""
n = int(input("Enter the number: "))

count = 0

while n > 0:
    n = n // 10
    count = count + 1

print("Number of digits:", count)
"""
'''
n = int(input("Enter the number: "))

r = 0

while(n>0):
    d = n%10
    r = r*10 + d
    n = n//10

print(r)
    
'''
'''
for n in range(2, 101):
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print(n)
'''

'''
n = input("Enter the number: ")

even = 0
odd = 0

for digit in n:
    if int(digit) % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even digits:", even)
print("Odd digits:", odd)
'''
''' 
n = int(input("Enter a number: "))

largest = 0

while n > 0:
    digit = n % 10

    if digit > largest:
        largest = digit

    n = n // 10

print("Largest digit:", largest)
'''
'''
n = int(input("Enter a number: "))

largest = 0

for digit in str(n):
    if int(digit) > largest:
        largest = int(digit)

print("Largest digit:", largest)
'''