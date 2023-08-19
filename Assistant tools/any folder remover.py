import shutil
import os
print(os.listdir())
a = input("Enter the name of folder you want to remove: ")
shutil.rmtree(a)

