#!/usr/bin/python3
# selection_boxes.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

month = StringVar()
combobox = ttk.Combobox(root, textvariable = month) # Creates box with dropdown menu
combobox.pack()
combobox.config(values = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(month.get())
month.set('Dec')    # Change current value to Dec
month.set('Not a month!')   # Careful as you can set something random to it as well

# User can also enter in anything they want into the dropdown

year = StringVar()

# Creates box with up and down arrow for changing value in textbox
Spinbox(root, from_ = 1990, to = 2014, textvariable = year).pack()  # Values from 1990 to 2014
print(year.get())

root.mainloop()
