from math import *
from bill import Bill
from stock import Stock
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from pprint import pprint





billOne = Bill("Student Loan", 250, 0.1, 10000)
billOne.showSchedule()
billOne.increasePayment(500)
billOne.showSchedule()
StockOne = Stock("GOOG",0, 0, 0)
StockOne.getInfo()

def Bubblesort (sortlist):
	donezo = false
	while(!donezo):
		donezo = true
		for i in range (0,len(sortlist)):
	
			if(sortlist[i] > sortlist[i+1])
				placeholder = sortlist[i]
				sortlist[i] = sortlist[i+1]
				sortlist[i+1] = placeholder
				donezo = false
	
	

def Insertionsort (sortlist):
	donezo = false
	while(!donezo):
		donezo = true
		for i in range (0,len(sortlist)):
			for i in range 
				donezo = false
	