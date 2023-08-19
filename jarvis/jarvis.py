import os
import webbrowser
import time
import pyttsx3
import datetime
import wikipedia

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

print("*********************************************")
# wishMe()
speak("Hello everyone")
text = "I am Jarvis. Please tell me may I help you "
print(text)
speak(text)
# speak("Type help for help")
speak("Please tell me your name sir.")
b = input("Tell me your name: ")
print("Hello, " + b + " How are you ?")
speak("Hello, " + b + " How are you ?")

cwd = os.getcwd()
# print(cwd)







talk = "Talk with me"

url = "https://www.youtube.com//"

t = time.ctime()

qs = {
 "hello":"Hello How Can I Help You ? ",
 "what s the time": t,
 "what is your name": "My name is jarvis your assistant.",
 "who are you": "I am jarvis your assistant.",
 "how can you do it": "I tell you time, open youtube,open vscode , for more informantion type help  and talk with you.",
 "i love you" : "I love you too "+ b,
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
 "who is your friend": "sukhmmandeep singh is my best friend.",
 "who are your creater": "Sardar sukhmmandeep singh ji is my creater . "
}
while True:
         
      a = input("You: ")
      if "exit" in a.lower():
              print("***Byee , Have a nice day ***")
              speak("***Byee , Have a nice day ***")
            #   print('**************************')
              break
      elif "byee" in a.lower():
              print("***Byee , Have a nice day ***")
              speak("***Byee , Have a nice day ***")
            #   print('**************************')
              break
     
      elif "open youtube" in a.lower():
               speak("Opening Youtube")
               webbrowser.open(url) 
      elif "open chrome" in a.lower():
             speak("Opening Chrome")
             os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
      elif "open notepad" in a.lower():
             speak("Opening Notepad")
             os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad")
      elif "play music" in a.lower():
              speak("Playing Music")
              os.startfile("hello.xspf")
      elif "open kacfb" in a.lower():
             speak("Opening sir")
             os.startfile("D:\KACFB")
      elif "open cmd" in a.lower():
             speak("Opening CMD")
             os.startfile("C:\\Users\\win 10\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt")
      elif "open 10th class" in a.lower():
             os.startfile("D:\\10th Class")
           
      elif "open vscode" in a.lower():
              speak("Opening Vs Code")
              os.startfile("C:\\Users\win 10\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe")
      elif "open cwd" in a.lower():
              speak("Opening correct working directory")
              os.startfile(cwd)
             


      else:
       print (f"jarvis: {(qs[a])}")
       speak((qs[a]))

   
