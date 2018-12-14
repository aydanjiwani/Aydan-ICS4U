from math import *
from bill import Bill
from debt import Debt
f= open("bills.txt","r")
fLines = f.readlines
f2= open("debts.txt","r")
f2Lines = f2.readlines
BillList = []
DebtList = []

for x in fLines:
	BillName,BillCost = x.split(",")
	BillList.append(Bill(self, BillName, BillCost))
	
for x in f2Lines:
	DebtName,DebtCost,DebtInterest,DebtPrinciple,DebtPriority = x.split(",")
	DebtList.append(Debt(self, DebtName,DebtCost,DebtInterest,DebtPrinciple,DebtPriority))	
	
class Budget():
  def __init__ (self, salary, bills, debts):
	self.salary = salary
	self.bills = bills
	self.debts = debts
	
