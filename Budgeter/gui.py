
from tkinter import *
from math import *
from bill import Bill
from debt import Debt
from budgetclass import Budget





import tkinter as tk
from tkinter import font as tkfont 

class BudgeterGUI(tk.Tk):

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
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Open Stock Tool",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Open Budget Tool",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to the Stock Tool", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
		button2 = tk.Button(self, text="Start Stock Tool",
                           command= lambda: showStock)
        button2.pack()
		stockLabel = tk.Label(self, text="Enter Stock").grid(row=0)

		e1 = tk.Entry(self)
		e1.grid(row=0, column=1)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to the Budget Tool", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
		button2 = tk.Button(self, text="Start Budget Tool",
                           command=lambda: showBudget)
        button2.pack()

		"""
		debt = tkinter.BooleanVar()
		c1 = tkinter.Checkbutton(lbl ,text="Debt" ,variable=debt)
		c1.pack()
		"""
	



def showBudget:
	messagebox.showinfo("Budget Tool","Tool enabled in console")
	f1= open("bills.txt","a+")
	f2= open("debts.txt","a+")
	submitted = False
	usingTool = True
	while(usingTool):
		while(!submitted):
			print("press b to enter a bill, d to enter a debt, x to delete the last item, m to return to the main menu, s to submit a budget"
			userchoice = input()
			lastitem = "x"
			if userchoice == "b":
				print("Please enter name of bill")
				billName = input()
				print("Please enter cost of bill")
				billCost = input()
				f1.append(billName + "," +billCost)
				lastitem = "b"
		
			elif userchoice == "d":
				print("Please enter name of debt")
				debtName = input()
				print("Please enter cost of debt")
				debtCost = input()
				print("Please enter interest rate of debt")
				debtRate = input()
				print("Please enter minimumpayment of debt")
				debtMinPay = input()
				print("Please enter principle of debt")
				debtPrinciple = input()
				f2.append(debtName + "," + debtCost + "," + debtRate +"," + debtPrinciple + "," + debtMinPay)
				lastitem = "d"
		
			
			elif userchoice == "x":
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
						f1.append(lines[i] + "\n" )
						
				
				elif("lastitem" == "d"):
					lines = f2.readlines()
					lines = lines[:-1]
					f2.close()
					f2 = open("debts.txt", "w")
					f2.close()
					f2 = open("debts.txt", "a+")
					for i in range(0,len(lines)):
						f2.append(lines[i] + "\n" )
				
			elif userchoice == "m":
				controller.show_frame("StartPage")
				return 0;
				
		
			elif userchoice == "s":
				f1Lines = f1.readlines()
				f2Lines = f2.readlines()
				BillList = []
				DebtList = []


				for x in f1Lines:
					BillName,BillCost = x.split(",")
					BillList.append(Bill(self, BillName, BillCost))
		
				for x in f2Lines:
					DebtName,DebtCost,DebtInterest,DebtPrinciple,DebtPriority = x.split(",")
					DebtList.append(Debt(self, DebtName,DebtCost,DebtInterest,DebtPrinciple,DebtPriority))
				f1.close()
				f2.close()
				print("Please enter your monthly income")
				income = input()
				CurrentBudget = Budget(BillList, DebtList, income, 0, [])
				budgetsuccess = self.CurrentBudget.getInfo()
				submitted = budgetsuccess
			else:
				print("invalid choice")
		print("press v to view the current budget, m to move forward by a month, b to return to the budget, and c to finish using the tool")
		userchoice2 = input()
		if(userchoice2 == "v"):
			self.CurrentBudget.expenselist.sort(key=lambda x: x.cost, reverse=True)
			for i in range (0, len(self.CurrentBudget.expenselist):
				print(vars(self.CurrentBudget.expenselist[i]))
				
		
		elif("userchoice == m"):
			self.CurrentBudget.budgetMonth()
			
		
		elif (userchoice == "b"):
			submitted = False
		
		elif (userchoice == "c"):
			usingTool = False
			
		
		
		else:
			print("invalid choice")
	controller.show_frame("StartPage")
	return 0;
		
			
	
			
	

		


def showStock:
	currStock = self.entry.get()
	Stock currentstock[currStock,0,0,0]
	self.currentstock.getInfo()
	stockFile = open("stockinfo.txt", "r")
	stockLines = stockFile.readlines()
	messagebox.showinfo("Stock Info", stockLines)
	stockFile.close()
			
if __name__ == "__main__":
    app = BudgeterGUI()
    app.mainloop()
	
