from math import *
class Bill():
	'''
	A debt object that hold the name, monthly minimum, interest rate of each loan/bill
	
	Attributes
	----------
	name: str
		The name of the bill
	monthCost : float
		The minumum amount that must be paid each month

	Methods
	-------
	
	payMonth() -> None
		Applies the current monthly payment and interest to the bill
	increasePayment() -> None
		Adjusts the monthly payment
	showSchedule() -> None
		Shows how long it will take to pay off the principle, returns null if no principle
	'''
	
	def __init__(self, name, monthCost):
		'''
		Parameters
	----------
	name: str
		The name of the bill
	monthCost : float
		The minumum amount that must be paid each month

        
		
			
		'''
		
		self.name = name
		self.monthCost = monthCost


		
		
	def payMonth(self):
		'''
		Conducts the monthly payment, reducing the principle and adding interest if applicable.
		
		Returns
		------	
		monthCost: float
		The amount paid this month
                
		'''

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
		
		
	


		


