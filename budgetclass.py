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
"""
An object that holds a list of all existing bills and debts
	
	Attributes
	----------
	salary : float
		The current income
	bills : list
		A list of all bills that must be paid in the budget
	debts : list
		A list of all debts that must be paid in the budget
	saving:
		The amount each month that the user wants to assign to savings
	
	Methods
	-------
	getInfo() -> none
		A method that prints the relevant info
	

"""
  def __init__ (self, salary, bills, debts, saving):
	self.salary = salary
	self.bills = bills
	self.debts = debts
	self.saving = saving
