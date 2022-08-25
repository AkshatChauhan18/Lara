import calendar
import datetime
from tkinter import *
from colorama import Fore

def month_calendar():

    date = datetime.date.today()
    root = Tk()
    root.config(background = "white")
    root.title("CALENDAR")
    cal_content = calendar.month(int(date.year),int(date.month),5,2)
    cal = Label(root, text = cal_content, font = "Consolas 10 bold")
    cal.pack(anchor='e')
    root.mainloop()

  

def year_calendar(date:int):
    try:
        root = Tk()
        root.title("Calendar")
        myCal = str(calendar.calendar(date))
        cal_year = Label(root, text=myCal, font="Consolas 10 bold")
        cal_year.pack()
        root.mainloop()
    except Exception as e:
        print(Fore.LIGHTRED_EX + e)


