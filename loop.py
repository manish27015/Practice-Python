# For loop
#range()      (s,s,s)start:stop:steps
# a = range(1,21,1)
# for i in range(1,21,2):
#     print(i)
# for i in range(21):
#     print(i)
#for i in range (16,0,-1):#reverse change in steps -1
#   print(i)
# Q. Lets Print a table of 5
"""
for i in range (5,51,5):
    print(i)
"""
# Table you want
"""
n = int(input("Which table you want ?"))
for i in range(n,n*10+1,n):
    print(i)
"""
#Loops for string
"""
a = "SHERYIANS"
#print(a[8])
for i in range(0,9,1):
    print(a[i])
"""
"""
a = "SHERYIANS TEACHES INDUSTRY THINGS"
print(len(a))

for i in range(len(a)):
    print(a[i])
"""
"""
for i in range(1,21):
    if i == 15:
        break
    print(i)

for i in range(1,21):
    if i == 15:
        continue
    print(i)
"""
"""
for i in range(1,21):
    if i == 13:
        print("break statement is executed")
        break
    print(i)

else:
    print("Break statemnet is not executed")

for i in range(1,21):
    if i == 22:
        print("continue statement is executed")
        continue
    print(i)

else:
    print("contiue statemnet is not executed")
"""
# While Loop
"""
a = 1
while a <= 30:
    print(a)
    a = a+1
"""
a = int(input("Tell the number "))
while  a > 0:
     print(a % 10)
     a = a // 10