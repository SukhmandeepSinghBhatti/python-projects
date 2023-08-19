import os
a = os.listdir()
print(a)
r = input("Enter the name of folder that you remove: ")
s = os.rmdir(r)
print(a)