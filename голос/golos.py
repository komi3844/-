import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3
ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
engine = pyttsx3.init()
engine.setProperty('voice', ru_voice_id)
engine.runAndWait()

def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()
#    print(words)
#   os.system("say" + words)

talk("Привет данилка у тебя сегодня днюшка!!!")
