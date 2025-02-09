import speech_recognition as sr
import webbrowser
import pyttsx3
from gtts import gTTS
import pygame
import os
import openai  # Use 'openai' here
from musiclibrary import play  # Import the play dictionary from musiclibrary

recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

# Function to speak text
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

    try:
        os.remove(filename)  # Safe deletion
    except PermissionError:
        print("Warning: Could not delete the file. It may still be in use.")
    finally:
        pygame.mixer.quit()  # Ensure pygame quits correctly

# AI process to generate a response
def aiprocess(command):
    openai.api_key = "your-openai-api-key"  # Replace with your OpenAI API key

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": command},
        ],
    )

    return completion.choices[0].message["content"]

# Process the command
def processCommand(command):
    command = command.lower()

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    elif "open whatsapp" in command:
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")

    elif "open amazon" in command:
        speak("Opening Amazon")
        webbrowser.open("https://www.amazon.com")
    elif"open gmail" in command:
        speak("Opening Gmail")
        webbrowser.open("https://www.gmail.com")
    elif"open twitter" in command:
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")
    elif"open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif"open netflix" in command:
        speak("Opening Netflix")
        webbrowser.open("https://www.netflix.com")
    elif"open spotify" in command:
        speak("Opening Spotify")
        webbrowser.open("https://www.spotify.com")
    elif"open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
    elif"open snapchat" in command:
        speak("Opening Snapchat")
        webbrowser.open("https://www.snapchat.com")
    elif"open google meet" in command:
        speak("Opening Google Meet")
        webbrowser.open("https://meet.google.com")
    elif"open zoom" in command:
        speak("Opening Zoom")
        webbrowser.open("https://zoom.us")
    elif"open googlemaps" in command:
        speak("Opening Google Maps")
        webbrowser.open("https://www.google.com/maps")
    elif"open google drive" in command:
        speak("Opening Google Drive")
        webbrowser.open("https://drive.google.com")
    elif"open google photos" in command:
        speak("Opening Google Photos")
        webbrowser.open("https://photos.google.com")
    elif"open google docs" in command:
        speak("Opening Google Docs")
        webbrowser.open("https://docs.google.com")
    elif"open radio" in command:
        speak("Opening Radio")
        webbrowser.open("https://www.radio.com")
    elif "open rapido" in command:
        speak("Opening Rapido")
        webbrowser.open("https://www.rapido.com")
    elif "open zomato" in command:
        speak("Opening Zomato")
        webbrowser.open("https://www.zomato.com")
    elif "open swiggy" in command:
        speak("Opening Swiggy")
        webbrowser.open("https://www.swiggy.com")
    elif"open uber" in command:
        speak("Opening Uber")
        webbrowser.open("https://www.uber.com")
    elif"open ola" in command:
        speak("Opening Ola")
        webbrowser.open("https://www.olacabs.com")
    elif"open where is my train" in command:
        speak("Opening Where is my train")
        webbrowser.open("https://www.whereismytrain.com")
    elif"open irctc" in command:
        speak("Opening IRCTC")
        webbrowser.open("https://www.irctc.co.in")
    elif"open paytm" in command:
        speak("Opening Paytm")  
        webbrowser.open("https://www.paytm.com")
    elif"open phonepe" in command:
        speak("Opening PhonePe")
        webbrowser.open("https://www.phonepe.com")
    elif"open amazon pay" in command:
        speak("Opening Amazon Pay")
        webbrowser.open("https://www.amazonpay.com")
    elif"open google pay" in command:
        speak("Opening Google Pay")
        webbrowser.open("https://pay.google.com")
        
    elif command.startswith("news"):
        speak("Getting news")
        webbrowser.open("https://news.google.com")
        

    elif command.startswith("weather"):
        speak("Getting weather")
        webbrowser.open("https://www.weather.com")

    elif command.startswith("time"):
        speak("Getting time")
        webbrowser.open("https://www.time.com")

    elif command.startswith("date"):
        speak("Getting date")
        webbrowser.open("https://www.date.com")
    
    
    if command.startswith("play"):
        speak("Play song")
        song = command.split("play")[1].strip()
        print(f"Song requested: {song}")  # Debug print

        if song in play:  # Check against the 'play' dictionary in musiclibrary
            link = play[song]  # Get the song URL from musiclibrary
            webbrowser.open(link)
        else:
            speak("Song not found in music library.")
    


    else:
        output = aiprocess(command)
        speak(output)

# Main loop to recognize speech and execute commands
if __name__ == "__main__":
    speak("Initializing Reane.....")

while True:
    recognizer = sr.Recognizer()
    print("Recognizing.....")

    try:
        with sr.Microphone() as source:
            print("Say something.....")
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=6)

        command = recognizer.recognize_google(audio)

        if command.lower() == "Reane":
            speak("Yes sir")

        with sr.Microphone() as source:
            print("Reane Active.....")
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=6)
            command = recognizer.recognize_google(audio)
        processCommand(command)

    except sr.UnknownValueError:
        print("Google could not understand audio")

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service: {e}")
