import requests

url = input("Enter the url of image here: ")
file = input('Enter the name of the file: ')
with open(file,"wb")as f:
    a = f.write(requests.get(url).content)

