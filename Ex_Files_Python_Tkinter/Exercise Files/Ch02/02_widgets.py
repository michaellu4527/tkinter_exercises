#!/usr/bin/python3
# widgets.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk     # Imports themed widgets

root = Tk()     # Tk constructor

button = ttk.Button(root, text = 'Click Me')    # Creates a button. First parameter is the parent
button.pack()       # Adds button to window

print(button['text'])
button['text'] = 'Press Me'    # Changes text on button
button.config(text = 'Push Me')     # Another way to do the same thing
print(button.config())      # Returns the dictionary

print(str(button))      # Returns Tk widget name associated with button
print(str(root))

ttk.Label(root, text ='Hello, Tkinter!').pack()     # Creates label to the GUI. NOTE:                                                                   since it's not assigned to a                                                                      variable, we can never access this label again

# mainloop() add
root.mainloop()
