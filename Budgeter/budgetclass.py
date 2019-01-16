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
	
	def getInfo():
		"""
		Analyzes the budget and returns if it is usable or not
		Returns
			-------
			bool
				True if the budget was valid
				False if there was not enough money
			
	
		"""
		self.expenselist = []
		for i in range 0,len(bills):
			salary -= bills[i].monthCost
			self.expenselist.append(bills[i])
		salary -= savings
		for i in range 0,len(debts):
				salary -= debts[i].minimumPayment
				self.expenselist.append(debts[i])
		if salary <= 0:
			print("Error, not enough funds to meet savings goal and pay bills. Try reducing bills or savings goal to pay off debts")
			return False
		else:
			int testvar = -1
			int targetDebt = -1
			for i in range 0,len(debts):
				if debts[i].interest > testvar:
					testvar = debts[i].interest
					targetDebt = i
				
		self.debts[targetDebt].increasePayment(salary)

		print("Total of"+ len(self.expenselist) +"Items found")
		print(salary + "was left over after savings and bills and used to pay off" + debts[targetDebt].name)
		return True
		
	def budgetMonth():
		for i in range (0, len(debts)):
			self.debts[i].payMonth()
			print("payments to debts applied for the month")
	
			
		
		
			
		
		
		
