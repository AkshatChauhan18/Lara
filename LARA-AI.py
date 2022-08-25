import calendar
import datetime
import os
import os.path
import pickle
import smtplib
import sys
import time
import webbrowser
from tkinter.filedialog import *
import _thread
import matplotlib
import matplotlib.pyplot as plt
import psutil
import pyautogui
import PyPDF2
import pyttsx3
import speech_recognition as sr

def initial():
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    Months=['january',
            'february',
            'march',
            'april',
            'may',
            'june',
            'july',
            'august',
            'september',
            'october',
            'november',
            'december']
    n=10
    master = "Mr.Akshat"
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 170)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 1)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Calibrating Microphone")
        r.adjust_for_ambient_noise(source,5)


    def snack():
        love = str(datetime.datetime.now().time())
        if love >= "17:30" and love < "19" \
                                      ":30" :
            print("Time to eat snacks  " + master)
            speak("time to eat snacks " + master)
    def dinner():
        love = str(datetime.datetime.now().time())
        if love >="20:30" and love <"21:30" :
            print("Time to eat dinner " + master)
            speak("time to eat dinner " +master)
    def lunch():
        love = str(datetime.datetime.now().time())
        if love>="14:30" and love <"15:30":
            print("It's time eat lunch " +master)
            speak("it's time to eat lunch " +master)
    def breakfast():
        love = str(datetime.datetime.now().time())
        if love >="8:30" and love<"10:30":
            print("It's time for breakfast" +master)
            speak("it's time for breakfast" +master)




    def lara():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = r.listen(source)
        try:
            print("Recognizing...")
            ai = r.recognize_google(audio, language='en-in')
            print(f"You said: {ai}\n")
        except Exception as e:

            ai = lara()
        return ai



    # speech function will pronounce the string which is passed to it
    def send_email(to ,content):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('bhuwneshchauhan18@gmail.com','NIGHTBEGINStoSHINE11')
        server.sendmail('bhuwneshchauhan18@gmail.com',to,content)
    def timey():
        hour = datetime.datetime.now().strftime("%H:%M:%S")
        print("Now the time is time is", hour)
        engine.say("Now the time is " + hour)
        engine.runAndWait()


    def date():
        hour = str(datetime.datetime.now().date())
        print("Today's date is", hour)
        engine.say("today's date is " + hour)
        engine.runAndWait()


    def speak(text):
        engine.say(text)
        engine.runAndWait()


    # this function will wish as per current time
    def wishme():
        love = datetime.datetime.now().hour
        if love >= 0 and love < 12:
            print("Good Morning " + master)
            engine.say("Good morning " + master)
            engine.runAndWait()

        elif love >= 12 and love < 16:
            print("Good Afternoon " + master)
            engine.say("Good Afternoon " + master)
            engine.runAndWait()
        else:
            print("Good Evening " + master)
            engine.say("Good Evening " + master)
            engine.runAndWait()
        speak("how may i help you sir ?")


    # this function will take command from microphone
    def take_command():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"You said :{query}\n")
        except Exception as e:
            print(master + " Please say that again:")
            speak(master + "please say that again")
            query=take_command()
        return query







    # main program starts here




    # logic for executing tasks ass per the ques
    def main():
        query = take_command()





        if "system"in query:
            c=psutil.sensors_battery()[0]
            y=(psutil.swap_memory().total/(1024**3))
            w=(psutil.swap_memory().used/(1024**3))
            z=psutil.cpu_freq()[0]/1000
            print("Your battery is " , c,"%")
            speak(f"Your battery is {c}  %" )
            print(f"Your  total swap memory is{y} GB")
            speak(f"Your total swap memory is {y} GB")
            print(f"Your  used swap memory is{w} GB")
            speak(f"Your  used swap memory is{w} GB")
            print("Your  current CPU frequency is" ,z," GHz" )
            speak(f"Your  current CPU frequency is {z} giga hertz")
            speak("sir your CPU percentage is")
            fig =plt.figure()
            ax = fig.add_subplot(111)


            plt.title("CPU PERCENT")
            plt.ylabel("Percentage")
            plt.grid("gray")
            fig.show()
            i = 0
            x,y=[],[]

            while True:
                x.append(i)
                y.append(psutil.cpu_percent())

                ax.plot(x,y, color='g')


                fig.canvas.draw()
                ax.set_xlim(left=max(0,i-30),right=i+30)

                time.sleep(0.1)
                i +=1

                if i>=200 :
                    matplotlib.pyplot.close()
                    break

        elif 'search' in query.lower():
            speak('what do you want to search')
            yo = take_command()
            speak('okay,right here in your screen ')
            dr = webdriver.Chrome()
            dr.get('https://google.com')
            time.sleep(5)
            search = dr.find_element_by_xpath( '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
            search.send_keys(yo)
            pyautogui.hotkey('enter')
           

        elif 'book' in query.lower():
            speak('sir please select the book')
            book = askopenfilename()
            pdf = PyPDF2.PdfFileReader(book)
            pages = pdf.numPages

            engine = pyttsx3.init('sapi5')
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            rate = engine.getProperty('rate')
            engine.setProperty('rate', 170)
            volume = engine.getProperty('volume')
            engine.setProperty('volume', 1)
            speak('i am going to read it for you sir')
            for num in range(0, pages):
                page= pdf.getPage(num)
                text = page.extractText()
                engine.say(text)
                engine.runAndWait()



        elif 'keylogger' in query.lower():
            os.startfile('key_logger_simple.pyw')


        elif "shutdown" in  query.lower():

            os.system("shutdown/s")

        elif 'window' in query.lower():
            print("What should i type")
            speak("what should i type ")

            po=take_command()

            time.sleep(2)
            pyautogui.hotkey('win')
            time.sleep(2)
            pyautogui.typewrite(f"{po}\n",0.5)
        elif 'weather' in query.lower():
            speak("you want weather of which place")
            po=take_command()
            url=f'http://api.openweathermap.org/data/2.5/weather?q={po}&appid=62696a1acfdf054e5a742fa769548ca9&units=metric'
            res=requests.get(url)
            data=res.json()
            temp=data["main"]["temp"]
            wind=data["wind"]["speed"]
            humid=data["main"]["humidity"]
            clouds=data["clouds"]["all"]
            print(temp)
            speak(f"temprature is {temp} degree celsius")
            print(wind)
            speak(f"wind spead is {wind}")
            print(humid)
            speak(f"humidity is {humid} %")
            print(clouds)
            speak(f"clouds are {clouds}%")

        elif 'wikipedia' in query.lower():
            print("Searching wikipedia")
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
        elif 'com' in query.lower():
            print("Opening site")
            speak('opening site it might take some time')
            query = query.replace("open", "")
            url=query
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"))
            webbrowser.get('chrome').open(url=query)
        elif 'time' in query.lower():
            timey()

        elif 'date' in query.lower():
            date()

        elif 'type' in query.lower():
            speak("what should i type ")
            r=take_command()
            pyautogui.typewrite(f"{r}")
        elif 'delete' in query.lower():
            speak("ok")
            pyautogui.hotkey('delete')

        elif 'next' in query.lower():
            pyautogui.hotkey('optionright')
        elif 'previous' in query.lower():
            pyautogui.hotkey('optionleft')

        elif "stop"in query.lower():
            speak("Bye sir have a good day")
            sys.exit()


        elif "screenshot" in query.lower():
            pyautogui.hotkey('win','prtscr')

        elif "relax"  in query.lower():
            speak("I know you like music , so opening spotyfai")
            pyautogui.hotkey('win')
            time.sleep(2)
            pyautogui.typewrite("Spotify\n",0.5)
            time.sleep(10)
            pyautogui.hotkey('playpause')
        elif"pause" in query.lower() or "play" in query.lower():
            pyautogui.hotkey('playpause')
        elif "calendar" in query.lower():
            speak("sir you want calendar of which month")
            print("")

            po=take_command().lower()
            if po.lower() in Months:
                speak("here is your calendar")
                y=Months.index(po)
                p=int(time.strftime('%Y'))
                o=calendar.month(p,y+1)
                print(o)


        elif "month" in  query.lower():
            speak("ok sir")
            a=int(time.strftime('%Y'))
            b=int(time.strftime('%m'))
            r=calendar.month(a,b)
            time.sleep(1)
            speak("here is your calendar")
            print(r)
        elif "year"in query .lower():
            a=int(time.strftime('%Y'))
            r=calendar.calendar(a)
            print(r)

        elif 'email'  in query.lower():
            speak("to whom sir")
            lo=take_command().lower()
            if "myself" in lo.lower():
                try:
                    print("What should i say")
                    speak("what should i say")
                    content=take_command()
                    to="bhuwneshchauhan18@gmail.com"
                    send_email(to,content)
                    speak("Email has beeen sent successfully ")
                except Exception as e:
                    speak("sir some error occurred")
                    print(e)
                    time.sleep(1) 
                    speak(f"sir it is saying {e}")
        elif "plans" in query.lower():
            calender(n,service)

    def mainstart():
        ro = lara()
        if "lara"in ro.lower():
            speak("Yes sir")
            main()

        elif "thank you" in ro.lower():
            speak("Most welcome sir scince i am your personal assistant")
        elif "i have eaten" in ro.lower():
            speak("ok!i was just reminding you ")

        elif "beautiful" in ro.lower() or "intelligent"in ro.lower():
            speak("I know sir that i am intelligent")
        elif 'delete' in ro.lower():
            pyautogui.hotkey('delete')

        elif 'next' in ro.lower():
            pyautogui.hotkey('optionright')
        elif 'previous' in ro.lower():
            pyautogui.hotkey('optionleft')
        elif 'hate' in ro.lower():
            speak("sorry sir i would try to improve")


    # If modifying these scopes, delete the file token.pickle.



    def authenticate():

        creds = None

        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)

            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        return service

    def calender(n,service):
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        print(f"Getting the upcoming {n} events")
        speak(f"Getting the upcoming {n} events")
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                            maxResults=n, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            speak('No upcoming events found')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])


    service=authenticate()

    wishme()
    snack ()
    lunch()
    dinner()
    breakfast()
    while True:
        mainstart()
def lartk():
    try:
        root.mainloop()
    except:
        pass

_thread.start_new_thread(lartk,())
initial()




