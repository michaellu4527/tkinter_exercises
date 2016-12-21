#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

root = Tk()

button1 = ttk.Button(root, text='Button 1')
button2 = ttk.Button(root, text='Button 2')
button1.pack()
button2.pack()

style = ttk.Style()  # Creating style object

print(style.theme_names())  # Returns all style names on system
print(style.theme_use())  # What system is currently using
style.theme_use('classic')  # Changing theme of buttons
style.theme_use('vista')  # Back to default

print(button1.winfo_class())
style.configure('TButton', foreground='blue')   # Changes text on button to blue

# Tkinter version of derived class. Alarm is derived from TButton so it inherits all its properties
style.configure('Alarm.TButton', foreground='orange',
                font=('Arial', 24, 'bold'))

button2.configure(style='Alarm.TButton')    # Change button2 style to to new Alarm style
style.map('Alarm.TButton', foreground=[('pressed', 'pink'),
                                       ('disabled', 'grey')])   # Properties are in PAIRS
button2.state(['disabled'])     # Disables button2

print(style.layout('TButton'))  # Lists how style of a button is laid out
print(style.element_options('Button.label'))    # Lists styles available for Button.label
print(style.lookup('TButton', 'foreground'))    # Returns current value of any style with specified
                                                # property

root.mainloop()
