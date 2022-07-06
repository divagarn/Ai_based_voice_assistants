import email
import operator
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from http import server
import random
import sys
from urllib import request
import webbrowser
import PyPDF2
import instaloader
import requests
from requests import get
from matplotlib.pyplot import text
import pyjokes as pyjokes
import pywhatkit as kit
import pyttsx3
import speech_recognition as sr
import datetime
import os
import os.path
import cv2
import wikipedia
from requests import get
import smtplib
import pyautogui
from bs4 import BeautifulSoup

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', 'voices[len(voices) - 1].id')

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# to convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning.....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=8)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        speak("say that again please...")
        return "none"
    query= query.lower()
    return query


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    #print(tt)

    if hour >= 0 and hour <= 12:
        speak(f"good morning,it's {tt}")
    elif hour > 12 and hour < 18:
        speak(f"good afternoon,it's {tt}")
    else:
        speak(f"god evening,it's {tt}")
    speak("i am matlai sir. please tell me how can i help you")


# to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nscetece2018@gmail.com', 'welcomeece')
    server.sendmail('nscetece2018@gmail.com', to, content)
    server.close()


# for news updates
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=9e98dbf1c3d640b29e088d0d5456e628'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

def pdf_reader():
    book = open('py3.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book) #pip install PyPDF2
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages} ")
    speak("sir please enter the page number i have to read")
    pg = int(input("please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)
    #jarvis speaking seep shoud be controlle by user

def start():
    pyautogui.press('esc')

    wish()
    while True:
        # if 1:

        query = takecommand().lower()

        # logic building for task

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "path location"
            songs = os.listdir(music_dir)
            # rd=random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))



        # elif "ip address" in query:
        # ip=get('https://www.ipaddress.my/').text
        # speak(f"your IP is {ip}")
        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentence=2)
            speak("according to wikipedia")
            speak(results)
            # print(results)

        elif "open YouTube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("sir,what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+918220270549", "hey this is divagar", 2, 25)
            time.sleep(120)
            speak("message has been sent")

        elif "play songs on youtube" in query:
            kit.playonyt("see you again")

        elif "email to dude" in query:
            try:
                speak("what shound i send sir?")
                content = takecommand().lower()
                to = "masterpets@gmail.com"
                sendEmail(to, content)
                speak("Email has been sant to avi")

            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to start this mail to dude")
                # pip install secure-smtplib

        elif "no thanks" in query:
            speak("thank you sir, have a good day.")
            sys.exit()

        elif "sleep" in query or "sleep now" in query or "good bye" in query:
            speak("thank you sir, have a good day.")
            sys.exit()

        # to close any application
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")
        # to set an alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 22:
                music_dir = 'path of the music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
        # to find a joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 10")

        elif "restart the system" in query:
            os.system("shutdown /r /t 10")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "hello" in query or "hey" in query:
            speak("hello sir , may i help you")
        elif "how are you" in query:
            speak("I'm fine, what about you")
        elif "thank you " in query or "thanks" in query:
            speak("it's my pleasure")
            sys.exit()
            #break

        # speak("sir, do you have any other work")

        ######################################################################################################################################
        ######################################################################################################################################

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("please wait sir, fetching the latest news")
            news()

        elif "email to buddy" in query:

            speak("sir what should i say")
            query = takecommand().lower()
            if "send a file" in query:
                email = 'your@gmail.com'  # our own email
                password = 'mails password'
                send_to_email = 'receiver@gmail.com'  # the reciver email here
                speak("okay sir, what is the subject of the email")
                query = takecommand().lower()
                subject = query  # the subject of the email
                speak("and sir, what is the message of this email")
                query2 = takecommand().lower()
                message = query2  # the message in the email
                speak("sir please enter the correct path of the file into the above terminal")
                file_location = input("please enter the path here")  # used to attach th efile in this email

                speak("please wait, i am sending email now")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                # setup the attachment
                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s " % filename)

                # Attach the attachment to the mimemultipart object
                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("email has been sent to avinash")

            else:
                email = 'your@gmail.com'
                password = 'your_pass'
                send_to_email = 'person@gmail.com'
                message = query

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                server.sendmail(email, send_to_email, message)
                server.quit()
                speak("email has been sent to avinash")

        elif "do some calculation" in query or "can you calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("what you need to calculate")
                print("listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divided' : operator.__truediv__,
                    'Mod' : operator.mod,
                    'Mod' : operator.mod,
                    '^' :operator.xor,
                }[op]
            def eval_binary_expr(op1, oper, op2):
                op1,op2=int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            print(eval_binary_expr(*(my_string.split())))
    # takecommand()
        elif "temperature" in query:
            search = "temperature in theni"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

        #elif "activate the mod" in query:
            #from pywikihow import search_wikihow
            #speak("how to do mode is activated please tell me what you what to know")
            #how = takecommand()
            #max_results = 1
            #how_to= search_wikihow(how,max_results)
            #assert len(how_to) ==1
            #how_to[0].print()
            #speak(how_to[0].summary)
        elif "activate how to mod" in query:
            speak("how to do mod is activated")
            while True:
                speak("please tell me what you whant to know")
                how = takecommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("okay sir, how this is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) ==1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir , not able to find")

    # speak("hi dude this is divagar")

#to find my location using IP address:

        elif "where am i" in query or "where we are" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo'+ipAdd+'.json'
                geo_request = requests.get(url)
                geo_data = geo_request.json()
                #print(geo_data)
                city = geo_data['city']
                #state = geo_data['state']
                country = geo_data['country']
                speak(f"sir i am not suere, but i tink we are in {city} city of {country} country")
            except Exception as e:
                speak("sorry sir, Due to network issue i am not able to find where we are.")
                pass

#to check a instagram profile
        elif "instagram profile" in query or "profile on instagram" in query:
            speak("sir please enter the user name correctly.")
            name = input("Enter username here:")
            webbrowser.open(f"www.instagram.com/ {name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(5)
            speak("sir would you like to download profile picture of this account.")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader() #pip install instadownloader
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir, profile picture is saved in our main folder. now i am ready")
            else:
                pass

#to take screenshot

        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("please sir hold the screen for few second, i am taking sceenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder. now i am ready for next command")

#To read PDF file

        elif "read pdf" in query:
            pdf_reader()

        elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
            speak("sir please tell me you want to hide this folder")
            condition=takecommand().lower()
            if "hide" in condition:
                os.system("attrib +h /s /d")
                speak("sir, all the files in this folder are now hidden")
            elif "visible" in condition:
                os.system("attrib +h /s /d")
                speak("sir, all the files in this folder are now visible")
            elif "leave it" in condition or "leave now" in condition:
                speak("ok sir")
        elif "hello" in query or "hey" in query:
            speak("hello sir")
        elif "how are you" in query :
            speak("i am fine")
        elif "fine" in query:
            speak("thats great")
        elif "thank you" in query:
            speak("it's my pleassure")
        elif "you can sleep" in query or "sleep now" in query:
            speak("okay sir")
            break


#importing whole program face reco main here:

if __name__ == "__main__":
    #while True:
        #permission = takecommand()
        #if "wake up" in permission:
            #start()
        #elif "goodbye" in permission:
            #speak("thanks for using matlai, have a good day")
            #speak("thanks.")
            #sys.exit()
    start()

        #speak("sir, do you have any other work")