from math import *
from bill import Bill
class Debt(Bill):
	'''
	A debt object that hold the name, monthly minimum, interest rate of each loan/bill
	
	Attributes
	----------
	name: str
		The name of the bill
	monthCost : float
		The minumum amount that must be paid each month
	interest : float
		The interest on the payments (0 if not present)
	principle: float
                Initial amount that must be paid back (0 if for a monthly bill)

	Methods
	-------
	
	payMonth() -> None
		Applies the current monthly payment and interest to the bill
	increasePayment() -> None
		Adjusts the monthly payment
	showSchedule() -> None
		Shows how long it will take to pay off the principle, returns null if no principle
	'''
	
	def __init__(self, name, monthCost, interest, principle, priority):
		'''
		Parameters
	----------
	name: str
		The name of the bill
	monthCost : float
		The minumum amount that must be paid each month
	interest : float, optional
		The interest on the payments (0 if not present)
	principle: float, optiona;
                Initial amount that must be paid back (0 if for a monthly bill)
        
		
			
		'''
		
		super().__init__(name, monthCost)
		self.interest = interest
		self.principle = principle
		self.priority = priority

		
		
	def payMonth(self):
		'''
		Conducts the monthly payment, reducing the principle and adding interest if applicable.
		
		Returns
		------
		monthCost: float
		The amount paid this month
                
		'''
		if(self.principle!=0):
			self.principle = self.principle - self.monthCost + self.principle* self.interest
			if (self.principle == 0):
				self.monthCost = 0
				print("Paid $" + str(self.monthCost), " on " + self.name, "reducing the original debt to 0. Congratulations!")
			else:
				print("Paid $" + str(self.monthCost), " on " + self.name, "reducing the original debt by " + str(self.monthCost - self.principle-self.interest)

		else:
			print("Paid " + str(self.monthCost) "for " + self.name)

		return self.monthCost
	
	
	def increasePayment(self, newPayment: float):
		'''
		Attempts to change the monthly payment
		
		This will change self.monthCost to the value of newPayment
		Parameters
		----------
		newPayment : float
			The value to change the monthCost to.
				
		Returns
		-------
		bool
			True if the method was successful
			False if the method attempted to bring the value below zero
			
		
		Raises
		------
		AttributeException
			If the attribute is non-existant and Python cannot add to it
		TypeError
			If the value of increase is not a float and it is trying to
			be added to self.price : float.
		
		'''
		self.monthCost = newPayment
		print("monthly payment changed to: " str(self.monthCost)
		if monthCost > 0:
			return True
		return False
		
		
	
	def showSchedule(self):
		'''
		Calculates how many payment periods it will take
		Returns
		-------
		monthCount: float
			The number of payment periods it will take to pay off the debt
		
		
		
		'''
		monthCount = 0
		testvar = self.principle
		while(testvar > 0):
			testvar -= self.monthCost
			testvar += testvar * self.interest
			monthCount+=1
		print("With a debt of " +str(self.principle), "and a monthly interest rate of " + str(self.interest) + "%, it would take " + str(months) "to pay off this debt at" + str(monthCost) +"$ per month."  )
		return monthCount
		
	

		


