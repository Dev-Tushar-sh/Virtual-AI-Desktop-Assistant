import pyttsx3
import datetime
import speech_recognition as sr
from speech_recognition import *
import wikipedia
import webbrowser
import os
import pywhatkit
import pyautogui
#import pyaudio 

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


# Face Recognition

def attandance():
    import face_recognition  
    import cv2     
    import numpy as np
    import csv
    from datetime import datetime

    video_capture = cv2.VideoCapture(0) 

    jobs_image = face_recognition.load_image_file("photos/jobs.jpg")
    jobs_encoding = face_recognition.face_encodings(jobs_image)[0]
    
    ratan_tata_image = face_recognition.load_image_file("photos/tata.jpg")
    ratan_tata_encoding = face_recognition.face_encodings(ratan_tata_image)[0]
    
    Tushar_image = face_recognition.load_image_file("photos/Tushar_Sharma.jpg")
    Tushar_encoding = face_recognition.face_encodings(Tushar_image)[0]
    
    tesla_image = face_recognition.load_image_file("photos/tesla.jpg")
    tesla_encoding = face_recognition.face_encodings(tesla_image)[0]

    rdj_image = face_recognition.load_image_file("photos/rdj.jpg")
    rdj_encoding = face_recognition.face_encodings(rdj_image)[0]
 
    known_face_encoding = [
    jobs_encoding,
    ratan_tata_encoding,
    Tushar_encoding,
    tesla_encoding,
    rdj_encoding
    ]
    
    known_faces_names = [
    "Steve jobs",
    "Ratan tata",
    "Tushar Sharma",
    "Elon musk",
    "RDJ"
    ]
    
    students = known_faces_names.copy()
    
    face_locations = []   
    face_encodings = []    
    face_names = [] 
    s=True


    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")


    f = open(current_date+'.csv','w+',newline = '')
    lnwriter = csv.writer(f)
    
    while True:
        _,frame = video_capture.read()
        small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
        # rgb_small_frame = small_frame[:,:,::-1]
        rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])
        if s:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
                name=""
                face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
                best_match_index = np.argmin(face_distance)
                if matches[best_match_index]:
                    name = known_faces_names[best_match_index]
    
                face_names.append(name)
                if name in known_faces_names:
                    if name in students:
                        students.remove(name)
                        print(students)
                        current_time = now.strftime("%H-%M-%S")
                        lnwriter.writerow([name,current_time])
        cv2.imshow("Attendence system",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    video_capture.release()
    cv2.destroyAllWindows()
    f.close() 



def wishme():
    hour = int(datetime.datetime.now().hour)
    if(hour >= 0 and hour <12):
        speak("Good Morning sir")
    elif(hour >=12 and hour<18):
        speak("Good Afternoon sir")
    else:
        speak("Good evening sir")
    speak("I am JARVIS and i am your personal assistant how may i help you")

#it take the audio and convert that in a string and return none if problem occur
    #it takes microphone input from the user and return string output
     #recognizer class used to recognize the audio  #use for source the microphone
     

def sendEmail(to,content):
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('kakashi.the.copy.ninja01@gmail.com','nqcbncoqerinqvit')
    server.sendmail('nohacking2222@gmail.com',to,content)
    server.close()

def ai(prompt):
    import openai
    import random
    from config import apikey

    openai.api_key = apikey
    
    text = f"Ai response for the prompt:{prompt} \n*******************************\n\n\n\n"

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": prompt
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
    
    # print(response["choices"][0]["message"]["content"])
    
    text += response["choices"][0]["message"]["content"]

    if not os.path.exists("Openai_files"):
        os.mkdir("Openai_files")

    with open(f"Openai_files/prompt- {random.randint(100,5000)}.txt","w") as f:
        f.write(text)



if __name__== "__main__":
    wishme()
    while True:  
        query=""
        # while True:
        #     query=takecommand().lower()
        #     if 'ok jarvis' in query:
        #         break
        speak("yes sir")
        query = takecommand().lower()
        #logic to exicuting task based commands

        if 'who is' in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia ")
            print(result)
            speak(result)

        elif 'ok jarvis' in query:
            speak("yes sir")
            ser = takecommand()
            result = wikipedia.summary(ser,sentences = 2)
            print(result)
            speak(result)
            break

        elif 'using intelligence' in query:
            prompt = query.split("intelligence")[1]
            ai(prompt)


        elif 'qr' in query:
                from pip import main
                import pyqrcode
                from pyqrcode import QRCode
                speak("yes sir")
                s=takecommand()
                no=pyqrcode.create(s)
                no.svg("qr.svg",scale = 8)
                webbrowser.open("file:///D:/My%20Programes/Project/qr.svg")
                break

        elif 'face recognition' in query:
            print("opening ")
            speak("Opening")
            attandance()
            break

        elif 'email to tony' in query:
            try:
                speak("what should i say?")
                content = takecommand()
                to = "nohacking2222@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry sir i am not able to send this email")
                break
            
        elif 'open youtube' in query:
            speak("Opening Youtube and what do you want to play ")
            command = takecommand()
            pywhatkit.playonyt(command)
            break

        elif 'search on google' in query:
            speak("what should I search ?")
            qry = takecommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=2)
            speak(results)


        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open("google.com")
            break

        # elif 'search' in query:
        #     speak("what do you want to search sir")
        #     ser=takecommand()
        #     try:
        #         print("Searching")
        #         pywhatkit.search(ser)
        #     except Exception as e:
        #         speak("some error occured please check your internet connection")
        #     break


        elif 'play song' in query:
            music_dir='D:\\My Programes\\Project\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            break
        
        elif 'the time' in query:
            strtemp = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strtemp}")
            break

        elif 'open vs code' in query:
            speak("opening our IDE sir")
            path = "C:\\Users\\tusha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
            break


        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")

        elif 'close youtube' in query:
            os.system("taskkill /f /im msedge.exe")


        elif 'close google' in query:
            os.system("taskkill /f /im msedge.exe")

