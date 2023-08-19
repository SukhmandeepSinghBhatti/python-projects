from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename , asksaveasfile, asksaveasfilename
import os


def newFile():
  global file
  root.title("Untitle - Notepad By Sukhman ")
  file = None
  TextArea.delete(1.0,END)
def openFile():
  global file
  file = askopenfilename(defaultextension=".txt",
                         filetypes=[("All Files", "*.*"),
                                    ("Text Documents", "*.txt")])
  if file == "" :
     file = None
  else:
       root.title(os.path.basename(file) + "- Notepad By Sukhman ")
       TextArea.delete(1.0, END)
       f = open(file , "r")
       TextArea.insert(1.0, f.read())
       f.close

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
  root.destroy()
def copy():
   TextArea.event_generate(("<<Copy>>"))
def cut():
   TextArea.event_generate(("<<Cut>>"))
def paste():
   TextArea.event_generate(("<<Paste>>"))
def selctAll():
   TextArea.event_generate(("<<SelectAll>>"))
# def undo():
#    TextArea.event_generate(("<<Undo>>"))
def about():
  showinfo("Notepad","Notepad By Sukhman")
  
if __name__=='__main__':
  
 root = Tk()
 root.geometry("644x788")
#  root.minsize(1200,800)
#  root.maxsize(1000,800)
 root.title("Untitled - Notepad By Sukhman")
 root.wm_iconbitmap("logo.ico") 
# Add Text Area
 TextArea = Text(root, font="lucida 13")
 file = None
 TextArea.pack(expand=True,fill=BOTH)
 
 
 MenuBar = Menu(root)
 filemenu = Menu(MenuBar, tearoff=0)
 filemenu.add_command(label="New", command=newFile , accelerator="Ctrl + N")
 filemenu.add_command(label="Open",command=openFile)
 filemenu.add_command(label="Save",command=saveFile)
 filemenu.add_separator()
 filemenu.add_command(label="Exit",command=quitApp)
 MenuBar.add_cascade(label="File", menu=filemenu)
 root.config(menu=MenuBar)
 Scroll = Scrollbar(TextArea)
 Scroll.pack(side=RIGHT, fill=Y)
 Scroll.config(command=TextArea.yview)
 TextArea.config(yscrollcommand=Scroll.set)
# edit Menu
 editmenu = Menu(MenuBar,tearoff=0)
 editmenu.add_command(label="Cut", command=cut)
 editmenu.add_command(label="Copy", command=copy)
 editmenu.add_command(label="Paste", command=paste)
 editmenu.add_command(label="Select All", command=selctAll)
#  editmenu.add_command(label="Undo", command=undo)
 MenuBar.add_cascade(label="Edit" , menu=editmenu)

 helpmenu = Menu(MenuBar,tearoff=0)
 helpmenu.add_command(label="About Notepad", command=about)
 MenuBar.add_cascade(label="Help", menu=helpmenu)
 
 
 
 root.mainloop()