#!/usr/bin/python3
# panedwindow.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

panedwindow = ttk.Panedwindow(root, orient = HORIZONTAL)
panedwindow.pack(fill = BOTH, expand = True)

frame1 = ttk.Frame(panedwindow, width = 100, height = 300, relief = SUNKEN)
frame2 = ttk.Frame(panedwindow, width = 400, height = 400, relief = SUNKEN)
panedwindow.add(frame1, weight = 1)
panedwindow.add(frame2, weight = 4) # 4 times the size of frame1, weight specified so size is dynamic when window expanded

frame3 = ttk.Frame(panedwindow, width = 50, height = 50, relief = SUNKEN)   # Notice no weight, so size is STATIC
panedwindow.insert(1, frame3)   # First parameter is index. 0 indexed, so will be placed in the 2nd position
panedwindow.forget(1)   # Removes frame in specified index

root.mainloop()
