#!/usr/bin/python3
# progressbar_scale.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200)	# Creates progress bar
progressbar.pack()

progressbar.config(mode = 'indeterminate')	# Use when you don't know how long operation will take
progressbar.start()	# Will start cycling of progress bar between window.
progressbar.stop()	# Will stop cycling

progressbar.config(mode = 'determinate', maximum = 11.0, value = 4.2)	# Sets PB at paricular position
progressbar.config(value = 8.0)	# Changing progress of progress bar
progressbar.step()	# Increments progress bar by 1
progressbar.step(5)	# Increments by 5, and exceeds PB, so it will wrap back to front

value = DoubleVar()
progressbar.config(variable = value)

scale = ttk.Scale(root, orient = HORIZONTAL,
		  length = 400, variable = value,
		  from_ = 0.0, to = 11.0)	# Creates scale underneath progress bar w/ same "value" so it tracks with 									the PB
scale.pack()
scale.set(4.2)	# Can manually set scale
print(scale.get())

root.mainloop()
