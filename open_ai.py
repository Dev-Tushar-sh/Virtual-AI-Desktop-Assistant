
import pyttsx3

import datetime
import speech_recognition as sr
from speech_recognition import *
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()  
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)   #listen function have problem with environment noise so we have to supress it
        print("Listening.......")
        r.pause_threshold = 1  #agar hum 1 sec pause lele bote time tho ye phrase consider na kare  
        #r.energy_threshold = 200
        audio = r.listen(source)  
        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language='en-in')
            # i=0
            # if 'ok jarvis' in query:
            #     i=1
            #     print(f"user said :{query}\n")
            # if i==1:
            print(f"user said :{query}\n")
        except Exception as e:
        # print(e)
            print("say that again please....")
            return "None"
    return query


if __name__=='__main__':
    speak("hi")
    query = takecommand()
    if 'who are' in query:
        speak("I am jarvis and i am the one who knocks")

    
