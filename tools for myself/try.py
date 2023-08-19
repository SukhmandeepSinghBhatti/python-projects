from tkinter import *
import speak 

def nn():
    if 'open' in inpu.get():
     speak.speak("Welcome Sir")
     
    import os
    import shutil
    from tkinter.messagebox import showinfo , showerror

    def info():
     showinfo("Mr. Hacker","This is a hacking tool that helps to hack the systems.")

    def ext():
     root.destroy()

    def vs():
      os.startfile("C:\\Users\win 10\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe")
 
    def cmd():
      os.startfile("C:\\Users\\win 10\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System   Tools\\Command Prompt") 

    def jar():
       os.startfile("D:\\Coding\\python projects\\jarvis\\desktop assistance.py")

    def dele():
      shutil.rmtree(aa.get())
      showinfo("Delete","Folder has successfully deleted.")

 
    def dell():
      os.remove(bb.get())
      showinfo("Delete","File has successfully deleted.")

    def sh():
     showinfo("Files and folders", os.listdir())

    def cw():
     showinfo("Correct Working directory", os.getcwd())

root = Tk()
root.geometry("1200x600")
root.title("Mr. Hacker")
root.wm_iconbitmap("ml.ico") 
t = Label(root,text="Lets Start Hacking....",fg="green", bg="black",font="arial 17")
t.pack(fill=BOTH)
f1 = Frame(root,bg="black",height=600)

'''This is one way to test the window look'''

# f1.place(x=5,y=35)
f1.pack(anchor=NW,fill=BOTH)


MenuBar = Menu(root,bg="black",fg="green")
filemenu = Menu(MenuBar, tearoff=0,bg="black",fg="green",font="13")
filemenu.add_command(label="Vs Code",command=vs )
filemenu.add_command(label="Command Prompt",command=cmd)
filemenu.add_command(label="Jarvis",command=jar)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=ext)
MenuBar.add_cascade(label="Tools", menu=filemenu)
root.config(menu=MenuBar)

helpmenu = Menu(MenuBar,tearoff=0,bg="black",fg="green",font="13")
helpmenu.add_command(label="About Us", command=info)
MenuBar.add_cascade(label="Help", menu=helpmenu)

aa = StringVar()
s1 = Entry(f1,textvariable=aa,font="13")

l1 = Label(f1,text="Remove this folder : ",fg="green",bg="black",font="19")
l1.grid(row=0,column=0, padx=6,pady=6)
s1.grid(row=0,column=1,pady=6)
b = Button(f1,text="Delete",command=dele,bg="black",fg="green",font="12")
b.grid(row=0,column=2,padx=6)

bb = StringVar()
l2 = Label(f1,text="Remove this file : ",fg="green",bg="black",font="19")
l2.grid(row=1,column=0,pady=6)
s2 = Entry(f1,textvariable=bb,font="13")
s2.grid(row=1,column=1)
b2 = Button(f1,text="Delete",command=dell,bg="black",fg="green",font="12")
b2.grid(row=1,column=2,padx=6)

b3 = Button(f1,text="Show all file and folders",bg="black",fg="green",font="12",command=sh)
b4 = Button(f1,text="Show correct working directory",bg="black",fg="green",font="12",command=cw)
b3.grid(row=2,column=4,padx=6,pady=6)
b4.grid(row=2,column=5,padx=6,pady=6)


# Add photo in program
photo = PhotoImage(file="body.png")
harman_label = Label(image=photo)
harman_label.place(x=1189,y=20)
root.mainloop()


root = Tk()
root.geometry("1299x699")
root.title("login")
la = Label(root,text="Login",fg="black",font="19")
la.pack()
passv = StringVar()
inpu = Entry(root,textvariable=passv)
inpu.pack()
Button(root,text="click here",command=nn).pack()



root.mainloop()