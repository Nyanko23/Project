# Part 1 - 4
f = open("myContact.txt")
print(f)
f = open("myContact.txt", 'w')    #write in text mode
# f = open("README.md", 'r+b')      #read and write in binery mode

f = open("myContact.txt", mode ='w', encoding= 'utf-8')
print(f)

f.close()

try:
    f = open("myContact.txt", encoding = 'utf-8')
    # perform file operations
    print(f.readlines())
except:
       print("Error")
finally:
     f.close()

