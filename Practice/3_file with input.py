import os
c = input("Enter the text: ")
with open("data of input.txt","a") as f:
    k = f.write((c))
    f.write('\n')