"""
PAssword Manger Program
Uses:
1- Dictionary
2- loops
3- conditional
4- module: random
5- file handling

website : password
"""
import random
import string
# import os

passwords = {}

# file_path = os.path.join(os.path.dirname(__file__), "passwords.txt")

#load exiting password file
try:
    with open("passwords.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            passwords[website] = pwd
    
except:
    pass

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(chars) for _ in range(8))
    return password

while True:
    print("\n-------PERSONAL PASSWORD MANAGER----------")
    print("1. Save Password")
    print("2. View Password")
    print("3. Genrate Password")
    print("4. Exit")
    
    choice = input("enter your choice: ")
    if choice == "1":
        
        site = input("enter website: ")
        pwd = input("enter password: ")
        
        passwords[site] = pwd
        
        with open("passwords.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")
            
        print("Saved!")
        
    elif choice == "2":
        if not passwords:
            print("No data")
        else:
            for site, pwd in passwords.items():
                print(site,":", pwd)
        
    elif choice == "3":
        print("Generated Password", generate_password())
        
    elif choice == "4":
        print("ok bye..")
        break
    
    else:
        print("In-valid input")