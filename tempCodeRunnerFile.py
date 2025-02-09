import speech_recognition as sr
import webbrowser
import pyttsx3
import pocketsphinx
import musiclibrary
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
ttsx = pyttsx3.init()


def speak_old(text):
    ttsx.say(text)
    ttsx.runAndWait()


def speak(text):
    filename = "audio.mp3"
    tts = gTTS(text=text, lang="en")
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.stop()
    pygame.mixer.quit()

    try:
        os.remove(filename)  # Safe deletion
    except PermissionError:
        print("Warning: Could not delete the file. It may still be in use.")


def aiprocess(command):
    client = OpenAI(api_key="your-openai-api-key")  # Fix typo: `api_key` instead of `pi_key`

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": command},
        ],
    )

    return completion.choices[0].message["content"]


def processCommand(c):
    c = c.lower()

    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open instagram" in c:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "open whatsapp" in c:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")

    elif "open amazon" in c:
        speak("Opening Amazon")
        webbrowser.open("https://www.amazon.com")

    elif c.startswith("play"):
        song = c.split("play")[1].strip()
        if song in musiclibrary.play:
            link = musiclibrary.play[song]
            webbrowser.open(link)
        else:
            speak("Song not found in music library.")

    elif c.startswith("news"):  # Fix the syntax issue
        speak("Getting news")
        webbrowser.open("https://news.google.com")

    elif c.startswith("weather"):
        speak("Getting weather")
        webbrowser.open("https://www.weather.com")

    elif c.startswith("time"):
        speak("Getting time")
        webbrowser.open("https://www.time.com")

    elif c.startswith("date"):
        speak("Getting date")
        webbrowser.open("https://www.date.com")

    else:
        output = aiprocess(c)
        speak(output)


if __name__ == "__main__":
    speak("Initializing Reane")

while True:
    recognizer = sr.Recognizer()
    print("Recognizing...")

    try:
        with sr.Microphone() as source:
            print("Say something")
            audio = recognizer.listen(source, timeout=2, phrase_time_limit=4)

        command = recognizer.recognize_google(audio)

        if command.lower() == "reane":
            speak("Yes sir")

        with sr.Microphone() as source:
            print("Reane Active......")
            audio = recognizer.listen(source, timeout=2, phrase_time_limit=4)
            command = recognizer.recognize_google(audio)
            processCommand(command)

    except sr.UnknownValueError:
        print("Google could not understand audio")

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service: {e}")
