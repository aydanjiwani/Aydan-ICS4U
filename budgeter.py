from math import *
from bill import Bill

		
billOne = Bill("Student Loan", 250, 0.1, 10000)
billOne.showSchedule()
billOne.increasePayment(500)
billOne.showSchedule()
		

