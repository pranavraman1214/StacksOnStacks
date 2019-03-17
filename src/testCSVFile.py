from alpha_vantage.timeseries import TimeSeries
import csv
allsymbols = []
for d in csv.DictReader(open('../allNASDAQ'), delimiter='|'):
    allsymbols.append(str(d['Symbol']))
print allsymbols


def printLinesToCSV(name, myFile,x):
    try:
        print (name)
        ts = TimeSeries(key='JMCHDT9XJ90DOIQL', output_format="pandas")
        data, metadata = ts.get_intraday(symbol=name, interval='1min', outputsize='compact')
        whatever = data
        data = data["4. close"]
        price = float(data.iloc[data.shape[0] - 1])
        if (price < 30):
            stocksUnder20.append(name)
            myFile.write(name + '\n')
            print (name)
        return
    except KeyError as e:
        print ("Recurse")
        printLinesToCSV(name, myFile,x)
    except ValueError as v:
        return


stocksUnder20 = []
i = 0
currentStock = 574

with open("../stocksUnder20", 'a') as myFile:
    for i in range(420):
        printLinesToCSV(allsymbols[currentStock + i],myFile,0)

