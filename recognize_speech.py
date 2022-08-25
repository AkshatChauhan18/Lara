import speech_recognition as sr
from colorama import Fore
def take_comand():
    with sr.Microphone() as mic:
        recognizer = sr.Recognizer()
        recognizer.adjust_for_ambient_noise(mic,0.5)
        print('listening')
        audio = recognizer.listen(mic)
    try:
        print('recognizing')
        message = recognizer.recognize_google(audio,language='en-in')
        message = message.lower()
    except sr.UnknownValueError:

        print(Fore.LIGHTRED_EX+"Sory didn't got that")
        print(Fore.WHITE)
        message = take_comand()
    return message
def wake_lara():
    with sr.Microphone() as mic:
        recognizer = sr.Recognizer()
        recognizer.adjust_for_ambient_noise(mic,0.5)
        print('listening')
        audio = recognizer.listen(mic)
    try:
        print('recognizing')
        message = recognizer.recognize_google(audio,language='en-in')
        message = message.lower()
    except sr.UnknownValueError:
        message = wake_lara()
    return message
