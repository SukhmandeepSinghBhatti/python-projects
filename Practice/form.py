name = input("Enter your name: ")
marks = input("Enter your marks: ")
a = input("Enter your Class: ")
fn = input("Enter your father name: ")
sentence = f"The name of the student is {name} son of {fn} student of {a} class and his marks is {marks}."
# print(sentence.format(name,a,marks))
with open("form data.txt", "a") as f:
    d = f.write(str(sentence))
    f.write('\n')