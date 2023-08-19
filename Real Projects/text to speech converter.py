import pyttsx3
from tkinter import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def starting():
    speak(user.get())
  
       
        
   

root =   Tk()
root.geometry("600x300")
root.maxsize(600,300)
root.wm_iconbitmap("app_logo.ico") 
root.title("Text To Speech Converter")


body = (root)
f1 = Frame(body,padx=99,pady=110,bg="black")
f1.place(x=20,y=40)
tittle = Label(body,text="Text To Speech Converter",font="arial 20 bold",bg="black",fg="white")
tittle.pack(fill=BOTH)
main = Label(f1,text="Enter the text here: ",font='14' ,bg="skyblue",padx=4)
ss = StringVar()
user = Entry(f1,textvariable=ss,font="14")
swith = Button(f1,text="Convert",command=starting,bg="yellow",padx=3)

main.grid(row=0,column=1)
user.grid(row=0,column=2)
swith.grid(row=0,column=3)

leftarea = Label(root,bg="black",pady=4,padx=15)
RIGHTarea = Label(root,bg="black",pady=4,padx=15)
BOTTOMarea = Label(root,bg="black",pady=4,padx=15,text="Created By : Sukhmandeep Singh",font="18",fg="white")
leftarea.pack(fill=BOTH,side=LEFT)
RIGHTarea.pack(fill=BOTH,side=RIGHT)
BOTTOMarea.pack(fill=BOTH,side=BOTTOM)





root.mainloop()

