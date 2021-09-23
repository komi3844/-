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

talk("Скажи мне что нибудь")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        zadanie = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + zadanie)
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        zadanie = command()

    return zadanie

def makeSomething(zadanie):
    if 'открыть сайт'.lower() in zadanie:
        talk("Уже открываю говносайт")
        url = 'https://zakupki.gov.ru/epz/main/public/home.html'
        webbrowser.open(url)
    elif 'стоп' in zadanie:
        talk("да, конечно, нет проблем")
        sys.exit()
    elif 'имя' in zadanie:
        talk("меня не зовут")
    elif 'поздравление' in zadanie:
        talk("Привет данилка у тебя сегодня днюшка Поздравляю")


while True:
    makeSomething(command())