from tkinter import *
import os
from tkinter.messagebox import showinfo 

def info():
 showinfo("Mr. Hacker","This is a hacking tool that helps to hack the systems.")

def ext():
 root.destroy()

def vs():
 os.startfile("C:\\Users\win 10\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe")
 
def cmd():
   os.startfile("C:\\Users\\win 10\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt") 

def jar():
    os.startfile("D:\\Coding\\python projects\\Real Projects\\exe files\\dist\\jarvis.exe")



root = Tk()
root.geometry("1200x600")
root.title("Mr. Hacker")
root.wm_iconbitmap("ml.ico") 
t = Label(root,text="Lets Start Hacking....",fg="green", bg="black",font="arial 17")
t.pack(fill=BOTH)
f1 = Frame(root,bg="blue")

'''This is one way to test the window look'''

# f1.place(x=5,y=35)
f1.pack(anchor=NW,fill=BOTH)


MenuBar = Menu(root)
filemenu = Menu(MenuBar, tearoff=0)
filemenu.add_command(label="Vs Code",command=vs )
filemenu.add_command(label="Command Prompt",command=cmd)
filemenu.add_command(label="Jarvis",command=jar)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=ext)
MenuBar.add_cascade(label="More", menu=filemenu)
root.config(menu=MenuBar)

helpmenu = Menu(MenuBar,tearoff=0)
helpmenu.add_command(label="About Us", command=info)
MenuBar.add_cascade(label="Help", menu=helpmenu)
root.mainloop()
