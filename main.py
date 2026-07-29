import speech_recognition as sr
import webbrowser
import re
import musicLibrary
import requests
from groq import Groq
from dotenv import load_dotenv
import os
import tempfile
from gtts import gTTS
import pygame

# Load environment variables from .env file
load_dotenv()

newsapi = os.environ.get("NEWSAPI_KEY")

# Initialize pygame mixer once for audio playback
pygame.mixer.init()

def speak(text):
    if not text:
        return
    try:
        tts = gTTS(text=text, lang='en', slow=False)  # slow=True for a slower, clearer pace
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            temp_path = fp.name
        tts.save(temp_path)

        pygame.mixer.music.load(temp_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()
        os.remove(temp_path)
    except Exception as e:
        print(f"Speech error: {e}")

def clean_for_speech(text):
    # strip markdown symbols the model might still add, so TTS doesn't read them aloud
    text = re.sub(r'[*_#`]', '', text)
    return text.strip()

def aiProcess(command):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a virtual voice assistant named Lyra, similar to Alexa or Google Assistant. "
                    "Always respond in English only, regardless of what language the user's command is in. "
                    "Always reply in plain conversational text with no markdown, no bullet points, no asterisks. "
                    "Keep every response to 4-5 short lines maximum, since it will be spoken aloud. "
                    "Be direct and concise, and get straight to the answer."
                )
            },
            {"role": "user", "content": command}
        ],
        max_tokens=150,
        temperature=0.7,
    )
    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("http://linkedin.com")
    elif "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("http://instagram.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for article in articles:
                speak(article['title'])
    else:
        # not a recognized command -> let the AI handle it
        response = aiProcess(c)
        speak(clean_for_speech(response))

if __name__ == "__main__":
    speak("Initializing Lyra...")
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Calibrating for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=1)

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=4)
            except sr.WaitTimeoutError:
                print("No speech detected, listening again...")
                continue

        print("Recognizing...")
        try:
            word = r.recognize_google(audio, language="en-US")
            print("Heard:", word)
            if word.lower() == "lyra":
                speak("Yaa")
                with sr.Microphone() as source:
                    print("Lyra Active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio, language="en-US")
                    processCommand(command)
        except sr.UnknownValueError:
            print("Could not understand, try again...")
        except sr.RequestError as e:
            print(f"Could not request results from Google; {e}")