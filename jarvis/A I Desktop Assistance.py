import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import random
import os
import time
from pytube import Playlist
from pytube import YouTube
import openai
from config import api_key
from ai_jarvis import reply

chatstr = ""
def chat(quary):
    global chatstr
    openai.api_key = api_key
    chatstr += f"Sukhman: {quary}",
    
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
     prompt = chatstr,
     messages=[
     {
       "role": "system",
       "content": "write a email to my boss for my rejoin "
     },
     {
       "role": "user",
       "content": ""
     }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    speak(response ["choices"] [0] ["text"])
    chatstr += f"{response ['choices'] [0] ['text']}"
    return f"{response ['choices'] [0] ['text']}"
    
     
def ai(prompt):
     openai.api_key = api_key
     text = f"Openai response for prompt: {prompt}\n******************\n\n"
    
     response = openai.ChatCompletion.create(
     model="gpt-3.5-turbo",
     prompt = prompt,
     messages=[
     {
       "role": "system",
       "content": "write a email to my boss for my rejoin "
     },
     {
       "role": "user",
       "content": ""
     }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
     print(response ["choices"] [0] ["text"])
     text += response ["choices"] [0] ["text"]
     if not os.path.exists("Openai files"):
          os.mkdir('Openai files')
     with open(f"Openai files/promt{random.randint(1,23456789001245)}.txt","w") as f:
          f.write(text)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

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
    speak("I am Jarvis Sir. Please tell me may I help you ")

def takeCommand():
    # it takes microphone input from the user and return the string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        quary = r.recognize_google(audio, language="en-in")
        print(f"User said: {quary}\n")
    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"
    return quary

cwd = os.getcwd()
talk = "Talk with me"
url = "https://www.youtube.com//"
t = time.ctime()
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
 "help": "Type open vscode for open vscode , type open youtube for open youtube , type open cmd for open cmd , type play music for playing music , type open chrome for open chrome , type open notepad for open notepad , type open kacfb for open knowlage about computer from books folder , type open 10th class for open 10th class folder type open coding for open coding folder , type show show questions or show all questions. ", 
 "fathee": "waheguru ji ka khalsa waheguru ji ki fathee",
 "sing a song": "jina naal tu compare kare sadhe level de ni hardia",
 'where are you live': "i live in your pc also",
 "who is your friend": "sukhmmandeep singh is my best friend.",
 "who create you": "Sardar sukhmmandeep singh ji is my creater . ",
 "when was sukhman born":"Sukmandeep  Singh  was born on 7th August 2007.",
 "ten guru": "Shri guru nanak dev ji , shri guru angad dev ji , shri guru amardas ji , shri guru ramdas ji , shri guru arjan dev ji , shri guru hergobind saheb ji , shri guru her rai saheb ji , shri guru her krishan saheb ji , shri guru teg bahadur sahib ji , shri guru gobind singh ji , shri guru granth saheb ji",
"who was harman": "harmandeep singh is your younger brother.",
"who was manjinder": "manjinder kaur is your mother",
"who was jagdeep": "jagdeep singh is your father",
"family info": "you are sukhandeep singh , harmandeep singh is your younger brother , manjinder kaur is your mother, jagdeep singh is your father,"
}

if __name__=="__main__":
    speak("waheguru ji ka khalsa waheguru ji ki fathee")
    wishMe()
   
    while True:
        quary = takeCommand().lower()
        if "wikipedia" in quary:
            speak("Searching wikipedia...")
            print("Searching Wikipedia....")
            quary = quary.replace("wikipedia","")
            results = wikipedia.summary(quary,sentences=2)
            print("According to wikipedia")
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "hello" in quary:
                speak("hello, how are you")
        elif "open youtube" in quary:
                speak("opening youtube")
                webbrowser.open("youtube.com")
        elif "open google" in quary:
                speak("opening google")
                webbrowser.open("google.com")
        elif "play music" in quary:
                speak("playing music")
                os.startfile("hello.xspf")
        elif "the time" in quary:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             print(f"Sir, the time is {strTime}")
             speak(f"Sir, the time is {strTime}")
        elif "open folder" in quary:
             speak("Opening sir")
             os.startfile("D:\KACFB")
        elif "open chrome" in quary:
             speak("Opening Chrome")
             os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        elif "open notepad" in quary:
             speak("Opening Notepad")
             os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad")
        elif "open cmd" in quary:
             speak("Opening CMD")
             os.startfile("C:\\Users\\win 10\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt")
        elif "open 10th class" in quary:
             os.startfile("D:\\10th Class")
        elif "open code" in quary:
              speak("Opening Vs Code")
              os.startfile("C:\\Users\win 10\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe")
        elif "open cwd" in quary:
              speak("Opening correct working directory")
              os.startfile(cwd)
        elif "quit" in quary:
                print("*** Byee , Have a nice day ***")
                speak("*** Byee , Have a nice day ***")
                exit()
        elif "Using artificial intelegence" in quary:
             ai(prompt=quary)
             print(ai)
        elif 'download this playlist' in quary:
             speak('enter the url of the playlist here')
             py = Playlist(input("\t ---> "))
             print(f"Downloading : {py.title} ")
             speak(f"Downloading : {py.title} ")
             for video in py.videos:
               video.streams.first().download()
             print('Downloading Completed')
             speak('Downloading Completed')
        elif "download this video" in quary:
           speak("enter the url of the video here")
           link = input('\t ---> ')
           YouTube_1 = YouTube(link)
           videos = YouTube_1.streams.all()
           vid =list(enumerate(videos))
           for i in vid:
              print(i)
           print()
           strm = int(input("\t $ ---> "))
           videos[strm].download()
           print("Video Sucessfully Downloaded")
           speak("Video Sucessfully Downloaded")
        elif 'chat' in quary:
              print('Start chatting....')
              speak('start chatting')
              while True:
                 you = f"Chatting: {takeCommand()}"
                 a = reply(you)
                 print(a)
                 speak(a)
                 if 'exit' in you:
                    speak("Byee")
                    print("Byee")
                    break
        elif "open a website" in quary:
             speak("tell me the name of website")
             print("Tell me the name of website")
             li = takeCommand()
             speak(f"openning {li}.com")
             print(f"Openning {li}.com")
             webbrowser.open(f"{li}.com")
        elif 'shutdown' in quary:
             speak('Alert! System Shutdowning...')
             os.startfile("shutdown.exe.link")
        elif "thanks" in quary:
             speak("welcome sir")
             print("Welcome Sir")
        elif "open my blog" in quary:
             speak('openning your blogs')
             print('Openning your Blogs')
             webbrowser.open('learncomputerwithsukhman.blogspot.com')
             webbrowser.open('computerinformationbysukhman.blogspot.com')
        elif "open blogger" in quary:
             speak('sir openning your blogs')
             webbrowser.open("https://draft.blogger.com/blog/posts/8794564774624530129")
        elif 'open my youtube channel' in quary:
             speak('Sir openning your youtube channel')
             webbrowser.open("https://www.youtube.com/channel/UCmaugrMU8fg5inZVOeaMdiQ")
        else:
             pass
       