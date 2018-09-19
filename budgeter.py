from math import *
class Bill():
	'''
	A debt object that hold the name, monthly minimum, interest rate of each loan/bill
	
	Attributes
	----------
	name: str
		The price of the book in dollars and cents (example format ###.##)
	monthCost : float
		The minumum amount that must be paid each month
	interest : float
		The interest on the payments (0 if not present)
	principle: float
                Initial amount that must be paid back (0 if for a monthly bill)
        lateFee: float
                Amount that must be paid if you pay late
		
	Methods
	-------
	
	payMonth() -> None
		Applies the current monthly payment and interest to the bill
	increasePayment() -> None
		Adjusts the monthly payment
	showSchedule() -> None
		Shows how long it will take to pay off the principle, returns null if no principle
	'''
	
	def __init__(self, name, monthCost, interest, principle, lateFee):
		'''
		Paremeters
	----------
	name: str
		The price of the book in dollars and cents (example format ###.##)
	monthCost : float
		The minumum amount that must be paid each month
	interest : float, optional
		The interest on the payments (0 if not present)
	principle: float, optiona;
                Initial amount that must be paid back (0 if for a monthly bill)
        lateFee: float, optional
                Amount that must be paid if you pay late
			
		
			
		'''
		
		self.name = name
		self.monthCost = monthCost
		self.interest = interest
		self.principle = principle
		self.lateFee = lateFee
		
		
	def payMonth(self) -> None:
		'''
   Conducts the monthly payment, paying interest and principle if applicable
                
		'''
		if(principle!=0):
      principle = principle - monthCost + principle* interest
      if (principle == 0):
        monthCost = 0
        print("Paid $" + str(monthCost), " on " + name, "reducing the original debt to 0. Congratulations!")
        else:
          print("Paid $" + str(monthCost), " on " + name, "reducing the original debt by " + str(monthCost - interest)

    else:
    print("Paid " + str(monthCost) "for " + name)

		return monthCost
	
	
	def increasePayment(self) -> None:
		'''
		Changes the monthly cost
		
		'''
    self.monthCost = input("Please enter the new monthly payment")
		print("monthly payment changed to: " str(monthCost)
		return monthCost
		
		
	
	def showSchedule(self) -> None:
		'''
		Attempts to increase the price of the book
		
		This will add the value of 'increase' to self.price.  If there is any issues, 
		it will return False if it attempts to lower the price below zero.
		
		Parameters
		----------
		increase : float
			The value to increase the price by.  This value can be negative;
			however, it will never lower the value below zero.  If this happens
			the function will return False.
				
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
    monthCount = 0
		testvar = principle
		while(testvar >= 0):
      testvar -= monthCost
      testvar += testvar * interest
      monthCount++
    print("With a debt of " +str(principle), "and a monthly interest rate of " + str(interest) + "%, it would take " + str(months) "to pay off this debt at" + str(monthCost) +"$ per month."  )
    return monthCount

		

