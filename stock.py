from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from pprint import pprint

class Stock():

    def __init__(self, name, value, RSI, SMA):
        self.name = name
        self.value = value
        self.RSI = RSI
        self.SMA = SMA
    
   
    

    def getInfo(self):
        f = open("stockinfo.txt", "a")
        ts = TimeSeries(key='GZR6JEGOB3LF6RCB')
        tc = TechIndicators(key='GZR6JEGOB3LF6RCB',output_format='pandas')
        data, meta_data = ts.get_daily(self.name)
        data2, meta_data2 = tc.get_rsi(self.name)
        data3, meta_data3 = tc.get_sma(self.name)
        teststring = data['2018-10-12']
        print(teststring)
        self.value = float(teststring['4. close'])
        f.write("the stock chosen is: " + self.name + "\n")
        f.write("the most recent closing price is: " + str(self.value))
        print("stock info added to file")

StockOne = Stock("GOOG",0, 0, 0)
StockOne.getInfo()
