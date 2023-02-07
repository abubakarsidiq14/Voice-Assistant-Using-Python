from fileinput import filename
from time import strftime
from tkinter import EXCEPTION
from urllib.parse import quote_from_bytes
from click import command
from grpc import server
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import webbrowser
import os
import wikipedia as wp
import smtplib
import pywhatkit as pwk

engine = pyttsx3.init('sapi5',100)
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)



hour = int(datetime.datetime.now().hour)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<=18:
        speak("Good Evening")
    else:
        speak("Good Afternoon") 

def Command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print("User said : ",query)

    except Exception as e:
        print(e)
        print("Sorry I can`t Recognize it")      
        return 'None'

    return query    

def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com',467)
    server.ehlo()
    server.starttls()
    server.login('abubakarsidiq0123@gmail.com','fdvqwhzldjicgvup')
    server.sendmail('abubakarsidiq0123@gmail.com',to ,content)
    print("Mail sent")
    server.close() 

if __name__=="__main__":
    wish()
    speak("Hello I am ARIES How can I Help you ")
    
    while True:
        query = Command().lower()
        if 'open youtube' in query:
            url = 'https://www.youtube.com/'
            chorme_path = r"C:\\Program Files (x86)\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register("chrome",None,webbrowser.BackgroundBrowser(chorme_path))
            webbrowser.get("chrome").open_new_tab(url)

        elif 'open google' in query:
            url = "https://www.google.co.in/"
            chorme_path = r"C:\\Program Files (x86)\Google\\Chrome\\Application\\chrome.exe"
            webbrowser.register("chrome",None,webbrowser.BackgroundBrowser(chorme_path))
            webbrowser.get("chrome").open_new_tab(url)

        elif 'file is present' in query:
            speak("Which file you want to open ")
            filename = Command()
            #filename = input()
            a = os.path.isfile(filename)
            if(a is True):
                print("File is present.")
                fp = open(filename,"r+")
                speak(fp.read())
                fp.close()
            else:
                print("File is not present.")
                speak("File is not present.")

        elif 'your name' in query:
            print("ARIES")
            speak("My name is ARIES.")
            

        elif 'who are you' in query:
            speak("My name is ARIES")   
            speak("Your personal assistant")
            
             
        elif 'wikipedia' in query:
            speak("Searching From Wikipedia")
            result=wp.summary(str(query), sentences = 2)
            print(result)
            speak(result)      

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'time ' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'code' in query:
            vspath="C:\\Users\\pc\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(vspath)    

        elif 'email' in query: 
            try:
                speak("To Who You want to send email")
                name = input()
                to = (f"{name}@gmail.com")
                speak("What to send")
                content = input()
                sendEmail(to , content)
                speak("Email send successully")
        
            except Exception as e:
                print(e)
                speak("Sorry,I can`t send mail")

        elif (hour>=19 and hour<=21):
                speak("This is coding time sir")
                speak("Can I open hacker rank")
                query1=Command().lower
                if 'open ' in query1:
                    webbrowser.open("hackerrank.com")

        elif 'from youtube' in query:
            play = query.replace('play','')
            speak("Playing...")
            pwk.playonyt(play)

        elif 'stop' in query:
            break                

        else:
            speak("Sorry I don`t get it Please tell again ")   


