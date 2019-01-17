from math import *
from bill import Bill
from debt import Debt
from stock import Stock
from budgetclass import Budget
import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox

fclearbills= open("bills.txt","w")
fcleardebts= open("debts.txt","w")
fclearbills.close()
fcleardebts.close()

class BudgeterGUI(tk.Tk):
	"""
	a tkinter object that holds all frames/screens to switch between
	Attributes:
	From tkinter library
	
	Methods:
	showframe(page_name:str) -> ()
		displays the set page
	
	
	"""

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		self.frames = {}
		self.frames["StartPage"] = StartPage(parent=container, controller=self)
		self.frames["PageOne"] = PageOne(parent=container, controller=self)
		self.frames["PageTwo"] = PageTwo(parent=container, controller=self)
		self.frames["StartPage"].grid(row=0, column=0, sticky="nsew")
		self.frames["PageOne"].grid(row=0, column=0, sticky="nsew")
		self.frames["PageTwo"].grid(row=0, column=0, sticky="nsew")
		self.show_frame("StartPage")
	
	def show_frame(self, page_name):
		frame = self.frames[page_name]
		frame.tkraise()


class StartPage(tk.Frame):
	"""
	a tkinter object that shows the main page
	Attributes:
	from tkinter library
	
	
	"""

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="Welcome to Budgeter", font=controller.title_font)
		label.pack(side="top", fill="x", pady=10)
		button1 = tk.Button(self, text="Open Stock Tool", command=lambda: controller.show_frame("PageOne"))
		button2 = tk.Button(self, text="Open Budget Tool",command=lambda: controller.show_frame("PageTwo"))
		button1.pack()
		button2.pack()


class PageOne(tk.Frame):
	"""
	a tkinter object that shows the stock tool page
	Attributes:
	from tkinter library
	
	
	"""

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label2 = tk.Label(self, text="Welcome to the Stock Tool", font=controller.title_font)
		label2.pack(side="top", fill="x", pady=10)
		button3 = tk.Button(self, text="Main Menu",command=lambda: controller.show_frame("StartPage"))
		button3.pack()
		button4 = tk.Button(self, text="Start Stock Tool",command= lambda: showStock())
		button4.pack()
		stockLabel = tk.Label(self, text="Enter Stock").pack(side="bottom", fill="x", pady=10)
		stockEnter = tk.Entry(self)
		stockEnter.pack()


class PageTwo(tk.Frame):
	"""
	a tkinter object that shows the budget tool page
	Attributes:
	from tkinter library
	
	
	"""

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		label = tk.Label(self, text="Welcome to the Budget Tool", font=controller.title_font)
		label.pack(side="top", fill="x", pady=10)
		button = tk.Button(self, text="Main Menu",command=lambda: controller.show_frame("StartPage"))
		button.pack()
		button2 = tk.Button(self, text="Start Budget Tool",command=lambda: showBudget())
		button2.pack()

	



