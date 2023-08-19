from tkinter import *
import speak 

def nn():
    if 'open' in inpu.get():
     speak.speak("Welcome Sir")
     root.destroy()
     a = Tk()
     a.geometry("1200x600")
     a.mainloop()
    elif "" in inpu.get():
       speak.speak("Enter Your password")
    else:
       speak.speak("Wrog password, Please Enter the correct password.")
root = Tk()
root.geometry("1299x699")

root.title("login")
la = Label(root,text="Login",fg="black",font="19")
la.pack(pady=10)
passv = StringVar()
inpu = Entry(root,textvariable=passv)
inpu.pack(pady=10)
Button(root,text="log In",command=nn).pack()



root.mainloop()