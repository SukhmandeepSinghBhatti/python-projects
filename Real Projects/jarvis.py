import os
import webbrowser
import time
import pyttsx3
import datetime
import wikipedia
from tkinter import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning!')
    elif hour >= 12 and hour <18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    # speak("I am Jarvis Sir. Please tell me may I help you ")

talk = "Talk with me"

url = "https://www.youtube.com//"

t = time.ctime()


# print("*********************************************")
# wishMe()

def  mainwork():
         
      user = Entry(f1,textvariable=ee)
      if "exit" in user.get().lower():
            #   print("***Byee , Have a nice day ***")
              speak("***Byee , Have a nice day ***")
              root.destroy()
            #   print('**************************')
              
      elif "byee" in user.get().lower():
            #   print("***Byee , Have a nice day ***")
              speak("***Byee , Have a nice day ***")
              root.destroy()
            #   print('**************************')
              
     
      elif "open youtube" in user.get().lower():
               speak("Opening Youtube")
               webbrowser.open(url) 
      elif "open chrome" in user.get().lower():
             speak("Opening Chrome")
             os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
      elif "open notepad" in user.get().lower():
             speak("Opening Notepad")
             os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad")
      elif "play music" in user.get().lower():
              speak("playing music")
              os.startfile("hello.xspf")
      elif "open kacfb" in user.get().lower():
             speak("Opening sir")
             os.startfile("D:\KACFB")
      elif "open cmd" in user.get().lower():
             speak("Opening CMD")
             os.startfile("C:\\Users\\win 10\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt")
      elif "open 10th class" in user.get().lower():
             os.startfile("D:\\10th Class")
           
      elif "open vscode" in user.get().lower():
              speak("Opening Vs Code")
              os.startfile("C:\\Users\win 10\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe")
      elif "open cwd" in user.get().lower():
              speak("Opening correct working directory")
              os.startfile(cwd)
             


      else:
       # print(qs[user.get().lower()])
       speak((qs[user.get().lower()]))


   

root = Tk()
root.geometry("600x400")
root.maxsize(600,400)
root.minsize(600,400)
root.wm_iconbitmap("head.ico") 
root.title("Jarvis Desktop Assistant")

body = (root)
lavle = Label(root,text="Jarvis Desktop Assistant",font="arial 30",bg="grey")
lavle.pack(fill=BOTH)

f1 = Frame(body,padx=100,pady=110)
f1.place(x=66,y=66)

you = Label(f1,text="You : ",font="35")
you.grid(row=1,column=0)

# Entries 
ee = StringVar()
user = Entry(f1,textvariable=ee,font="30")
user.grid(row=1,column=1)

aa = StringVar()
jarvissaid = Label(f1,text="Jarvis : ",font="30")
jarvissaid.grid(row=3,column=0)
jarvis = Entry(f1,textvariable=aa,font="30",)
jarvis.grid(row=3,column=1)

b1 = Button(f1,text="Send message",command=mainwork)
b1.grid(row=1,column=2)

# photo = PhotoImage(file="")
# img_label = Label(f1,image=photo)
# img_label.grid(row=2,column=0)

LEFTarea = Label(root,bg="grey",padx=9)
RIGHTarea = Label(root,bg="grey",padx=9)
BOTTOMarea = Label(root,bg="grey",padx=9)

LEFTarea.pack(side=LEFT,fill=BOTH)
RIGHTarea.pack(side=RIGHT,fill=BOTH)
BOTTOMarea.pack(side=BOTTOM,fill=BOTH)



qs = {
 "hello":"Hello How Can I Help You ? ",
 "what s the time": t,
 "what is your name": "My name is jarvis your assistant.",
 "who are you": "I am jarvis your assistant.",
 "how can you do it": "I tell you time, open youtube,open vscode , for more informantion type help  and talk with you.",
 "i love you" : "I love you too ",
 "how are you": "I am fine tell about your self.",
 "i am fine": "Ok",
 "go for a walk": "No because i am busy now.",
 "thanks": "Your welcome",
 "hai": "hello",
 "today i fall in gutter": "haa haa haa",
 "": talk ,
 "help": "Type open vscode for open vscode , type open youtube for open youtube , type open cmd for open cmd , type play music for playing music , type open chrome for open chrome , type open notepad for open notepad , type open kacfb for open knowlage about computer from books folder , type open 10th class for open 10th class folder",
 "fathee": "waheguru ji ka khalsa waheguru ji ki fathee",
 "sing a song": "jina naal tu compare kare sadhe level de ni hardia",
 'where are you live': "i live in your pc also",
 "who is your friend": "sukhmmandeep singh is my best friend.",
 "who are your creater": "Sardar sukhmmandeep singh ji is my creater . "

}

speak("Hello everyone")
text = "I am Jarvis. Please tell me may I help you "
# print(text)
speak(text)
# speak("Type help for help")
# speak("Please tell me your name sir.")
# b = input("Tell me your name: ")
# print("Hello, " + b + " How are you ?")
speak("Hello, How are you ?")

cwd = os.getcwd()

root.mainloop()
