#!/usr/bin/python3
# button.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk        
    
root = Tk()

button = ttk.Button(root, text = "Click Me")    # Creating button with text "Click ME"
button.pack()

def callback(): # Needs to be used whenever you create a button
    print('Clicked!')

button.config(command = callback)   # Will call the callback function when button is clicked
button.invoke()

button.state(['disabled'])  # Disables button
print(button.instate(['disabled'])) # Asks if button is disabled (Will return True)
button.state(['!disabled']) # Turning disabled off button
print(button.instate(['!disabled']))    # Asks if button is not disabled

logo = PhotoImage(file = 'python_logo.gif') # change path to image as necessary
button.config(image = logo, compound = LEFT)    # Places logo to left
small_logo = logo.subsample(5, 5)   # Scales down image size
button.config(image = small_logo)   # Display new image

root.mainloop()
