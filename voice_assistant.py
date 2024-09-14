import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import requests
import json
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import nltk

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

def get_weather(city):
    api_key = "Y2477ab37b8b601bb70cb8eb8d22e51af"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] != 200:
        speak("City not found.")
        return
    
    weather_description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    speak(f"The weather in {city} is currently {weather_description} with a temperature of {temperature} degrees Celsius.")

def send_email(to, subject, message):
   
    sender_email = "aliarshad1002@gmail.com"  
    sender_password = "12345678" 

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to, msg.as_string())
        speak("Email sent successfully.")

def respond(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}.")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}.")
    elif "weather" in command:
        city = command.split("in")[-1].strip()
        get_weather(city)
    elif "search" in command:
        query = command.replace("search", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Searching for {query} on Google.")
    elif "send email" in command:
        speak("Who do you want to send the email to?")
        recipient = listen()
        speak("What is the subject?")
        subject = listen()
        speak("What is the message?")
        message = listen()
        send_email(recipient, subject, message)
    elif "exit" in command:
        speak("Goodbye!")
        return True
    else:
        speak("I'm sorry, I can only respond to greetings, tell the time or date, provide weather updates, search the web, and send emails.")

def main():
    speak("Hello! I am your advanced voice assistant. How can I help you?")
    while True:
        command = listen()
        if command:
            if respond(command):
                break

if __name__ == "__main__":
    main()