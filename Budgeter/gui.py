
f= open("bills.txt","a+")
fLines = f.readlines
f2= open("debts.txt","a+")
f2Lines = f2.readlines
BillList = []
DebtList = []
from tkinter import * as tk
from math import *
from bill import Bill
from debt import Debt
from budgetclass import Budget

for x in fLines:
	BillName,BillCost = x.split(",")
	BillList.append(Bill(self, BillName, BillCost))
	
for x in f2Lines:
	DebtName,DebtCost,DebtInterest,DebtPrinciple,DebtPriority = x.split(",")
	DebtList.append(Debt(self, DebtName,DebtCost,DebtInterest,DebtPrinciple,DebtPriority))
 
window = Tk()
window.geometry('800x600')
window.title("Welcome to Budgeter)
int currenttask = 0
 
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=3)

btn = Button(window, text="Stock Tool", command = showStock) 
btn.grid(column=1, row=0)
if(currenttask != 0):
	btn.config(state="disabled")

btn2 = Button(window, text="Budget Tool", command = showBudget)
btn2.grid(column=1, row=3) 
if(currenttask != 0):
	btn.config(state="disabled")

btn2 = Button(window, text="Return to main menu Tool", command = mainMenu)
btn2.grid(column=1, row=3) 


def mainMenu:
	
	
def showBudget:
	if (currenttask !=1):
		break
	else:
		print("Type add to add a budget item, edit to edit the most recent budget item, and delete to delete the most recent item")	
		x = input()
		if(input = "add"):
			print("Type b to add a bill and d to add a debt")
				if(input = "b"):
				
				if(input = "d"):
		
		if(input = "edit"):
			print("Type b to edit the most recent bill and d to edit the most recent debt")
		
		if(input = "delete"):
			print("Type b to delete the most recent bill and d to delete the most recent debt")
		
		
	

def showStock:
	if (currenttask !=2):
		break
	else:
		print("Please enter a stock Ticker to analyze):
			currStock = input()
			Stock currentstock[currStock,0,0,0]
			self.currentstock.getInfo()
			

window.mainloop()
