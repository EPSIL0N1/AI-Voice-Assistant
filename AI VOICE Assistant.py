import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
# import smtplib
import openai
from myopenaikey import my_key
from googlesearch import search as srch
import time
import sys




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id)

engine.setProperty('voice',voices[1].id)


def advance (query):
    openai.organization = "org-3rWXZNAyBTvMgAnVonej7Lw0"
    openai.api_key = my_key.a
    openai.Model.list()
    prompt = query

    response = openai.Completion.create(engine = "text-davinci-001", prompt=prompt, max_tokens = 500)

    res_1 = response["choices"]
    res_2 = res_1[0]
    res_2 = dict(res_2)
    # print(res_2["text"])
    # speak(res_2["text"])
    return res_2["text"]
    
def imagecreate(query):
    openai.organization = "org-3rWXZNAyBTvMgAnVonej7Lw0"
    openai.api_key = my_key.a
    openai.Model.list()
    response = openai.Image.create(
    prompt=query,
    n=1,
    size="1024x1024"
    )
    image_url = str(response['data'][0]['url'])
    speak("Opening Image...")
    webbrowser.open(image_url)
    

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning, Sir")
        speak("Good Morning, Sir")
    elif hour>=12 and hour<18:
        print("Good Afternoon, Sir")
        speak("Good Afternoon, Sir")
    else:
        print("Good Evening, Sir")
        speak("Good Evening, Sir")
    print("How can I help you?")
    speak("How can I help you?")

def pause():
    print("For how many seconds should I stop listening?")
    speak("For how many seconds should I stop listening?")
    seconds = takeCommand()
    p = 1
    while p==1:
        # if seconds == "None":
        #     print("Please say the time again")
        #     speak("Please say the time again")
        #     seconds = takeCommand()
        try:
            seconds = int(seconds)
            p = 0
        except Exception as e:
            print("Please say the time again")
            speak("Please say the time again")
            seconds = takeCommand()
    
    seconds_str = str(seconds)
    print("Pausing for " + seconds_str + "seconds")
    speak("Pausing for " + seconds_str + "seconds")
        
    time.sleep(seconds)

    print("Turning back on...")
    speak("Turning back on...")
    p = 0
            
        
    
# def sendemail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('naruto11110000@gmail.com','shrobona@1')
#     server.sendmail('naruto11110000@gmail.com', to, content)
#     server.close()
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
            
        print(f"User said: {query}\n")

    except Exception as e:
        print("Please say that again... ")
        speak("Please say that again... ")
        
        return "None"
    return query

# def adv_takeCommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
            
#         print(f"User said: {query}\n")

#     except Exception as e:
#         print("Say that again please... ")
#         return "Quote"
#     return query




if __name__ == "__main__":
    # speak("Good Morning Sir")
    wishme()
    while True:
        query = takeCommand().lower()
        
        
        #going advance
        
        if "advance" in query:
            a=1
            
            print("Initiating Advance mode...")
            speak("Initiating Advance mode...")
            
            engine.setProperty('voice',voices[0].id)
            print("Advance Mode Initiated.")
            speak("Advance Mode Initiated.")
                
            print("Please Tell Me What I can do for you")
            speak("Please Tell Me What I can do for you")
            
            while a==1:
                
                adv_query = takeCommand()
            
               
                if "image" in adv_query:
                    print("Creating requested image...please wait a moment")
                    speak("Creating requested image...please wait a moment")
                    adv_query = adv_query.replace("create image of","")
                    imagecreate(adv_query)
                    
                elif "file" in adv_query:
                    print("What should be the file name?")
                    speak("What should be the file name?")
                    
                    file_name = takeCommand()
                    
                    if file_name == "None":
                        print("Please Repeat the file name")
                        speak("Please Repeat the file name")
                        file_name = takeCommand()
                        
                    f = open(file_name + ".txt","w")
                    print("What should i write?")
                    speak("What should i write?")
                    file_content = takeCommand()
                    print("Processing your command...")
                    speak("Processing your command...")
                    
                    script = str(advance(file_content))
                    f.write(script)
                    
                    f.close()
                    
                    print("Opening requested file...")
                    speak("Opening requested file...")
                        
                    os.startfile(file_name + ".txt")
                    
                    print("Do you want to delete the file?")
                    speak("Do you want to delete the file?")
                    
                    answer = takeCommand()
                    if answer == "None":
                        print("Do you want to delete the file?")
                        speak("Do you want to delete the file?")
                        answer = takeCommand()
                        print("Deleting requested file...")
                        speak("Deleting requested file...")
                        
                        os.remove(file_name + ".txt")
                        
                        print("File Deleted")
                        speak("File Deleted")
                        
                    elif "yes" in answer:
                        print("Deleting requested file...")
                        speak("Deleting requested file...")
                        
                        os.remove(file_name + ".txt")
                        
                        print("File Deleted")
                        speak("File Deleted")
                        
                    else:
                        speak("Ok Sir")
                        print("Ok Sir")
                    
                elif "listening" in adv_query:
                    pause()
                elif "normal mode" in adv_query:
                    print("Advance mode turned off")
                    speak("Advance mode turned off")
                    a=0
                    engine.setProperty('voice',voices[1].id)
                    print("What can I do for you?")
                    speak("What can I do for you?")
                    
                else:
                    if adv_query == "None":
                        adv_query = takeCommand()
                        
                    else:
                        script = advance(adv_query)
                        print(script)
                        speak(script)


        elif 'wikipedia' in query:
            print("Searching Wikipedia...")
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif "search" in query:
            print("Searching in Google...")
            speak("Searching in Google...")
            query = query.replace("search","")
            for i in srch(query,tld="com",num=1,stop=2,pause=2):
                webbrowser.open(i)
        
        elif "listening" in query:
            pause()
            
        elif "open youtube" in query:
            print("Opening Youtube...")
            speak("Opening Youtube...")
            
            webbrowser.open("www.youtube.com")
            
        elif "open gmail" in query:
            
            print("Opening Gmail...")
            speak("Opening Gmail...")
            
            webbrowser.open("www.gmail.com")
            
        elif "play music" in query:
            music_dir = 'C:/Users/hp/Music/random Songs'
            songs = os.listdir(music_dir)
            number = random.randint(0,len(songs))
            print("Playing Music...")
            speak("Playing Music...")
            os.startfile(os.path.join(music_dir,songs[number]))
            
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif "open code" in query:
            codepath = "C:/Users/hp/AppData/Local/Programs/Microsoft VS Code/Code.exe"
            print("Opening Visual Code...")
            speak("Opening Visual Code...")
            # n = 0
            os.startfile(codepath)
            
            
        elif "who made you" in query:
            print("I was created by Mr.Sourik Poddar on 5th January 2023")
            speak("I was created by Mr.Sourik Poddar on 5th January 2023")
            
        # elif "write email" in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "sourikpoddar896@gmail.com"
        #         sendemail(to,content)
        #         speak("Email has been sent")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry Sir the Email was not sent")
                
        elif "stop" in query:
            speak("Thank You Sir, Have a good day")
            quit()
            # False
        
        
        
        
        
            
        
         