#system related

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "lock the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        
        elif "take screenshot" in query:
            speak('tell me a name for the file')
            name = takecommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("screenshot saved")

        elif "open notepad" in query:
            npath = "C:\WINDOWS\system32\\notepad.exe"
            os.startfile(npath)

        elif 'type' in query: #10
            speak("what do you want to type sir ")
            # query = query.replace("type", "")
            typee = takecommand()
            pyautogui.write(f"{typee}")

        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")

        elif "volume up" in query:
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")

        elif "volume down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "mute" in query:
            pyautogui.press("volumemute")

        elif "refresh" in query:
            pyautogui.moveTo(1551,551, 2)
            pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
            pyautogui.moveTo(1620,667, 1)
            pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')

        elif "scroll down" in query:
            pyautogui.scroll(1000)
            
        elif "drag visual studio to the right" in query:
            pyautogui.moveTo(46, 31, 2)
            pyautogui.dragRel(1857, 31, 2)



#chrome automation

        elif 'open chrome' in query:
            os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')
        elif 'maximize this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('x')
        elif 'google search' in query:
            query = query.replace("google search", "")
            pyautogui.hotkey('alt', 'd')
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')

        elif 'youtube search' in query:
            query = query.replace("youtube search", "")
            pyautogui.hotkey('alt', 'd')
            time.sleep(1)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')
        elif 'open new window' in query:
            pyautogui.hotkey('ctrl', 'n')
        elif 'open incognito window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'n')
        elif 'minimise this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('n')
        elif 'open history' in query:
            pyautogui.hotkey('ctrl', 'h')
        elif 'open downloads' in query:
            pyautogui.hotkey('ctrl', 'j')
        elif 'previous tab' in query:
            pyautogui.hotkey('ctrl', 'shift', 'tab')
        elif 'next tab' in query:
            pyautogui.hotkey('ctrl', 'tab')
        elif 'closed tab' in query:
            pyautogui.hotkey('ctrl', 'w')
        elif 'close window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'w')
        elif 'clear browsing history' in query:
            pyautogui.hotkey('ctrl', 'shift', 'delete')
        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")

        elif 'goodbye' in query: 
            speak("goodbye sir. I am going to sleep")
            break