# The system should have 'pyaudio' and 'setuptools' pre-installed for the functioning. 
#................... Yashika Negi ;)....................
# Importing modules
import webbrowser
import datetime
import pyttsx3
import speech_recognition as sr
import os 
import random
import sys

# Text to speech convertor
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

# Function speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function greetMe
def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("HEY! Good Morning!")

    elif hour >= 12 and hour<18:
        speak("HEY!Good Afternoon")
    
    elif hour >= 18  and hour<21:
        speak("HEY! Good Evening!")

    else:
        speak("HEY! Greetings!")
    
    speak("I am cookie. How may I help you?")

#Function takeCommand
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Working...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        print("Kindly repeat...")
        return "None"
    return query

# the main() function
if __name__ == "__main__":
    greetMe()
    while True:
        query = takeCommand().lower()

        if 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open github' in query:
            webbrowser.open("https://github.com/yashika-ishi")
        
        elif 'open twitter' in query:
            webbrowser.open("twitter.com")
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H: %M: %S")
            speak(f"The time is {strTime}")

        # Put double '\\' here in the location of the directory path
        elif 'play music' in query:
            music = "C:\\Users\\YASHIKA NEGI\\Documents\\Yashika\\VS code\\vs code python\\OIBSIP-Python\\Voice_Assisstant\\kpop"
            songs = os.listdir(music)
            rd = random.choice(songs)
            os.startfile(os.path.join(music, songs[0]))

        # Exit the terminal
        elif 'exit' in query:
            speak("Okay. Cookie is shutting down now. ADIOS!")
            sys.exit()


        
        