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

