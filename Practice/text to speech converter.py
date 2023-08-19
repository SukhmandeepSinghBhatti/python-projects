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
f1 = Frame(body,padx=22,pady=44)
f1.place(x=20,y=40)
tittle = Label(body,text="Text To Speech Converter",font="arial 20 bold",bg="grey")
tittle.pack(fill=BOTH)
main = Label(f1,text="Enter the text here",font='12')
ss = StringVar()
user = Entry(f1,textvariable=ss)
swith = Button(f1,text="Convert",command=starting)

main.grid(row=0,column=1)
user.grid(row=0,column=2)
swith.grid(row=0,column=3)







root.mainloop()

