#!/usr/bin/python3
# label.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

label = ttk.Label(root, text = "Hello, Tkinter!")   # Constructor method
label.pack()
label.config(text = 'Howdy, Tkinter!')  # Changing text on label
label.config(text = 'Howdy, Tkinter! It\'s been a really long time since we last met.  Great to see you again!')
label.config(wraplength = 150)  # Wraps text after 150px
label.config(justify = CENTER)  # Aligns text center (left/right/oenter)
label.config(foreground = 'blue', background = 'yellow')    # Foreground = text, background = color of label                                                                background
label.config(font = ('Courier', 18, 'bold'))    # Font family, font size, font weight
label.config(text = 'Howdy, Tkinter!')

logo = PhotoImage(file = 'python_logo.gif') # change path to image as necessary
label.config(image = logo)  # letting Tk know that "logo" is an image
label.config(compound = 'text') # will only display image
label.config(compound = 'center')   # Displays text overlayed on top of image in center
label.config(compound = 'left') # Displays image to left of text

label.img = logo    # ALWAYS do this since the "logo" object is a LOCAL variable. It will disappear if used                         inside a function
label.config(image = label.img) # Now the image will stay as long as the label exists

root.mainloop()
