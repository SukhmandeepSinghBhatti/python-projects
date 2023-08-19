import os
import MusicPlayer


while(True):
 a = input(("Enter the command:  "))
 if "ld" in a:
    print(os.listdir())
 elif "pm" in a:
    print(MusicPlayer())