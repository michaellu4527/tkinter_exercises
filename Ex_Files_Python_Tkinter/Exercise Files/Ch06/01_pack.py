#!/usr/bin/python3
# pack.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

root = Tk()

# All widgets packed on left side, anchored in top left corner
ttk.Label(root, text='Hello, Tkinter!',
          background='yellow').pack(side=LEFT, anchor='nw')

# Align widgets left, 10px of padding in both x and y directions
ttk.Label(root, text='Hello, Tkinter!',
          background='blue').pack(side=LEFT, padx=10, pady=10)

label = ttk.Label(root, text='Hello, Tkinter!',
                  background='green')

# Align left, and fill up extra 10px of padding in both x and y direct
label.pack(side=LEFT, ipadx=10, ipady=10)
print(label)

for widget in root.pack_slaves():   # Returns a list of all the labels managed by pack manager
    widget.pack_configure(fill=BOTH, expand=True)   # Set properties to expand across entire screen
    print(widget.pack_info())

label.pack_forget()     # Forgets "label" which is the green label

root.mainloop()
