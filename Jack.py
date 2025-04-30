import pyttsx3  
import datetime
import speech_recognition as sr  
import wikipedia

engine =  pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice' , voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour =  int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning")
    elif hour >= 12 and hour <18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")

    speak("hello I am Jack, how can i help You Abhishek")

def takecommand():
    """Takes voice input from the microphone and returns it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # This sets how long the pause is allowed
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
    WishMe()
    while True:
        query = takecommand().lower()
    #logic for executing task based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query= query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)




