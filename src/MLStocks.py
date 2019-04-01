import numpy as np
from sklearn import svm

from alpha_vantage.techindicators import TechIndicators
import pandas as pd

df = pd.read_csv("C:/Users/ryohe/PycharmProjects/StacksOnStacks/stockSymbols.csv")
symbolList = list(df["Symbols"])
df = pd.read_csv("NKE.csv")
labels_df = df["label"]
features_df = df.drop("label", axis=1)
labels = labels_df.values.tolist()
features = features_df.values.tolist()

clf = svm.SVC(gamma='scale')
clf.fit(features, labels)
for symbol in symbolList:
    whatever = None
    while whatever is None:
        try:
            ti = TechIndicators(key='KU7YQYX4LFOFNQTU', output_format='pandas')
            rsi, metadata = ti.get_rsi(symbol=symbol, interval='weekly', time_period='4', series_type='open')
            adx, metadata = ti.get_adx(symbol=symbol, interval='weekly', time_period='4')
            cci, metadata = ti.get_cci(symbol=symbol, interval='weekly', time_period='4')
            mfi, metadata = ti.get_mfi(symbol=symbol, interval='weekly', time_period='4')
            roc, metadata = ti.get_roc(symbol=symbol, interval='weekly', time_period='4')

            whatever = 1
        except KeyError:
            pass
    data = [float(rsi.iloc[rsi.shape[0] - 1]), float(adx.iloc[adx.shape[0] - 1]), float(cci.iloc[cci.shape[0] - 1]),
        float(mfi.iloc[mfi.shape[0] - 1]), float(roc.iloc[roc.shape[0] - 1])]

    print(symbol)
    print(clf.predict(np.array(data).reshape(1, -1)))
