from tkinter import *
from PIL import ImageTk,Image
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename , asksaveasfile
import os

   


def newFile():
  global file
  root.title("Untitle - Notepad By Sukhman ")
  file = None
  a1.delete(1.0,END)
def openFile():
  global file
  file = askopenfilename(defaultextension=".txt",
                         filetypes=[("All Files", "*.*"),
                                    ("Text Documents", "*.txt")])
  if file == "" :
     file = None
  else:
       root.title(os.path.basename(file) + "- Mr.Hacker ")
       a1.delete(1.0, END)
       f = open(file, "r")
       a1.insert(1.0, f.read())
       f.close

def saveFile():
   global file
   if file == None:
      file = asksaveasfile(initialfile="Untitled.txt ",defaultextension=".txt",
                         filetypes=[("All Files", "*.*"),
                                    ("Text Documents", "*.txt")])
      if file == "":
           file = None
      else:
         f = open(file,"w")
         f.write(a1.get(1.0, END))
         f.close

         root.title(os.path.basename(file) + "- Mr.Hacker")
   else:
       f = open(file,"w")
       f.write(a1.get(1.0, END))
       f.close

       root.title(os.path.basename(file) + "- Mr.Hacker")
def quitApp():
  root.destroy()
def copy():
   a1.event_generate(("<<Copy>>"))
def cut():
   a1.event_generate(("<<Cut>>"))
def paste():
   a1.event_generate(("<<Paste>>"))
def about():
         showinfo("Notepad","Notepad By Sukhman") 

def sukh():
   b.destroy()

def dba():

   a1 = Text(body,font="arial 20", fg="green",bg="black")
   a1.pack(expand=True,fill=BOTH)
   file = None

   
   MenuBar = Menu(root)
   filemenu = Menu(MenuBar, tearoff=0)
   filemenu.add_command(label="New", command=newFile)
   filemenu.add_command(label="Open",command=openFile)
   filemenu.add_command(label="Save",command=saveFile)
   filemenu.add_separator()
   filemenu.add_command(label="Exit",command=quitApp)
   MenuBar.add_cascade(label="File", menu=filemenu)
   root.config(menu=MenuBar)
   Scroll = Scrollbar(a1)
   Scroll.pack(side=RIGHT, fill=Y)
   Scroll.config(command=a1.yview)
   a1.config(yscrollcommand=Scroll.set)
# edit Menu
   editmenu = Menu(MenuBar,tearoff=0)
   editmenu.add_command(label="Cut", command=cut)
   editmenu.add_command(label="Copy", command=copy)
   editmenu.add_command(label="Paste", command=paste)
   MenuBar.add_cascade(label="Edit" , menu=editmenu)

   helpmenu = Menu(MenuBar,tearoff=0)
   helpmenu.add_command(label="About Notepad", command=about)
   MenuBar.add_cascade(label="Help", menu=helpmenu)


root = Tk()
root.geometry("600x300") 
root.title("Mr. Hacker")
root.wm_iconbitmap("ml.ico") 

body = (root)
title = Label(root,text="Lets Start hacking....",fg="green",bg="black",font="arial 20 bold")
title.pack(fill=BOTH)
f1 = Frame(body,bg="red",border=4)
f1.pack(side=TOP, anchor=NW)

b =Button(f1,text="Open Text Editor",command=dba)
b.pack()
# b2 = Button(f1,text="Close Text Editor", command=sukh)
# b2.pack()
a1 = Text(f1,)
# a1.pack(expand=True,fill=BOTH)
file = None


 
 
 

f2 = Frame(body,bg="green")
f2.place(x=1000,y=150)

a2 = PhotoImage(file="body.png")
harman_label = Label(f2,image=a2,bg="black")
harman_label.pack()


file = None

 
MenuBar = Menu(root)
filemenu = Menu(MenuBar, tearoff=0)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open",command=openFile)
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quitApp)
MenuBar.add_cascade(label="File", menu=filemenu)
root.config(menu=MenuBar)
Scroll = Scrollbar(a1)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=a1.yview)
a1.config(yscrollcommand=Scroll.set)
# edit Menu
editmenu = Menu(MenuBar,tearoff=0)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)
MenuBar.add_cascade(label="Edit" , menu=editmenu)

helpmenu = Menu(MenuBar,tearoff=0)
helpmenu.add_command(label="About Notepad", command=about)
MenuBar.add_cascade(label="Help", menu=helpmenu)
 
 
 





root.mainloop()