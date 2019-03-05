from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import pandas as pd

symbols = ['NKE', 'AAPL', 'NFLX', 'MSFT', ]

new_df = pd.DataFrame(columns=symbols)
for stock in symbols:
    ts = TimeSeries(key='KU7YQYX4LFOFNQTU', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=stock, interval='1min', outputsize='full')
    new_df[stock] = data['4. close']

print(new_df)


