from math import *
class Debt():
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
	
	def __init__(self, author, title, price=0.00):
		'''
		Constructor to build a book object
		
		
		Parameters
		----------
		author : str
			The name of the author of the book
		price : float, optional
			The initial price of the book
			The default price of a book is 0.00 if none is entered
		title : str
			The title of the book
			
		..note:: that the "self" parameter is not listed in this section.
			
		
			
		'''
		
		self.author = author
		self.price = price
		self.title = title
		
		
	def printAuthor(self) -> None:
		'''
		Prints the name of the author to the console
		
		
		.. warning:: The rest of the documentation will be here at some point.
		
		'''
		print(self.author)
		return
	
	
	def printPrice(self) -> None:
		'''
		Prints the price of the book to the console
		
		.. warning:: The rest of the documentation will be here at some point.
		
		'''
		print(self.price)
		return
		
		
	def printTitle(self) -> None:
		'''
		Prints the title of the book to the console
		
		.. warning:: The rest of the documentation will be here at some point.
		
		'''
		print(self.title)
		return
	
	
	def increasePrice(self, increase : float) -> None:
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
		
		if self.price + increase > 0:
			self.price += increase
			return True
		return Falses

bookOne = Book("Terry Pratchett", "Guards! Guards!", 5.99)
bookTwo = Book("Robert Jordan", "The Eye of the World", 8.99)

bookOne.printAuthor()
bookOne.printPrice()
bookOne.printTitle()
bookOne.increasePrice(1)
bookOne.printPrice()

bookTwo.printAuthor()
bookTwo.printPrice()
bookTwo.printTitle()
bookTwo.increasePrice(-6)
bookTwo.printPrice()
try:
	bookTwo.increasePrice("Hello!")
except TypeError:
	print ("Raised a TypeError as expected")
except Exception:
	print ("Some other Error popped up?")
