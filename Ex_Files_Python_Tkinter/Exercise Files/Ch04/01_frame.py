#!/usr/bin/python3
# frame.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

# Frames are like containers in HTML

frame = ttk.Frame(root) # Create frame
frame.pack()
frame.config(height = 100, width = 200) # Size of frame
frame.config(relief = RIDGE)    # Adjusting border
ttk.Button(frame, text = 'Click Me').grid() # Notice "frame" is the parent and NOT root
frame.config(padding = (30, 15))    # number of pixels in x and y direction
ttk.LabelFrame(root, height = 100, width = 200, text = 'My Frame').pack()   # Adds a frame that comes with a                                                         label underneath. Text will be displayed in top left corner

root.mainloop()
