from tkinter import *
import speak 
import os

def nn():
    with open("pass.txt") as f:
       r = f.read()
       
    if r in inpu.get():
     speak.speak("Welcome Sir")
     root.destroy()
   #   os.startfile("D:\\Coding\\python projects\\Gift\\tools for myself\\main.py")
    #  os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
     os.startfile("D:\\songs")


   #   a = Tk()
   #   a.title("data base")
   #   a.geometry("1200x600")
    
   #   a.mainloop()
    elif "" in inpu.get():
       speak.speak("Enter Your password")
    else:
       speak.speak("Wrog password, Please Enter the correct password.")
root = Tk()
root.geometry("1299x699")
root.maxsize(600,300)

root.title("login")
la = Label(root,text="Login",fg="white",font="bold 20",bg="black")
la.pack(fill=BOTH,pady=10)

passv = StringVar()
inpu = Entry(root,textvariable=passv)
inpu.pack()
Button(root,text="log In",command=nn).pack(pady=4)



root.mainloop()