import openai
from config import api_key
import pyttsx3

openai.api_key = api_key

como = openai.Completion()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def reply(question):
    try:
     prompt   = f"Sukhmna{question}\n Jarvis:"
     response = como.create(prompt=prompt,engine="text-davinci-002",stop=      ['\Jarvis'],max_tokens=200)
     ans = response.choices[0].text.strip()
     return ans
    except Exception as e:
       speak(f'Sorry I dont about {question}')

