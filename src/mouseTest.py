import pyautogui
import webbrowser
import time


def sell(symbol):
    time.sleep(2)
    webbrowser.open('http://google.com', new=1)
    time.sleep(2.5)
    pyautogui.click(519, 62, duration=0)
    pyautogui.typewrite("Robinhood")
    pyautogui.typewrite(["enter"])
    time.sleep(4)
    pyautogui.click(403, 133, duration=0)
    pyautogui.typewrite(symbol)
    time.sleep(2)
    pyautogui.typewrite(["enter"])
    time.sleep(2.5)
    pyautogui.click(1402, 246, duration=0)
    pyautogui.click(1539, 317, duration=0)
    pyautogui.typewrite(str(3))
    pyautogui.click(1422, 533, duration=0)
    time.sleep(1)
    pyautogui.click(1409, 650, duration=0)
    time.sleep(5)
    pyautogui.click(1891, 17, duration=0)


def buy(symbol):
    time.sleep(2)
    webbrowser.open('http://google.com', new=1)
    time.sleep(2.5)
    pyautogui.click(519, 62, duration=0)
    pyautogui.typewrite("Robinhood")
    pyautogui.typewrite(["enter"])
    time.sleep(6)
    pyautogui.click(403, 133, duration=0)
    pyautogui.typewrite(symbol)
    time.sleep(2)
    pyautogui.typewrite(["enter"])
    time.sleep(2.5)
    pyautogui.click(1539, 317, duration=0)
    pyautogui.typewrite("1")
    pyautogui.click(1422, 533, duration=0)
    time.sleep(1)
    pyautogui.click(1409, 650, duration=0)
    time.sleep(5)
    pyautogui.click(1891, 17, duration=0)


sell("FSI")
