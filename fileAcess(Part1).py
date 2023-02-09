# part 5 onwards
try:
    f = open("myContact.txt", encoding = 'utf-8')
    # perform file operations
    print(f.readlines())
except:
       print("Error")
finally:
     f.close()

with open("test.txt", 'w', encoding = 'utf-8') as f:
    f.write("my first file\n ")
    f.write("This file\n\n")
    f.write("contains three lines\n")

with open("test.txt", 'r', encoding = 'utf-8') as f:
    print(f.read())

import fnmatch
import os

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.txt'):
        print(file)
















































































































































































































































































































































































































































































































































