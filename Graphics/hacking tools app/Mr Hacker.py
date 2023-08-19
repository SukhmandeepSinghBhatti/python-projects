from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename , asksaveasfilename



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

def newFile():
  global file
  root.title("Untitle - Notepad By Sukhman ")
  file = None
  bg1.delete(1.0,END)
def openFile():
  global file
  file = askopenfilename(defaultextension=".txt",
                         filetypes=[("All Files", "*.*"),
                                    ("Text Documents", "*.txt")])
  if file == "" :
     file = None
  else:
       root.title(os.path.basename(file) + "- Mr. Hacker ")
       bg1.delete(1.0, END)
       f = open(file, "r")
       bg1.insert(1.0, f.read())
       f.close

def saveFile():
   global file
   if file == None:
      file = asksaveasfilename(initialfile="Untitled ",defaultextension=".txt",
                         filetypes=[("All Files", "*.*"),
                                    ("Text Documents", "*.txt")])
      if file == "":
           file = None
      else:
         f = open(file,"w")
         f.write(bg1.get(1.0, END))
         f.close

         root.title(os.path.basename(file) + "- Mr. Hacker")
   else:
       f = open(file,"w")
       f.write(bg1.get(1.0, END))
       f.close

       root.title(os.path.basename(file) + "- Notepad By Sukhman")
def quitApp():
  root.destroy()
def copy():
   bg1.event_generate(("<<Copy>>"))
def cut():
   bg1.event_generate(("<<Cut>>"))
def paste():
   bg1.event_generate(("<<Paste>>"))
def sa():
     bg1.event_generate(("<<SelectAll>>"))
def about():
  showinfo("Mr. Hacker","This program is hacking tool.")


if __name__=='__main__':
 root = Tk()
root.geometry("636x333")
root.title("Mr. Hacker")
root.wm_iconbitmap("ml.ico") 


T = Label(text="Lets start hacking....",fg="green",bg="black",font="55",pady=23)
T.pack(fill=X)
body = Label(root,bg="black")
aaa = Label(body,bg="black")
aaa1 = Label(body,bg="black")
# bg1 = Label(bg="blue",height=1200,width=12000)
bg1 = Text(bg="black",height=100,width=12000,fg="green",font="lucida 25")

file = None
bg1.pack(expand=True,fill=BOTH)
 
 
MenuBar = Menu(body)
filemenu = Menu(MenuBar, tearoff=0)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open",command=openFile)
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quitApp)
MenuBar.add_cascade(label="File", menu=filemenu)
root.config(menu=MenuBar)
Scroll = Scrollbar(bg1)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=bg1.yview)
bg1.config(yscrollcommand=Scroll.set)

# Scroll = Scrollbar(bg1)
# Scroll.pack(side=BOTTOM, fill=X)
# Scroll.config(command=bg1.xview)
# bg1.config(xscrollcommand=Scroll.set)
# edit Menu
editmenu = Menu(MenuBar,tearoff=0)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)
editmenu.add_command(label="Select All", command=sa)
MenuBar.add_cascade(label="Edit" , menu=editmenu)


helpmenu = Menu(MenuBar,tearoff=0)
helpmenu.add_command(label="About Mr. Hacker", command=about)
MenuBar.add_cascade(label="Help", menu=helpmenu)
 
 
 


bg = Image.open("body.png")
bck = ImageTk.PhotoImage(bg)
# gb = Label(bg="black",height=111)

body_img = Label(aaa1,image=bck)
body_img.pack()
body.pack(fill=BOTH)
# gb.pack()


bg1.pack(side=BOTTOM,pady=1)
Button1 = Button(aaa1,text="Show correct working dir",command=b1)
Button1.pack()
allinone = Button(aaa,text="Show all files and folders", command=allfile)
allinone.pack()
search = StringVar()
sl = Entry(aaa, textvariable=search)
sl.pack(pady=5)

a = Button(aaa,text="Delete", command=dell )



aaa1.pack(anchor=NE,pady=2,padx=600)
aaa.pack(anchor=NE,pady=2,padx=600)
a.pack()
create = StringVar()
s2 = Entry(aaa,textvariable=create)
s2.pack(pady=5)
sukbuttonhmanda = Button(aaa,text="Create the file",command=createa)
sukbuttonhmanda.pack()
root.mainloop()
