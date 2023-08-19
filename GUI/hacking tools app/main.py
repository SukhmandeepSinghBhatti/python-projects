from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import messagebox



def b1():
    # print(os.listdir())
    messagebox.showinfo("Correct working directory", os.getcwd())
def dell():
 os.remove(  search.get() )
def allfile():
  messagebox.showinfo("Files and Folders",os.listdir())

def createa():
  with open (create.get(),"a") as f:
    b = f.write()

if __name__=='__main__':
 root = Tk()
root.geometry("636x333")
root.title("Mr. Hacker")

body = Label(bg="black",fg="white",height=111) 
aaa = Label(body,bg="black")
aaa1 = Label(body,bg="black")
bg1 = Label(bg="black",height=1200,width=12000)


root.wm_iconbitmap("ml.ico") 
bg = Image.open("body.png")
bck = ImageTk.PhotoImage(bg)
gb = Label(body,bg="black",height=111)

body_img = Label(root,image=bck)
body_img.place(x=0, y=0)
body.pack(fill=BOTH)
gb.pack()

T = Label(gb,text="Lets start hacking....",fg="green",bg="black",font="55",pady=23)
T.pack()
bg1.pack(pady=1)
Button1 = Button(aaa1,text="Show correct working diractory",command=b1)
Button1.pack()
allinone = Button(aaa,text="Show all files and folders", command=allfile)
allinone.pack()
search = StringVar()
sl = Entry(aaa, textvariable=search)
sl.pack(pady=5)

a = Button(aaa,text="Delete", command=dell )



aaa1.pack(anchor=NE,pady=2,padx=7)
aaa.pack(anchor=NE,pady=2,padx=7)
a.pack()
create = StringVar()
s2 = Entry(aaa,textvariable=create)
s2.pack(pady=5)
sukbuttonhmanda = Button(aaa,text="Create the file",command=createa)
sukbuttonhmanda.pack()
root.mainloop()
