from alpha_vantage.techindicators import TechIndicators
import smtplib
class indicateStock:
    def __init__(self, symbol):
        self.symbol = symbol

    def getEMA50(self):
        whatever = None
        while whatever is None:
            try:
                ti = TechIndicators(key='KU7YQYX4LFOFNQTU', output_format='pandas')
                data, metadata = ti.get_ema(symbol=self.symbol, interval='1min', time_period='50', series_type='close')
                whatever = data
                ema50 = float(data.iloc[data.shape[0] - 1])
                return float(data.iloc[data.shape[0] - 1])
            except KeyError:
                pass

    def getEMA200(self):
        whatever = None
        while whatever is None:
            try:
                ti = TechIndicators(key='KU7YQYX4LFOFNQTU', output_format='pandas')
                data, metadata = ti.get_ema(symbol=self.symbol, interval='1min', time_period='200', series_type='close')
                whatever = data
                return float(data.iloc[data.shape[0] - 1])
            except KeyError:
                pass

    def compareEMA50and200(self):
        increasing = False
        ema50 = self.getEMA50()
        ema200 = self.getEMA200()
        print self.symbol
        print ema200
        print ema50
        if ema200 > ema50:
            increasing = True
        if ema50 < ema200:
            increasing = False
        if ema200 == ema50:
            if increasing == True:
                s = smtplib.SMTP("smtp.gmail.com", 587)
                s.starttls()
                s.ehlo
                s.login("pranavryoheistocksonstocks@gmail.com", "rnamiki2pvraman2")
                s.sendmail("pranavryoheistocksonstocks@gmail.com", "pvraman2@illinois.edu", "Buy the stock" + self.symbol)
                s.quit()
            else:
                s = smtplib.SMTP("smtp.gmail.com", 587)
                s.starttls()
                s.ehlo
                s.login("pranavryoheistocksonstocks@gmail.com", "rnamiki2pvraman2")
                s.sendmail("pranavryoheistocksonstocks@gmail.com", "pvraman2@illinois.edu", "Sell the stock" + self.symbol)
                s.quit()








symbols = ['NKE', 'AAPL', 'NFLX', 'MSFT', ]
stockObject = []
stock = 0
for x in range(len(symbols)):
    stockObject.append(indicateStock(symbols[stock]))
    stock = stock + 1

print len(stockObject)
i = 0
while i is 0:
    for x in range(len(stockObject)):
        stockObject[x].compareEMA50and200()