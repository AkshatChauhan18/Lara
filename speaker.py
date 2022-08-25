import pyttsx3 as tts
voice = tts.init('sapi5')
voices = voice.getProperty('voices')
voice.setProperty('voice', voices[1].id)
rate =  voice.getProperty('rate')
voice.setProperty('rate', 170)
volume = voice.getProperty('volume')
voice.setProperty('volume', 1)


def speak(sentence:str):
    voice.say(sentence)
    voice.runAndWait()