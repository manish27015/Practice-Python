#Write a program to store seven marks in a list entered by the user.
"""
marks = []
 
f1 = int(input("Tell the Marks here"))
marks.append(f1)
f2 = int(input("Tell the Marks here"))
marks.append(f2)
f3 = int(input("Tell the Marks here"))
marks.append(f3)
f4 = int(input("Tell the Marks here"))
marks.append(f4)
f5 = int(input("Tell the Marks here"))
marks.append(f5)
f6 = int(input("Tell the Marks here"))
marks.append(f6)
f7 = int(input("Tell the Marks here"))
marks.append(f7)

print(marks)
"""
#Write a program to accept marks of 6 students and display them in a sorted manner

"""
marks = []
 
f1 = int(input("Tell the Marks here"))
marks.append(f1)
f2 = int(input("Tell the Marks here"))
marks.append(f2)
f3 = int(input("Tell the Marks here"))
marks.append(f3)
f4 = int(input("Tell the Marks here"))
marks.append(f4)
f5 = int(input("Tell the Marks here"))
marks.append(f5)
f6 = int(input("Tell the Marks here"))
marks.append(f6)

marks.sort()
print(marks)

"""
#Check that a tuple type cannot be changed in python. 
"""
a = (34, 234, "MANISH") #Tupple
a[2] = "Raushan"

b = [2,45,"shahil"]  #List
b[2]= "Ankit"
print(b)
"""
#Write a program to sum a list with 4 numbers. 

l = [3,5,4,6]
print(sum(l))

#Write a program to count the number of zeros in the following tuple: 

a = (7, 0, 8, 0, 0, 9)
n = a.count(0)
print(n)