import os 
o = os.listdir()
print(o)
a = input(("Enter the name of file that you create: "))
d = input("Enter the text:  ")
with open(a,"a") as f:
    b = f.write(d)