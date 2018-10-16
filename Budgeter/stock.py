from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from pprint import pprint

class Stock():
"""
An object that holds the information of a selected stock
	
	Attributes
	----------
	name: str
		The name of the stock (Ticker)
	Value : float
		The most recent closing price of the stock
	RSI : float
		A magic number that can be used to determine if a stock is oversold or undersold (in theory)
	SMA: float
        A magic number that can be used to determine if a stock is trending up or down (in theory)
	Methods
	-------
	getInfo() -> none
		A method that prints the relevant info of the stock
	

"""
    def __init__(self, name, value, RSI, SMA):
        self.name = name
        self.value = value
        self.RSI = RSI
        self.SMA = SMA
		"""
    Parameters
	----------
	name: str
		The name of the stock (Ticker)
	Value : float
		The most recent closing price of the stock
	RSI : float
		A magic number that can be used to determine if a stock is oversold or undersold (in theory)
	SMA: float
        A magic number that can be used to determine if a stock is trending up or down (in theory)
   """
    

    def getInfo(self):
	'''
		Prints all relevant info about stock to a text file
		
		Returns
		------
		none
                
		'''
        f = open("stockinfo.txt", "w")
        ts = TimeSeries(key='GZR6JEGOB3LF6RCB')
        tc = TechIndicators(key='GZR6JEGOB3LF6RCB',output_format='pandas')
        data, meta_data = ts.get_daily(self.name)
        data2, meta_data2 = tc.get_rsi(self.name)
        data3, meta_data3 = tc.get_sma(self.name)
        teststring = data['2018-10-12']
        print(teststring)
        self.value = float(teststring['4. close'])
        f.write("The stock chosen is: " + self.name + "\n")
        f.write("The most recent closing price is: " + str(self.value) + "\n")
        print("stock info added to file")

StockOne = Stock("GOOG",0, 0, 0)
StockOne.getInfo()
