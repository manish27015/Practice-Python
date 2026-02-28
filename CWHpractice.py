# name = input("Enter your name")
# print("Good Afternoon ",name)


# date = input ("enter the date")
# print("letter ='''")
# print(f"Dear {name}" "\n"
#     "you are selected!""\n",
#     date ,"\n"
#     "'''")

# str ="manish  kumar"
# index = str.find("  ")
# print(bool(index))
# print(index)

# replaced_string = str.replace("  "," ")
# print(replaced_string)

# l = 10
# w = 7
# r = 5
# areaR = l*w
# print(areaR)

# areaC = 3.14*r*r
# print(areaC)



# print ((456 == 456) != (234 == 236))
# print("Hello how are you.")
"""
def sum(a,b):
    print(f"The sum of your number is {a+b}")

sum(5,9)
"""
# Use a while loop to print the first 10 natural numbers (1 to 10).

a=0
while a < 10:
    a = a + 1
    print("Nautural number", a)

#Use a for loop to display all the items in a given list, for example, [10, 20, 30, 40, 50].

a = [10, 20, 30, 40, 50]

for i in a:#Range sirf int mai diya jata hai
    print(i)

#Write a program that calculates the sum of all numbers from 1 to a user-provided number.

num = int(input("Tell the number :- "))
num1 = 0
for i in range(0,num+1):
    num1 = num1 + i

print(num1)
