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
    def setOtherVariables(self, bought, stockprice, stockcount):
        self.buy_bool = bought
        self.stock_price = stockprice
        self.stock_count = stockcount

    def sell(self):
        time.sleep(2)
        webbrowser.open("https://google.com", new=1)
        time.sleep(1.5)
        pyautogui.click(1032, 180, duration=0)
        pyautogui.hotkey('ctrl', 'command', 'f')
        time.sleep(1.5)
        pyautogui.moveTo(885, 0)
        pyautogui.moveTo(885, 20)
        pyautogui.click(885, 35, duration=0)
        time.sleep(1)
        pyautogui.typewrite("Robinhood")
        pyautogui.typewrite(["enter"])
        time.sleep(1)
        pyautogui.moveTo(300, 500)
        time.sleep(5)
        pyautogui.click(428, 34, duration=0)
        pyautogui.typewrite(self.symbol)
        time.sleep(2)
        pyautogui.typewrite(["enter"])
        time.sleep(2.5)
        pyautogui.click(1194, 125, duration=0)
        pyautogui.click(1290, 181, duration=0)
        pyautogui.typewrite(str(self.stock_count))
        time.sleep(1)
        pyautogui.click(1267, 341, duration=0)
        time.sleep(1)
        pyautogui.click(1252, 451, duration=0)
        time.sleep(1)
        pyautogui.hotkey('command', 'w')

    def buy(self, buy_count):
        time.sleep(2)
        webbrowser.open("https://google.com", new=1)
        time.sleep(1.5)
        pyautogui.click(1032, 180, duration=0)
        pyautogui.hotkey('ctrl', 'command', 'f')
        time.sleep(1.5)
        pyautogui.moveTo(885, 0)
        pyautogui.moveTo(885, 20)
        pyautogui.click(885, 35, duration=0)
        time.sleep(1)
        pyautogui.typewrite("Robinhood")
        pyautogui.typewrite(["enter"])
        time.sleep(1)
        pyautogui.moveTo(300, 500)
        time.sleep(5)
        pyautogui.click(428, 34, duration=0)
        pyautogui.typewrite(self.symbol)
        time.sleep(2)
        pyautogui.typewrite(["enter"])
        time.sleep(2.5)
        pyautogui.click(1306, 185, duration=0)
        pyautogui.typewrite(str(buy_count))
        pyautogui.click(1196, 351, duration=0)
        time.sleep(1)
        pyautogui.click(1262, 451, duration=0)
        time.sleep(1)
        pyautogui.hotkey('command', 'w')

    def getEMA12(self):
        whatever = None
        while whatever is None:
            try:
                ti = TechIndicators(key='JMCHDT9XJ90DOIQL', output_format='pandas')
                data, metadata = ti.get_ema(symbol=self.symbol, interval='1min', time_period='12', series_type='close')
                whatever = data
                return [float(data.iloc[data.shape[0] - 2]), float(data.iloc[data.shape[0] - 1])]
            except KeyError:
                pass

    def getEMA26(self):
        whatever = None
        while whatever is None:
            try:
                ti = TechIndicators(key='JMCHDT9XJ90DOIQL', output_format='pandas')
                data, metadata = ti.get_ema(symbol=self.symbol, interval='1min', time_period='26', series_type='close')
                whatever = data
                return [float(data.iloc[data.shape[0] - 2]), float(data.iloc[data.shape[0] - 1])]
            except KeyError:
                pass

    def getPrice(self):
        whatever = None
        while whatever is None:
            try:
                ts = TimeSeries(key='JMCHDT9XJ90DOIQL', output_format="pandas")
                data, metadata = ts.get_intraday(symbol=self.symbol, interval='1min', outputsize='compact')
                whatever = data
                data = data["4. close"]
                return float(data.iloc[data.shape[0] - 1])
            except KeyError:
                pass

    def compareEMA50and200(self):
        ema12 = self.getEMA12()
        ema26 = self.getEMA26()
        self.stock_price = self.getPrice()
        print(self.symbol)
        emaDiffBefore = ema12[0] - ema26[0]
        emaDiffAfter = ema12[1] - ema26[1]
        print(emaDiffBefore)
        print(emaDiffAfter)

        if emaDiffBefore < 0 and emaDiffAfter > 0 and self.buy_bool:
            buy_count = math.floor(self.buy_power / self.stock_price)
            self.buy(buy_count)
            self.stock_count = buy_count
            self.buy_power = self.buy_power - buy_count*self.stock_price
            #Additional Lines
            writeToFile(self.symbol, buy_count,self.stock_price,self.buy_power )
            s = smtplib.SMTP("smtp.gmail.com", 587)
            s.starttls()
            s.ehlo
            s.login("pranavryoheistocksonstocks@gmail.com", "rnamiki2pvraman2")
            s.sendmail("pranavryoheistocksonstocks@gmail.com", "pranavryoheistocksonstocks@gmail.com", "Buy the stock " + self.symbol)
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
            #Resets the file
            resetFile()
            s.quit()
            self.buy_bool = True


# Seperated our main function into two seperate functions.
def nostockinfile():
    df = pd.read_csv("../stockSymbols.csv")
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











