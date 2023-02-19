import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Aniket!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Aniket!")

    else:
        speak("Good Evening Aniket!")

    speak(" Jarvis at Your Service. how may i help you sir ")

def wishme1():
    hour1 = int(datetime.datetime.now().hour)
    if hour1>=0 and hour1<12:
        speak("Good Morning sir")

    elif hour1>=12 and hour1<18:
         speak("Good Afternoon sir")

    else:
        speak("Good Evening sir")



def takeCommand():
    #it takes microphone inputs from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listenning........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        

        print("Say That Again Please")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        #Logic For Executing Tasks Based On query
        if 'wikipedia' in query:
            speak("Searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening YouTube")
            webbrowser.open("https://www.youtube.com")
            

        elif 'open google' in query:
            speak("opening Google")
            webbrowser.open("https://www.google.com")
            
        
        elif 'open gmail' in query:
            speak("opening Gmail")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            

        elif "what time is it" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Time is {strTime}")
            speak(f"The Time is {strTime}")

        elif "open chrome" in query:
            speak("opening Chrome")
            ppath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(ppath)

        elif "open whatsapp" in query:
            speak("opening whatsapp")
            webbrowser.open("https://web.whatsapp.com/")

        elif "exit" in query:
            speak("Thank You Sir For Your Time. Ask me anything you want !")
            exit()

        elif "talk to lisa" in query:
            engine.setProperty('voice',voices[1].id)
            wishme1()
            print("Lisa Here !")
            speak("My name is lisa. what can i assist you with ? ")

        elif "talk to jarvis" in query:
            engine.setProperty('voice',voices[0].id)
            speak("Jarvis here. How can i help you sir ?")

        elif "on youtube" in query:
            print("Searching on YouTube")
            speak("Searching on Youtube")
            
            driver = webdriver.Chrome()
            driver.get('https://www.youtube.com')
            query = query.replace("on youtube", "")
            searchbox = driver.find_element_by_xpath('//*[@id="search"]')
            searchbox.send_keys(query)
            searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
            speak("Here's what i found on youtube")
            searchButton.click()
            
        elif "search for" in query:
            print("Searching On Google")
            speak("Searching on Google")
            driver = webdriver.Chrome()
            driver.get('https://www.google.com')
            query = query.replace("search for", "")
            searchbox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            searchbox.send_keys(query)
            speak("Here's what i found on Google")
            searchbox.send_keys(Keys.ENTER)
            

        elif "play" in query:
            print("Playing on YouTube")
            speak("playing on Youtube")

            driver = webdriver.Chrome()

            driver.get('https://www.youtube.com')
            query = query.replace("play", "")

            searchbox = driver.find_element_by_xpath('//*[@id="search"]')
            searchbox.send_keys(query)

            searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
            searchButton.click()
            
            play = driver.find_element_by_xpath('//*[@id="dismissible"]')
            play.click()

        

