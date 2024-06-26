from time import strftime
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():   
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello Sir.I am K Junior. Please tell me how may I help you")       

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
        print("Say that again please...")  
        return "None"
    return query 

if __name__ == "__main__":
   wishMe()
while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")


        elif ('open google') in query:
            webbrowser.open("google.com")


        elif 'open maharana' in query:
            speak("opening maharana pratap ERP website")
            webbrowser.open("https://erp.mpgi.net/")   



        elif 'play music' in query:
            speak("playing music,sir")
            music_dir = 'C:\\Users\\Admin\\Music\\Playlists'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        

        elif 'the time' in query:
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {strtime}")
        
        elif 'hello' in query:
            speak(" hello ,sir ")
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'good morning' in query:
            speak("good morning , sir")

        elif 'good night' in query:
            speak("good night , sir")
        
        elif 'bye'in query:
            speak("bye ,sir")