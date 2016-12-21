#!/usr/bin/python3
# virtual.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

entry = ttk.Entry(root)
entry.pack()

entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))

entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')   # Create virtual event
entry.bind('<<OddNumber>>', lambda e: print('Odd Number!'))     # Bind virtual event for it to run

print(entry.event_info('<<OddNumber>>'))    # Prints out information about virtual event

# Will trigger event automatically
entry.event_generate('<<OddNumber>>')
entry.event_generate('<<Paste>>')

# Deletes the virtual event
entry.event_delete('<<OddNumber>>')

root.mainloop()
