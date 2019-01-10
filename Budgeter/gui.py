
f1= open("bills.txt","a+")
f1Lines = f1.readlines
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

import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
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
                           command=showStock)
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
                           command=showBudget)
        button2.pack()
        button3 = tk.Button(self, text="Main Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button3.pack(side="bottom", fill="x", pady=10)
		button4 = tk.Button(self, text="Start Budget Tool",
                           command=showBudget)
        button4.pack(side="bottom", fill="x", pady=10)
		debt = tkinter.BooleanVar()
		c1 = tkinter.Checkbutton(lbl ,text="Debt" ,variable=debt)
		c1.pack()
		
	



def showBudget:

		
	

def showStock:
	currStock = self.entry.get()
	Stock currentstock[currStock,0,0,0]
	self.currentstock.getInfo()
	stockFile = open("stockinfo.txt", "r")
	stockLines = stockFile.readlines()
	messagebox.showinfo("Stock Info", stockLines)
	stockFile.close()
			
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
	
