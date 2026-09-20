# print("Hello how are you.")
"""Create a function:-

def hello():
    print("This is a hello function.")

hello()
"""
"""
def sum(a,b):
    print("The sum of your number is ",a+b)

sum(3,4)
sum(12,12)
sum(13,13)
"""
"""
def hello(name,age):
    print(f"Your name is {name} and your age is {age}")

hello(age=22,name="akarsh")
"""
'''
def hello():
    return "hello how are you"

print(hello())
'''


# ---------------------------
#module
def myFunc():
    print("Hello World!")
    
    
if __name__ == "__main__":
    #If this code is directly executed by running the file its present in
    print("We are directly running this code")
    
    myFunc()
    print(__name__)