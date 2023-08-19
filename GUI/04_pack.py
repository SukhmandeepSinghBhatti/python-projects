from tkinter import *
from tkinter.messagebox import showinfo

def exitApp():
   root.destroy()
def printa():
   print("Redy")
def helo():
   print("hello user")
def ha():
   showinfo("Help","Press Exit for close app.\n Press print for Redy. \n Press Hello for hello. \n Press help for help.")

root = Tk()
root.geometry("444x233")
root.title("Pycham")
a = Label(text="Ready", font=" 14",bg="red", fg="white", padx=22,pady=22)
a.pack(side=BOTTOM, fill=X)
abb = Button ( root,text="Exit", command=exitApp )
abb.pack(side="left",anchor="nw" )
acc = Button(root,text="Print",command=printa)
acc.pack(side=LEFT,anchor="nw")
add = Button(root,text="Hello", command=helo)
add.pack(side=LEFT,anchor="nw")
aee = Button(root,text="Help", command=ha)
aee.pack(side=LEFT,anchor="nw")


 



root.mainloop()