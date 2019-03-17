from alpha_vantage.techindicators import TechIndicators
import smtplib
import pandas as pd

df = pd.read_csv("C:/Users/ryohe/PycharmProjects/StacksOnStacks/stockSymbols.csv")
symbolList = list(df["Symbols"])
print(symbolList)

def getEMA50(symb):
    whatever = None
    while whatever is None:
        try:
            ti = TechIndicators(key='KU7YQYX4LFOFNQTU', output_format='pandas')
            data, metadata = ti.get_ema(symbol=symb, interval='1min', time_period='50', series_type='close')
            whatever = data
            return data
        except KeyError:
            pass

def getEMA200(symb):
    whatever = None
    while whatever is None:
        try:
            ti = TechIndicators(key='KU7YQYX4LFOFNQTU', output_format='pandas')
            data, metadata = ti.get_ema(symbol=symb, interval='1min', time_period='200', series_type='close')
            whatever = data
            return data
        except KeyError:
            pass

def compareEMA50and200():
    increasing = False
    ema50 = getEMA50('NKE')
    ema200 = getEMA200('NKE')
    print(ema200)
    print(ema50)
    if ema200 > ema50:
        increasing = True
    if ema50 < ema200:
        increaing = False
    if ema200 == ema50:
        if increasing == True:
            s = smtplib.SMTP("smtp.gmail.com", 587)
            s.starttls()
            s.ehlo
            s.login("pranavryoheistocksonstocks@gmail.com", "rnamiki2pvraman2")
            s.sendmail("pranavryoheistocksonstocks@gmail.com", "pvraman2@illinois.edu", "Buy the stock")
            s.quit()
        else:
            s = smtplib.SMTP("smtp.gmail.com", 587)
            s.starttls()
            s.ehlo
            s.login("pranavryoheistocksonstocks@gmail.com", "rnamiki2pvraman2")
            s.sendmail("pranavryoheistocksonstocks@gmail.com", "pvraman2@illinois.edu", "Sell the stock")
            s.quit()


print(getEMA50("SNAP"))
print(getEMA200("SNAP"))
print(getEMA50("SNAP") - getEMA200("SNAP"))


