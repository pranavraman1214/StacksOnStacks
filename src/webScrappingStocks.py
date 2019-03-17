from bs4 import BeautifulSoup
import requests
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
import smtplib
import pandas as pd
import pyautogui
import webbrowser
import time
import math

money = 28


class IndicateStock:
    def __init__(self, symbol, buy_power):
        self.symbol = symbol
        self.buy_power = buy_power
        self.buy_bool = True
        self.stock_price = 0
        self.stock_count = 0
        self.ema50 = None
        self.ema200 = None
    def setOtherVariables(self, bought, stockprice, stockcount):
        self.buy_bool = bought
        self.stock_price = stockprice
        self.stock_count = stockcount

    def sell(self):
        time.sleep(2)
        webbrowser.open('http://google.com', new=1)
        time.sleep(2.5)
        pyautogui.click(519, 62, duration=0)
        pyautogui.typewrite("Robinhood")
        pyautogui.typewrite(["enter"])
        time.sleep(4)
        pyautogui.click(403, 133, duration=0)
        pyautogui.typewrite(self.symbol)
        time.sleep(2)
        pyautogui.typewrite(["enter"])
        time.sleep(2.5)
        pyautogui.click(1402, 246, duration=0)
        pyautogui.click(1539, 317, duration=0)
        pyautogui.typewrite(str(self.stock_count))
        pyautogui.click(1422, 533, duration=0)
        time.sleep(1)
        pyautogui.click(1409, 650, duration=0)
        time.sleep(5)
        pyautogui.click(1891, 17, duration=0)

    def buy(self, buy_count):
        time.sleep(2)
        webbrowser.open('http://google.com', new=1)
        time.sleep(2.5)
        pyautogui.click(519, 62, duration=0)
        pyautogui.typewrite("Robinhood")
        pyautogui.typewrite(["enter"])
        time.sleep(4)
        pyautogui.click(403, 133, duration=0)
        pyautogui.typewrite(self.symbol)
        time.sleep(2)
        pyautogui.typewrite(["enter"])
        time.sleep(2.5)
        pyautogui.click(1539, 317, duration=0)
        pyautogui.typewrite(str(buy_count))
        pyautogui.click(1422, 533, duration=0)
        time.sleep(1)
        pyautogui.click(1409, 650, duration=0)
        time.sleep(5)
        pyautogui.click(1891, 17, duration=0)

    def get_ema50_ema200(self):
        page_link = f"https://finance.yahoo.com/quote/{self.symbol}/key-statistics?p={self.symbol}"
        page_response = requests.get(page_link, timeout=5)
        page_content = BeautifulSoup(page_response.content, "html.parser")
        textContent = []
        data = []
        searchString = "td"
        for i in range(len(page_content.find_all(searchString))):
            paragraphs = page_content.find_all(searchString)[i].text
            textContent.append(paragraphs)

        for i in range(len(textContent)):
            if i % 2 != 0:
                data.append(textContent[i])

        return [data[36], data[37]]

    def get_price(self):
        page_link = f"https://www.nasdaq.com/symbol/{self.symbol}/real-time"
        page_response = requests.get(page_link, timeout=5)
        page_content = BeautifulSoup(page_response.content, "html.parser")
        textContent = []
        data = []
        searchString = "span"
        for i in range(len(page_content.find_all(searchString))):
            paragraphs = page_content.find_all(searchString)[i].text
            textContent.append(paragraphs)

        for i in range(len(textContent)):
            if i % 2 != 0:
                data.append(textContent[i])

        return data[25]

    def compareEMA50and200(self):
        current_emas = self.get_ema50_ema200()
        if self.ema50 and self.ema200:
            emaDiffBefore = self.ema50 - self.ema200
            self.ema50 = float(current_emas[0])
            self.ema200 = float(current_emas[1])
            emaDiffAfter = self.ema50 - self.ema200
            self.stock_price = self.get_price()
            print(self.symbol)
            print(emaDiffBefore)
            print(emaDiffAfter)

            if emaDiffBefore < 0 and emaDiffAfter > 0 and self.buy_bool:
                buy_count = math.floor(self.buy_power / self.stock_price)
                self.buy(buy_count)
                self.stock_count = buy_count
                self.buy_power = self.buy_power - buy_count * self.stock_price
                # Additional Lines
                writeToFile(self.symbol, buy_count, self.stock_price, self.buy_power)
                s = smtplib.SMTP("smtp.gmail.com", 587)
                s.starttls()
                s.ehlo
                s.login("pranavryoheistocksonstocks@gmail.com", "rnamiki2pvraman2")
                s.sendmail("pranavryoheistocksonstocks@gmail.com", "pranavryoheistocksonstocks@gmail.com",
                           "Buy the stock " + self.symbol)
                s.quit()
                self.buy_bool = False
                while not self.buy_bool:
                    self.compareEMA50and200()

            if emaDiffBefore > 0 and emaDiffAfter < 0 and not self.buy_bool:
                self.sell()
                self.stock_count = 0
                self.buy_power = self.buy_power + self.stock_count * self.stock_price
                s = smtplib.SMTP("smtp.gmail.com", 587)
                s.starttls()
                s.ehlo
                s.login("pranavryoheistocksonstocks@gmail.com", "rnamiki2pvraman2")
                s.sendmail("pranavryoheistocksonstocks@gmail.com", "pranavryoheistocksonstocks@gmail.com",
                           "Sell the stock " + self.symbol)
                # Resets the file
                resetFile()
                s.quit()
                self.buy_bool = True
        else:
            print("hello")
            self.ema50 = float(current_emas[0])
            self.ema200 = float(current_emas[1])
            return



# Seperated our main function into two seperate functions.
def nostockinfile():
    df = pd.read_csv("../stockSymbols2.csv")
    allsymbols = list(df["Symbols"])
    stockObject = []
    # Cycles thru and makes a Stock object of each symbol
    for x in range(len(allsymbols)):
        stockObject.append(IndicateStock(allsymbols[x], money))
    # Infinite loop of comparisons
    i = 0
    while i is 0:
        for x in range(len(stockObject)):
            stockObject[x].compareEMA50and200()
    return


def stockInFile():
    currentStock = IndicateStock(data, buypower)
    currentStock.setOtherVariables(False, stockPrice, stocksBought)
    while (currentStock.buy_bool == False):
        currentStock.compareEMA50and200()
    nostockinfile()
    return


# Helper methods to reset the file after we have sold a stock
def resetFile():
    out = open('../BoughtStocks', 'w')
    out.write("Empty")
    out.write("\n")
    out.write("0")
    out.write("\n")
    out.write("0")
    out.write("\n")
    out.write("0")
    out.write("\n")
    return


# Helper method to write the Bought Stocks file when we have bought a stock
def writeToFile(symbol,stocksBought,pricePaid, buyPower):
    out = open('../BoughtStocks', 'w')
    out.write(str(symbol))
    out.write("\n")
    out.write(str(stocksBought))
    out.write("\n")
    out.write(str(pricePaid))
    out.write("\n")
    out.write(str(buyPower))
    out.write("\n")
    return


#Main I guess
data = ""
stocksBought = ""
stockPrice = ""
buypower = ""
with open('../BoughtStocks', 'r') as myfile:
    data = myfile.readline().strip()
    stocksBought = int(myfile.readline())
    stockPrice = float(myfile.readline())
    buypower = float(myfile.readline())

if stocksBought is 0:
    nostockinfile()
else:
    stockInFile()

