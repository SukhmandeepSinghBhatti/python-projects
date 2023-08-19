a = input("Enter your name: ")
c = "Good morning, "+ a
print(c)
with open("data1.txt","a") as f:
    b = f.write((c))
    f.write("\n")