import shutil
import os

print(os.listdir())

copy = input("Enter the name of file you want to copy: ")
newname = input("Enter the name of the new file: ")

shutil.copyfile(copy,newname)

print("file copied...")