#!/usr/bin/python3
# entry.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

entry = ttk.Entry(root, width = 30) # Adds single line text box of 30px width
entry.pack()

entry.get()

# NO set method. Can only delete or insert
entry.delete(0, 1)  # Deletes 0th char to 1st char (non inclusive)
entry.delete(0, END)    # Deletes all text
entry.insert(0, 'Enter your password')  # Adds specified text

entry.config(show = '*')    # Will place stars when text is entered
entry.state(['disabled'])   # Disables text box
entry.state(['readonly'])   # User can select text, but CANNOT change it
entry.state(['!disabled'])

root.mainloop()
