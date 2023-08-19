import pyttsx3 # Importing pyttsx3 module.

engine = pyttsx3.init('sapi5') # Creating engine named variable and use pyttsx3 module function and use sapi5.
voices = engine.getProperty("voices") # Creating voices named variable and use pyttsx3 module function .getproperty and recive voices.

engine.setProperty("voices",voices[0].id) # Using engine.setPropery method to set the voice and voice id.

# Createing speak function for speak the audio.

def speak(audio):
    engine.say(audio) # Using engine.say computer spead the audio that is text.
    engine.runAndWait() # This function is use to wait the next command.

