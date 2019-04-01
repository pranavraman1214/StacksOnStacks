from alpha_vantage.techindicators import TechIndicators
import pandas as pd

df = pd.read_csv("C:/Users/ryohe/PycharmProjects/StacksOnStacks/stockSymbols.csv")
symbolList = list(df["Symbols"])
symbol = 'CRCM'
whatever = None
while whatever is None:
        try:
            ti = TechIndicators(key='KU7YQYX4LFOFNQTU', output_format='pandas')
            rsi, metadata = ti.get_rsi(symbol=symbol, interval='weekly', time_period='4', series_type='open')
            adx, metadata = ti.get_adx(symbol=symbol, interval='weekly', time_period='4')
            cci, metadata = ti.get_cci(symbol=symbol, interval='weekly', time_period='4')
            mfi, metadata = ti.get_mfi(symbol=symbol, interval='weekly', time_period='4')
            roc, metadata = ti.get_roc(symbol=symbol, interval='weekly', time_period='4')

            #ts = TimeSeries(key='KU7YQYX4LFOFNQTU', output_format="pandas")
            #data, metadata = ts.get_weekly(symbol=symbol)
            #open_price = data["1. open"]
            #close_price = data["4. close"]
            whatever = 1
        except KeyError:
            pass
#df_joined = pd.concat([rsi, adx, cci, mfi, roc, open_price, close_price], axis=1)

#header = ['RSI','ADX','CCI','MFI','ROC','1. open','4. close']
#df_joined.to_csv('haha.csv', columns=header)
print([float(rsi.iloc[rsi.shape[0] - 1]),float(adx.iloc[adx.shape[0] - 1]),float(cci.iloc[cci.shape[0] - 1]),float(mfi.iloc[mfi.shape[0] - 1]),float(roc.iloc[roc.shape[0] - 1])])

