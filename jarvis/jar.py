import os
import webbrowser
import time
import gtts
import pyttsx3
import datetime
from qtpy import QtGui, QtWidgets, QtCore
print(QtWidgets.QWidget)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
# print('**************************')
# text = "Hello, I am Jarvis and  How Can I Help You ? "
# speak(text)









# url = "https://www.youtube.com/"

# t = time.ctime()

# qs = {
#  "hello":"Hello, How Can I Help You ? ",
#  "what is the time": t,
#  "what is your name": "My name  jarvis your assistant.",
#  "how can you do it": "I tell you time, open youtuve,open vscode and talk with you."
# }
# while True:
         
#       a = input("You: ")
    
#       if "exit" in a.lower():
#               speak("***Thanks, Have a nice day***")
#               break
#       elif "open youtube" in a.lower():
#                webbrowser.open(url) 
# #       elif "open Google"in a.lower():
# #            webbrowser.open()
             
#       elif "open vscode" in a.lower():
#               os.startfile("C:\\Users\win 10\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe")
#       else:
#         speak({(qs[a])})

