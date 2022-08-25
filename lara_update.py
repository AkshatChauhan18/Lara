'''TODO:
play song
show system info
greet according to time
tell time
todo list
planner
send email
check email
tell date
weather
wikipedia
relax command
pause and play
face recognition
code Red
code yellow 
face rec
TODO:
'''
import os
from colorama import Fore
import json
import random
import sys
import pyautogui
import home_automation
import _thread
from recognize_speech import*
from speaker import *
from webwork import *
from desktop_automation import *
from calendar_functions import *
data = json.load(open("intents.json"))


def main():
    print()
    print(Fore.GREEN+'Please say command')
    print(Fore.WHITE)
    query = take_comand()
    print(f'You said {query}')
    print()

    if query in data['intents'][1]['patterns']:
        speak(random.choice(data['intents'][1]["responses"]))
        sys.exit()

    if query in data['intents'][2]['patterns']:
        speak(random.choice(data['intents'][2]['responses']))
        _thread.start_new_thread(home_automation.automate,(1,))

    if query in data['intents'][3]['patterns']:
        speak(random.choice(data['intents'][3]['responses']))
        _thread.start_new_thread(home_automation.automate,(0,))

    if query in data['intents'][4]['patterns']:
        speak(random.choice(data['intents'][4]['responses']))
        os.system("shutdown/p")

    if query in data['intents'][5]['patterns']:
        speak(random.choice(data['intents'][5]['responses']))
        os.system("shutdown/l")

    if query in data['intents'][6]['patterns']:
        speak(random.choice(data['intents'][6]['responses']))
        os.system("Rundll32.exe user32.dll,LockWorkStation")

    if query in data['intents'][7]['patterns']:
        speak(random.choice(data['intents'][7]['responses']))
        os.system("shutdown/r")

    if query.startswith('open'):
        speak(random.choice(data['intents'][8]['responses']))
        open_website(query.replace("open", ""))

    if query.startswith('search'):
        speak(random.choice(data['intents'][9]['responses']))
        search_query(query.replace('search', ""))

    if query.startswith('start'):
        speak(random.choice(data['intents'][10]
              ['responses'])+" "+query.replace('start', ""))
        open_app(query.replace('start', ""))

    if 'screenshot' in query:
        speak(random.choice(data['intents'][11]['responses']))
        pyautogui.hotkey('win', 'prtsc')

    if 'calendar' in query and 'this month' in query:
        speak(random.choice(data['intents'][12]['responses']))
        _thread.start_new_thread(month_calendar,())

    if 'calendar of year' in query:
        speak(random.choice(data['intents'][12]['responses']))
        _thread.start_new_thread(year_calendar,(int(query.split()[-1]),))

    print()


while True:
    message = wake_lara()
    if 'lara' in message:
        print('you said lara')
        response_list = data['intents'][0]["responses"]
        response = random.choice(response_list)
        speak(response)
        main()