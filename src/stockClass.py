from alpha_vantage.techindicators import TechIndicators
import smtplib
class indicateStock:
    def __init__(self, symbol, increasing):
        self.symbol = symbol
        self.increasing = increasing
    def getEMA12(self):
        whatever = None
        while whatever is None:
            try:
                ti = TechIndicators(key='KU7YQYX4LFOFNQTU', output_format='pandas')
                data, metadata = ti.get_ema(symbol=self.symbol, interval='1min', time_period='12', series_type='close')
                whatever = data
                return float(data.iloc[data.shape[0] - 1])
            except KeyError:
                pass
    def getEMA26(self):
        whatever = None
        while whatever is None:
            try:
                ti = TechIndicators(key='KU7YQYX4LFOFNQTU', output_format='pandas')
                data, metadata = ti.get_ema(symbol=self.symbol, interval='1min', time_period='26', series_type='close')
                whatever = data
                return float(data.iloc[data.shape[0] - 1])
            except KeyError:
                pass
    def compareEMA50and200(self):
        ema12 = self.getEMA12()
        ema26 = self.getEMA26()
        print self.symbol
        print ema26
        print ema12
        if ema26 > ema12:
            self.increasing = True
            print self.increasing
        if ema26 < ema12:
            self.increasing = False
            print self.increasing
        if self.increasing == True:
            s = smtplib.SMTP("smtp.gmail.com", 587)
            s.starttls()
            s.ehlo
            s.login("pranavryoheistocksonstocks@gmail.com", "rnamiki2pvraman2")
            s.sendmail("pranavryoheistocksonstocks@gmail.com", "pranavryoheistocksonstocks@gmail.com", "Buy the stock " + self.symbol)
            s.quit()
        if ema12 == ema26:
            if self.increasing == True:
                s = smtplib.SMTP("smtp.gmail.com", 587)
                s.starttls()
                s.ehlo
                s.login("pranavryoheistocksonstocks@gmail.com", "rnamiki2pvraman2")
                s.sendmail("pranavryoheistocksonstocks@gmail.com", "pranavryoheistocksonstocks@gmail.com","Buy the stock " + self.symbol)
                s.quit()
            else:
                s = smtplib.SMTP("smtp.gmail.com", 587)
                s.starttls()
                s.ehlo
                s.login("pranavryoheistocksonstocks@gmail.com", "rnamiki2pvraman2")
                s.sendmail("pranavryoheistocksonstocks@gmail.com", "pranavryoheistocksonstocks@gmail.com","Sell the stock" + self.symbol)
                s.quit()

# Sets up the stocks. Basically we could place all the stocks from robin hood in this array
allsymbols = ['NKE', 'AAPL', 'NFLX', 'MSFT', 'TRXC', 'SNAP', 'ACB']
stockObject = []
stock = 0
# Cycles thru and makes a Stock object of each symbol
for x in range(len(allsymbols)):
    stockObject.append(indicateStock(allsymbols[x], False))
# Infinite loop of comparisons
i = 0
while i is 0:
    for x in range(len(stockObject)):
        stockObject[x].compareEMA50and200()