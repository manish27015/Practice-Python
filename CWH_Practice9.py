"""
a = "a very log string with emails"
emails = []
3 seconds
"""
# (         r = reading             )
# f = open("superman.txt")
# data = f.read()
# print(data)
# f.close()

# (         a = appending             )
 
# st = " Hey Harry you are amazing."
# f = open("superman.txt", "a")
# f.write(st)
# f.close()

#(          w = writing                 )

# r = open("superman.txt",'w')
# r.write("Hello this akarsh and i am writing inside this file ")
# r.close()

# +  - open for updating. 
# ‘rb’ will open for read in binary mode. 
# ‘rt’ will open for read in text mode. 


# f = open("file.txt")
# print(f.read())
# f.close()

# The same can be written using with statement like this:

# with open("file,txt") as f:
#     print(f.read())

#We dont have to explicity close the file

""""""""""""""""""""""""
'''
Write a program to read the text from a given file ‘poems.txt’ and find out 
whether it contains the word ‘twinkle’. 
'''
"""
f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("The word twinkle is present in the content")

else:
    print("The word twinkle is not present in the content ")\
    

f.close()
"""

"""
The game() function in a program lets a user play a game and returns the score 
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
contains the previous Hi-score. You need to write a program to update the Hi
score whenever the game() function breaks the Hi-score."""
'''
import random

def game():
    print("You are playing the game....")
    score =  random.randint(1,62)
    #fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore != "" ):
            hiscore=int(hiscore)
        else:
            hiscore = 0
            
    print(f"Your score: {score})")
    if(score>hiscore):
        #write this hiscore too the file
        with open("hiscore.txt", 'w')as f:
            f.write(str(score))
    
    return score

game()
'''

"""Write a program to generate multiplication tables from 2 to 20 and write it to the 
different files. Place these files in a folder for a 13 – year old."""
"""
def generateTable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
        
    with open(f"tables/table_{n}.txt", 'w') as f:
        f.write(table)
            
for i in range(2,21):
    generateTable(i)
"""

"""A file contains a word “Donkey” multiple times. You need to write a program 
which replace this word with ##### by updating the same file. """
'''
word = "Donkey"

with open ("myfile.txt", "r") as f:
    content = f.read()
    
contentNew = content.replace(word, "######")

with open("myfile.txt", "w") as f:
    f.write(contentNew)
    '''
#Repeat program 4 for a list of such words to be censored.
"""
words = ["Donkey", "Bad", "ganda"]

with open ("myfile.txt", "r") as f:
    content = f.read()
    
for word in words:
    content = content.replace(word, "#"*len(word))

with open("myfile.txt", "w") as f:
    f.write(content)
    """
# Write a program to mine a log file and find out whether it contains ‘python’.
"""
with open("log.html") as f:
    content = f.read()
    
if("Python" in content):
    print("Yes Python is present")
else:
    print("No Python is not present")
    
"""

#Write a program to find out the line number where python is present from ques 6. 
"""
with open("log.html") as f:
    lines = f.readlines()
    
lineno = 1
for line in lines:
    if("Python" in line):
        print(F"Yes Python is present. Line no: {lineno}")
        break
    lineno += 1
else:
    print("No Python is not present")
"""
#Write a program to make a copy of a text file “myfile.txt” 
"""
with open("myfile.txt") as f:
    content = f.read()
    
with open ("myfile_copy.txt", "w") as f:
    f.write(content)    
"""
'''
Write a program to find out whether a file is identical & matches the content of 
another file. '''
"""
with open("myfile.txt") as f:
    content1 = f.read()

with open("poem.txt")as f:
    content2 = f.read()

if(content1==content2):
    print("Yes these files are identical")
else:
    print("No these files are not identical")
    """
# Write a program to wipe out the content of a file using python. 

"""
with open("myfile_copy.txt", "w") as f:
    f.write("")
    
"""
#Write a python program to rename a file to “renamed_by_ python.txt.

with open("old.txt") as f:
    content = f.read()

with open("renamed_by_python.txt", "w")as f:
    f.write(content)