from tkinter import * 
from tkinter.ttk import *

from time import strftime 

root = Tk() 
root.title('Clock') 

def time(): 
	string = strftime('%H:%M:%S %p') 
	lbl.config(text = string) 
	lbl.after(1000, time) 

def buttonCommand():
	lbl.config(text = "Soda") 

lbl = Label(
	root,
	font = ('calibri', 40, 'bold'), 
	background = 'purple', 
	foreground = 'white'
)
button = Button(
	root,
	text='Stop', 
	width=25, 
	command=buttonCommand,
)

lbl.pack(anchor = 'center')
button.pack() 
time()
  
mainloop() 