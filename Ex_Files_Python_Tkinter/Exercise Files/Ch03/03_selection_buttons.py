#!/usr/bin/python3
# selection_buttons.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()	# Top level window

checkbutton = ttk.Checkbutton(root, text = 'SPAM?')	# SPAM? Button
checkbutton.pack()

spam = StringVar()
spam.set('SPAM!')	# set SPAM! to spam variable
print(spam.get())

checkbutton.config(variable = spam, onvalue = 'SPAM Please!',
		   offvalue = 'Boo SPAM!')	# onvalue means checkbox checked, offvalue means unchecked
print(spam.get())	# Print in console

breakfast = StringVar()
ttk.Radiobutton(root, text = 'SPAM', variable = breakfast,
		value = 'SPAM').pack()	# Creates radio button (rounded)
ttk.Radiobutton(root, text = 'Eggs', variable = breakfast,
		value = 'Eggs').pack()
ttk.Radiobutton(root, text = 'Sausage', variable = breakfast,
		value = 'Sausage').pack()
ttk.Radiobutton(root, text = 'SPAM', variable = breakfast,
		value = 'SPAM').pack()	# Since 2 spam values, both will be highlighted when clicked on
print(breakfast.get()) # Note: value will be empty if no selection is made

checkbutton.config(textvariable = breakfast)	# Check button text will now change to whatever "breakfast" 												variable is set equal to

root.mainloop()
