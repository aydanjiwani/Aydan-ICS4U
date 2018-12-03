from math import *
from bill import Bill
f= open("bills.txt","r")
fLines = f.readlines
BillList = []


for x in fLines:
	BillName,BillCost,BillInterest,BillPrinciple = x.split(",")
	BillList.append(Bill(self, BillName, BillCost, BillInterest,BillPrinciple))