def showBudget():
	"""
	displays the budget tool, and the completed budget
	
	Returns
	-----
	none
	Exceptions
	-------------
	IndexOutOfBoundsError: Raised when an attempt to submit a budget with an empty bill or debt list happens
	ValueError: Raised when a nonnumber is entered into a numerical field for a budget item
	
	"""
	messagebox.showinfo("Budget Tool","Tool enabled in console")
	f1= open("bills.txt","a+")
	f2= open("debts.txt","a+")
	submitted = False
	usingTool = True
	while(usingTool):
		while(submitted == False):
			print("press b to enter a bill, d to enter a debt, x to delete the last item, m to return to the main menu, s to submit a budget")
			userchoice = input()
			lastitem = "x"
			if (userchoice == "b"):
				print("Please enter name of bill")
				billName = input()
				print("Please enter cost of bill")
				billCost = float(input())
				f1.write(billName + "," +str(billCost) + "\n")
				lastitem = "b"
		
			elif (userchoice == "d"):
				print("Please enter name of debt")
				debtName = input()
				print("Please enter cost of debt")
				debtCost = float(input())
				print("Please enter interest rate of debt")
				debtRate = float(input())
				print("Please enter minimumpayment of debt")
				debtMinPay = float(input())
				print("Please enter principle of debt")
				debtPrinciple = float(input())
				f2.write(debtName + "," + str(debtCost) + "," + str(debtRate) +"," + str(debtPrinciple) + "," + str(debtMinPay) + "\n")
				lastitem = "d"
		
			
			elif (userchoice == "x"):
				if(lastitem == "x"):
					print("no items found")
				elif("lastitem" == "b"):
					lines = f1.readlines()
					lines = lines[:-1]
					f1.close()
					f1 = open("bills.txt", "w")
					fl.close()
					f1 = open("bills.txt", "a+")
					for i in range(0,len(lines)):
						f1.write(lines[i] + "\n" )
						
				
				elif("lastitem" == "d"):
					lines = f2.readlines()
					lines = lines[:-1]
					f2.close()
					f2 = open("debts.txt", "w")
					f2.close()
					f2 = open("debts.txt", "a+")
					for i in range(0,len(lines)):
						f2.write(lines[i] + "\n" )
				
			elif (userchoice == "m"):
				controller.show_frame("StartPage")
				return 0;
				
		
			elif (userchoice == "s"):
				f1.close()
				f1 = open("bills.txt", "r")
				f2.close()
				f2 = open("debts.txt", "r")
				f1Lines = f1.readlines()
				f2Lines = f2.readlines()
				BillList = []
				DebtList = []
		
				


				for i in range (0,len(f1Lines)):
					BillName,BillCost = f1Lines[i].strip("\n").split(",")
					BillList.append(Bill(BillName, float(BillCost)))
		
				for j in range (0,len(f2Lines)):
					DebtName,DebtCost,DebtInterest,DebtPrinciple,DebtMinPay = f2Lines[j].strip("\n").split(",")
					DebtList.append(Debt(DebtName,float(DebtCost),float(DebtInterest),float(DebtPrinciple), float(DebtMinPay)))
				f1.close()
				f2.close()
				print("Please enter your monthly income")
				income = int(input())
				print("Please enter your monthly savings goal")
				savingsGoal = int(input())
				print(DebtList)
				print(BillList)
				CurrentBudget = Budget(income, BillList, DebtList, savingsGoal, [])
				budgetsuccess = CurrentBudget.getInfo()
				submitted = budgetsuccess
			else:
				print("invalid choice")
		print("press v to view the current budget, m to move forward by a month, b to return to the budget, and c to finish using the tool")
		userchoice2 = input()
		if(userchoice2 == "v"):
			CurrentBudget.expenselist.sort(key=lambda x: x.cost, reverse=True)
			for i in range (0, len(self.CurrentBudget.expenselist)):
				print(vars(self.CurrentBudget.expenselist[i]))
				
		
		elif("userchoice == m"):
			CurrentBudget.budgetMonth()
			
		
		elif (userchoice == "b"):
			submitted = False
		
		elif (userchoice == "c"):
			usingTool = False
			
		
		
		else:
			print("invalid choice")
	controller.show_frame("StartPage")
	return 0;
		
			
	
			
	

		


def showStock():
	"""
	displays the stock tool, and the stock analysis
	
	Returns
	-----
	none
	Exceptions
	-----------
	KeyError: Raised when an invalid stock ticker is entered
	
	"""
	print("Please enter a stock Ticker")
	currStock = input()
	currentstock = Stock(currStock,0,0,0)
	currentstock.getInfo()
	stockFile = open("stockinfo.txt", "r")
	stockLines = stockFile.readlines()
	messagebox.showinfo("Stock Info", stockLines)
	stockFile.close()
			
if __name__ == "__main__":
    app = BudgeterGUI()
    app.mainloop()
	
