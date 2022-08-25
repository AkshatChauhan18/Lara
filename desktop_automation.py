import pyautogui
import time


def open_app(app: str):
    pyautogui.hotkey('win', 's')
    time.sleep(2)
    pyautogui.typewrite(app)
    pyautogui.hotkey('enter')


def play_song():
    pyautogui.hotkey('win', 's')
    time.sleep(2)
    pyautogui.typewrite("spotify")
    pyautogui.hotkey("enter")
    time.sleep(10)
    pyautogui.hotkey("playpause")
    

if __name__=="__main__":
    play_song()    