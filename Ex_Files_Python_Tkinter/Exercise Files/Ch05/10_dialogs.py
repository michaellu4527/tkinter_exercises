#!/usr/bin/python3
# dialogs.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import messagebox

# Pops up lowest severity message box
messagebox.showinfo(title="A Friendly Message", message='Hello, Tkinter!')
print(messagebox.askyesno(title='Hungry?', message='Do you want SPAM?'))    # Has option yes/no

from tkinter import filedialog

filename = filedialog.askopenfile()     # Popup window for opening a file
print(filename.name)

from tkinter import colorchooser

'''Makes pop up of color picker tool with initial color set at white. Tkinter will return the
    rgb of any color that is selected along w/ its hex value'''
print(colorchooser.askcolor(initialcolor="#FFFFFF"))
