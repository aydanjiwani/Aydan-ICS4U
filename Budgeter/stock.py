from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from pprint import pprint
from binarysearch import binarySearch



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
    
	def checkRanking(self, criteria):
		'''
		Prints the ranking of a given stock in a criteria
		Parameters
		----------
		Criteria: int
			The criteria for the stock ranking
		Returns
		------
		ranking: int
			the ranking of that stock
		
		Note: Function not implemented due to exceeding free API call limit
                
		'''
		f2 = open("STOCKLIST.txt", "r")
		stocks = f2.read().splitlines()
		stockindex = [Stock(stocks[i],0,0,0) for i in range (0,stocks.len())]
		values = []
		if(criteria == 1):
			key = self.value
			for i in range (0,stocks.len()):
				self.stockindex[i].getInfo()
				values.append(stockindex[i].value)
		ranking = binarySearch(values, stockindex.len(), 0, key)
		print(self.name + "is ranked" + ranking)
		f2.close()
		return ranking
		if(criteria == 2):
			key = self.sma-self.value
			for i in range (0, stocks.len()):
				if(key == self.stockindex[i].sma-stockindex[i].value):
					print(self.name + "is ranked" + i) 
					f2.close()
					return i
		if(criteria == 3):
			key = self.rsi
			for i in range (0, stocks.len()):
				if(key == self.stockindex[i].rsi):
					print(self.name + "is ranked" + i) 
					f2.close()
					return i
		
	def getInfo(self):
		'''
		Prints all relevant info about stock to a text file
		
		Returns
		------
		none
                
		'''
		
		f = open("stockinfo.txt", "w")
		ts = TimeSeries(key='GZR6JEGOB3LF6RCB')
		tc = TechIndicators(key='GZR6JEGOB3LF6RCB')
		data, meta_data = ts.get_daily(self.name)
		data2, meta_data2 = tc.get_rsi(self.name)
		data3, meta_data3 = tc.get_sma(self.name)
		self.rsi = float(data2['2019-01-16']['RSI'])
		self.sma = float(data3['2019-01-16']['SMA'])
		teststring = data['2019-01-16']
		self.value = float(teststring['4. close'])
		f.write("The stock chosen is: " + self.name + "\n")
		f.write("The most recent closing price is: " + str(self.value) + " more info in console")
		if(self.rsi > 70):
			print("this stock has a high RSI and is currently oversold. The price may fall soon")
		elif(self.rsi < 30):
			print("this stock has a low RSI and is currently overbought. The price may rise soon")
		else:
			print("the stock is trading at normal levels")
		if(self.value > self.sma):
			print("the price of this stock is currently higher than the moving average. it is trending upwards")
		else:
			print("the price of this stock is currently lower than the moving average. it is trending downwards")
		f.close()
		
		
		
		


