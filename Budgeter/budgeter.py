from math import *
from bill import Bill
from stock import Stock
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from pprint import pprint


f2 = open("STOCKLIST.txt", "r")
stocks = f2.read().splitlines()
stockindex = [Stock(stocks[i],0,0,0) for i in range (0,stocks.len())]

billOne = Bill("Student Loan", 250, 0.1, 10000)
billOne.showSchedule()
billOne.increasePayment(500)
billOne.showSchedule()
StockOne = Stock("GOOG",0, 0, 0)
StockOne.getInfo()
def recommend(criteria):
	
	
		if(criteria == 1):
			print("finding stocks with highest value")
			for i in range (0,stocks.len()):
				stockindex[i].getInfo()
			stocksByValue = sorted(stocks, key=lambda x: x.value, reverse=True)
			print("The stocks with the best value are:" + stocksByValue[0].name + stocksByValue[1].name + stocksByValue[2].name)
			
			
			
			
			
		if(criteria == 2):
			print("finding stocks with best trend")
			for i in range (0,stocks.len()):
				stockindex[i].getInfo()
			stocksByTrend = sorted(stocks, key=lambda x: (x.sma-x.value), reverse=True)
			print("The stocks with the best trend are:" + stocksByTrend[0].name + stocksByTrend[1].name + stocksByTrend[2].name)
			
		if(criteria == 3):
			print("finding stock with best RSI")
			for i in range (0,stocks.len()):
				stockindex[i].getInfo()
			stocksByRSI = sorted(stocks, key=lambda x: x.rsi, reverse=True)
			print("The stocks with the best RSI are:" + stocksByRSI[0].name + stocksByRSI[1].name + stocksByRSI[2].name)
