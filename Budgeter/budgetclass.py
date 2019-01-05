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
	getInfo() -> Bool
		A method that prints the relevant info and returns if the budget is valid
	

"""

  def __init__ (self, salary, bills, debts, saving):
  """
  Parameters
	----------
	salary : float
		The current income
	bills : list
		A list of all bills that must be paid in the budget
	debts : list
		A list of all debts that must be paid in the budget
	saving:
		The amount each month that the user wants to assign to savings
  
  """
	self.salary = salary
	self.bills = bills
	self.debts = debts
	self.saving = saving
	
def getInfo():
	"""
	Analyzes the budget and returns if it is usable or not
	Returns
		-------
		bool
			True if the budget was valid
			False if there was not enough money
			
	
	"""
	for i in range 0,len(bills):
		salary -= bills[i].monthCost
	salary -= savings
	for i in range 0,len(debts):
			salary -= debts[i].minimumPayment
	if salary <= 0:
		print("Error, not enough funds to meet savings goal and pay bills. Try reducing bills or savings goal to pay off debts")
		return False
	else:
	int testvar = 99999
	int targetDebt = -1
		for i in range 0,len(debts):
			if debts[i].interest < testvar:
				testvar = debts[i].interest
				targetDebt = i
				
	this.debts[targetDebt].increasePayment(salary)
	print(salary + "was left over after savings and bills and used to pay off" + debts[targetDebt].name)
	return True
	
			
		
		
			
		
		
		
