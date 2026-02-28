"""                                     LIST                                    """
#Mutable, Duplicates, Ordered, Heterogenous
"""
b = [12,13,14,15,16,16,16,35.5,True,print()]

a = ["hello", "How are you"]
print(a[::])
print(b[0])
print(b[:7])
print(b[::])
print(b[-2])

#1st way using index
for i in range(len(b)):
    print(b[i])

#2nd way directly on values
for i in b:
    print(i)

l= [1,3,4,5,6]
l.append(7)
print(l)

l.insert(1,2)
print(l)

l.remove(3)
print(l)

l.extend(a)
print(l)

l[0] = 8
print(l)

#Q. Print positive and negative elements of an list

c = [-45,67,66,-36,9,-20,34]
print("Positive elements are")
for i in c:
    if i >=0:
        print(i)
print("Ngative are ")
for i in c:
    if i<=0:
        print(i)

#Q. Mean of list elements

d = [1,2,3,4,5,6]
sum = 0
for i in d:
    sum = sum + i 
print(sum/len(d))

#Q.Greatest element and print its index too

e = [123,43,54,654,432,2345,65,533]
largest = l[0]
index = 0
for i in range(len(e)):
    if e[i] > largest:
        largest = (e[i])
        index = i
    
print(f"Your largest number is {largest} at index {index}")

#Q. Second largest

f = [12,16,13,19,17]
largest1 = f[0]
sec_largest = l[0]
for i in f:
    if i > largest1:
        sec_largest = largest1
        largest1 = i
    elif i > sec_largest:
        sec_largest = i
print(sec_largest,largest1)


g = [12,13,15,16]
for i in range(len(g)-1):
    if g[i] < g[i+1]:
        continue
    else:
        print("Your list is not sorted")
        break
else:
    print("Your list is sorted")
"""

"""                                 TUPLE                                    """
#Immutable, Duplicates, ordered, Heterogenous
"""
a = (1,2,3,4,5,5,6,6,print(),"hello")

index = a.index(5)
print(index)

count = a.count(5)
print(count)

b,c,d,e = (1,2,3,4)#Unpacking
print(b)
print(type(b))

"""
"""                                 SET                             """
#Mutable,Unordered, semi-Hetrogenous
# We cannot access them through index values
# a = {1,2,3,4,5}
# print(a)
"""
a = hash("hello")
print(a)

b = hash((1,2,344))
print(b)

c = {1,2,3,8,"hello",9,4,5}
for i in c:
    print(i)

d = {1,2,3,4}
d.remove(2)
print(d)
d.add(5)
print(d)
d.pop()
print(d)
d.clear()
print(d)

e = {1,2,3,4,5}
f = {4,5,6,7,8}

s = e.union(f) #(Also write e|f)
print(s)

s = e.intersection(f)#(Also write e&f)
print(s)

s = e.difference(f)#(Also write e-f)
print(s)

s = e.symmetric_difference(f)#(Also write e^f)
print(s)

f -= e
print(f)
"""
"""                             Dictionary                          """
#Mutable, Dulicate,order,Heterogenous
a = {1:"hello", 2:56}
print(type(a))

b = {10:100,20:200,30:300,40:400}
print(b[10])

b[10]=1000 #Updating the value
print(b)

b.update({50:500})
print(b)

b[60] = 600 # Creating the value
print(b)

del b[60] # Deleting 
print(b)

for i in b:
    print(b[i])

c = b
c[10] = 100
print(b)

d = c.copy()
d[10] = 2000
print(c)
print(d)

h = d.get(20)
print(h)
#Q. Write a python script to merge two python dictionaries. 

d1 = {10:100,20:200,40:300}
d2 = {40:400,50:500,60:600}

for i in d2:
    d1[i]= d2[i]

print(d1)

#Q. Write a python program to sum all the values in a dictionary
sum = 0
for i in d1:
    sum = sum + d1[i]

print(sum)

#Q.Count the frequency of each elements

a1 = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,5,5,6,7,9]
count = 0
# for i in a1:
#     if i == 1:
#         count = count + 1
        
# print(count)
e = {}
for i in a1:
    if i in e.keys():
        e[i] = e[i]+1
    else:
        e[i]= 1

print(e) 

#Q. Write a python program to combine two dictionary by adding values for comman keys
d1 = {10:100,20:200,40:300}
d2 = {40:400,50:500,60:600}
for i in d2:
    if i in d1.keys():
        d1[i] = d1[i] + d2[i]
    else:
        d1[i] = d2[i]

print(d1)


