import pyautogui


def sell(symbol):
    pyautogui.PAUSE = 3
    pyautogui.click(519, 62, duration=0)
    pyautogui.typewrite("Robinhood")
    pyautogui.typewrite(["enter"])
    pyautogui.click(403, 133, duration=0)
    pyautogui.typewrite(symbol)
    pyautogui.typewrite(["enter"])
    pyautogui.click(1402, 246, duration=0)
    pyautogui.click(1539, 317, duration=0)
    pyautogui.typewrite("500")
