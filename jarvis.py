import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import random
import smtplib
import wikipedia
import pywhatkit
import psutil
import requests

# ----------------- TEXT TO SPEECH -----------------
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ----------------- TAKE VOICE INPUT -----------------
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("You said:", query)
        return query.lower()
    except:
        speak("Sorry, I didn't catch that")
        return "none"

# ----------------- GREETING -----------------
def wish_me():
    hour = int(datetime.datetime.now().hour)

    if hour < 12:
        speak("Good morning user")
    elif hour < 18:
        speak("Good afternoon user")
    else:
        speak("Good evening user")

    speak("I am Jarvis. How can I help you?")

# ----------------- BASIC FUNCTIONS -----------------

def tell_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("Current time is " + time)

def tell_date():
    date = datetime.datetime.now().strftime("%d %B %Y")
    speak("Today's date is " + date)

def open_youtube():
    webbrowser.open("https://youtube.com")

def open_google():
    webbrowser.open("https://google.com")

def play_song(song):
    speak("Playing " + song)
    pywhatkit.playonyt(song)

def wikipedia_search(topic):
    result = wikipedia.summary(topic, sentences=2)
    speak(result)

def tell_joke():
    jokes = [
        "Why did the computer go to doctor? Because it had a virus.",
        "Why don’t programmers like nature? Too many bugs.",
        "Why did the student break up with calculator? It could not function well."
    ]
    speak(random.choice(jokes))

def system_info():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    speak(f"CPU usage is {cpu} percent and RAM usage is {ram} percent")

def send_email(to, subject, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("your_email@gmail.com", "your_password")

        email = f"Subject: {subject}\n\n{message}"
        server.sendmail("your_email@gmail.com", to, email)
        server.quit()

        speak("Email sent successfully")
    except:
        speak("Unable to send email")

# ----------------- MAIN FUNCTION -----------------
def main():
    wish_me()

    while True:
        query = take_command()

        if 'time' in query:
            tell_time()

        elif 'date' in query:
            tell_date()

        elif 'youtube' in query:
            open_youtube()

        elif 'google' in query:
            open_google()

        elif 'play' in query:
            speak("Which song?")
            song = take_command()
            play_song(song)

        elif 'wikipedia' in query:
            speak("What should I search?")
            topic = take_command()
            wikipedia_search(topic)

        elif 'joke' in query:
            tell_joke()

        elif 'system' in query:
            system_info()

        elif 'email' in query:
            speak("To whom?")
            to = take_command()
            speak("Subject?")
            subject = take_command()
            speak("Message?")
            message = take_command()
            send_email(to, subject, message)

        elif 'exit' in query:
            speak("Goodbye Raahul")
            break

# ----------------- RUN PROGRAM -----------------
main()