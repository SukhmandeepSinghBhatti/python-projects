import shutil
import os 
import time
import pyttsx3
import webbrowser
import wikipedia
from pytube import Playlist
from pytube import YouTube
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voices",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

w = os.getcwd()

with open('user.txt',"r") as f:
     u = f.read()
while True:
  
   with open('pass.txt',"r") as f:
     e = f.read()
  
   user = input('Enter your User Name: ')
   a = input("Enter Your Password: ")
   if u in user:
    if e in a:
       speak('welcome sir')
       print('Welcome Sir')
       print("==================================================================================================")
       
       while True:
          entry = input(f"{os.getcwd()}> $ ").lower()
          try:
            if 'cwd' in entry:
               print(os.getcwd())

            elif "exit" in entry:
                 exit()
            elif "help" in entry:
                 print(" cwd : correct working directory\n exit : quit the terminal\n help  : for help\n ld : list all the files and directories\n cd : Change Directory\n Run : Start any file with url\n INFO : for author info\n rkmdir : Remove any folder\n Speak : To speak text from computer\n mkdir : To create a directory \n mkf : To createe a file \n rmf : To remove any file \n time : To show correct date and time\n Open : To open any website\n Wikipedia : To search on wikipedia\n Rename : To rename any file\n get-playlist : To download full playlist from youtube\n get-video : To download youtube video\n cmd : To open command prompt\n")
            elif "ld" in entry:
              print(os.listdir())
            elif "time" in entry:
              print(time.ctime())
            elif "cd" in entry:
              b = input('\t $ ---> ')
              os.chdir(b)
            elif "run" in entry:
             c = input("\t $ ---> ")
             os.startfile(c)
            elif "info" in entry:
              print("Mr.Hacker :- \n\tIt is a terminal like hacking tool with linux and windows commands.")
            elif "rkmdir" in entry:
             d = input('\t $ ---> ')
             print("Type Y for Yes and N for No.")
             p = input()
             if 'y' in p:
               shutil.rmtree(d)
               print("Folder successfullh deleted.")
             else:
               print('Deleting Cenceled.')
            elif "speak" in entry:
             s = input("\t $ ---> ")
             speak(s)
            elif "mkdir" in entry:
             m = input("\t $ ---> ")
             os.mkdir(m)
             print("Folder successfullh created.")
            elif "mkf" in entry:
               mf = input("\t $ ---> ")
               with open(mf,'a') as f:
                 f.write()
                 print("File successfullh created.")
            elif "rmf" in entry:
               rr = input("\t $ ---> ")
               print("Type Y for Yes and N for No.")
               p = input()
               if 'y' in p:
                    os.remove(rr)
                    print("File successfullh deleted.")
               else:
                   print('Deleting Cenceled.')
            elif "open" in entry:
                url = input('\t $ ---> ')
                webbrowser.open(url)
            elif "wikipedia" in entry:
                  quary = input('\t $ ---> ')
                  print("Searching Wikipedia....")
                  quary = quary.replace("wikipedia","")
                  results = wikipedia.summary(quary)
                  print("According to wikipedia...")
                  print(results)
            elif 'rename'in entry:
                old = input("\t $ ---> ")
                new = input("\t $ ---> ")
                os.rename(old,new)
                print("File successfullh renamed.")
            elif 'get-playlist' in entry:
                 py = Playlist(input("\t $ ---> "))
                 print(f"Downloading : {py.title} ")
                 for video in py.videos:
                   video.streams.first().download()
                   print('Downloading Completed')
            elif "get-video" in entry:
               link = input('\t $ ---> ')
               YouTube_1 = YouTube(link)
               videos = YouTube_1.streams.all()
               vid =list(enumerate(videos))
               for i in vid:
                   print(i)
               print()
               strm = int(input("\t $ ---> "))
               videos[strm].download()
               print("Video Sucessfully Downloaded")
            elif "cp" in entry:
               op = input("\t $ ---> ")
               np = input("\t $ ---> ")
               if e in op :
                 e.replace(e,"")
                 with open("pass.txt","w") as f:
                    f.write(np)
                    print('Password Successfully Changed')
                    speak('Password Successfully Changed')
               else:
                  speak("Please Enter the Old Password.")
                  print("Please Enter the Old Password.")
            elif 'system' in entry:
               print(subprocess.call('systeminfo'))
            elif "cmd" in entry:
                 os.startfile("C:\\Users\\win 10\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt")
            elif "play music" in entry:
                 os.startfile("D:\\Coding\\python projects\\jarvis\\hello.xspf")
            else:
              print(f"'{entry}' is not a internal and external command.")
          except Exception as e:
             pass
   elif "" in a:
      speak('please enter username or password')       
      print('Please Enter The Password')       
   else:
      speak('wrong password, please enter the correct password')
      print('Wrong Password, Please Enter The Correct Password')
