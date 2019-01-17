from math import *
from bill import Bill
from debt import Debt


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

	def __init__ (self, salary, bills, debts, saving, expenselist):
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
		expenselist : list
			A list of all bills and debts that must be paid in the budget
		"""
		self.salary = salary
		self.bills = bills
		self.debts = debts
		self.saving = saving
		self.expenselist = expenselist
	
	def getInfo(self):
		"""
		Analyzes the budget and returns if it is usable or not
		Returns
			-------
			bool
				True if the budget was valid
				False if there was not enough money
			
	
		"""
		self.expenselist = []
		currSalary = self.salary
		for i in range (0,len(self.bills)):
			currSalary -= self.bills[i].monthCost
			self.expenselist.append(self.bills[i])
		currSalary -= self.saving
		for i in range (0,len(self.debts)):
				currSalary -= self.debts[i].minimumPayment
				self.expenselist.append(self.debts[i])
		if currSalary <= 0:
			print("Error, not enough funds to meet savings goal and pay bills. Try reducing bills or savings goal to pay off debts")
			return False
		else:
			testvar = -1
			targetDebt = 0
			for i in range (0,len(self.debts)):
				if self.debts[i].interest > testvar:
					testvar = self.debts[i].interest
					targetDebt = i
				
		self.debts[targetDebt].increasePayment(currSalary)

		print("Total of "+ str(len(self.expenselist)) +" Items found")
		print(str(currSalary) + " was left over after savings and bills and used to pay off " + self.debts[targetDebt].name)
		return True
		
	def budgetMonth(self):
		for i in range (0, len(self.debts)):
			self.debts[i].payMonth()
			print("payments to debts applied for the month")
	
			
		
		
			
		
		
		
