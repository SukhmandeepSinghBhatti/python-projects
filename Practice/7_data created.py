import os
d = (os.listdir()) # This line print all the  file of dirictory
print (d)
with open("data.txt","a") as f:
    a = f.write(str(d))




