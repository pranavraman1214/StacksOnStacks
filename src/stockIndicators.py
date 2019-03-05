from alpha_vantage.techindicators import TechIndicators
import smtplib

def getEMA50(symb):
    whatever = None
    while whatever is None:
        try:
            ti = TechIndicators(key='KU7YQYX4LFOFNQTU', output_format='pandas')
            data, metadata = ti.get_ema(symbol=symb, interval='1min', time_period='50', series_type='close')
            whatever = data
            return float(data.iloc[data.shape[0] - 1])
        except KeyError:
            pass

def getEMA200(symb):
    whatever = None
    while whatever is None:
        try:
            ti = TechIndicators(key='KU7YQYX4LFOFNQTU', output_format='pandas')
            data, metadata = ti.get_ema(symbol=symb, interval='1min', time_period='200', series_type='close')
            whatever = data
            return float(data.iloc[data.shape[0] - 1])
        except KeyError:
            pass

def compareEMA50and200():
    increasing = False
    ema50 = getEMA50('NKE')
    ema200 = getEMA200('NKE')
    print ema200
    print ema50
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

i = 0
while i is 0:
    compareEMA50and200()











