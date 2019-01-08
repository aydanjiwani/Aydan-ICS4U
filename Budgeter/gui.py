from tkinter import *
 
window = Tk()
 
window.title("Welcome to 'Budgeter)
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=3)
btn = Button(window, text="Stock Tool")
 
btn.grid(column=1, row=0)
btn2 = Button(window, text="Budget Tool")
 
btn2.grid(column=1, row=6)
window.mainloop()
window.geometry('800x600')