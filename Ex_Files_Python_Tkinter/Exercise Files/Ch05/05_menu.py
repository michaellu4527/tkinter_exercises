#!/usr/bin/python3
# menu.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

root = Tk()

root.option_add('*tearOff', False)  # ALWAYS include this line or else menu will look bad
menubar = Menu(root)     # Constructing menu
root.config(menu=menubar)    # Set menu to menubar
file = Menu(menubar)        # Creating menu options
edit = Menu(menubar)
help_ = Menu(menubar)

# label will set the actual menu titles shown on the GUI
menubar.add_cascade(menu=file, label='File')
menubar.add_cascade(menu=edit, label='Edit')
menubar.add_cascade(menu=help_, label='Help')

file.add_command(label='New', command=lambda: print('New File'))
file.add_separator()        # Adds solid line between sections
file.add_command(label='Open...', command=lambda: print('Opening File...'))
file.add_command(label='Save', command=lambda: print('Saving File...'))

file.entryconfig('New', accelerator='Ctrl+N')   # accelerator will show the "shortcut" to do action
logo = PhotoImage(
    file='C:\\Users\\Student\\Documents\\8 Python\\tkinter_exercises\\tkinter_exercises\\Ex_Files_Python_Tkinter\\Exercise Files\Ch05\\python_logo.gif').subsample(
    10, 10)
file.entryconfig('Open...', image=logo, compound='left')    # Places image to left of text
file.entryconfig('Open...', state='disabled')   # Open... option will be disabled

file.delete('Save')     # Delete save option
save = Menu(file)   # Creating another menu within "File"
file.add_cascade(menu=save, label='Save')       # Creating a submenu with a tile of "Save"
save.add_command(label='Save As', command=lambda: print('Saving As...'))    # 2 options
save.add_command(label='Save All', command=lambda: print('Saving All...'))

choice = IntVar()

'''Radio button is button that presents options, where only ONE can be selected at a time
 (Name, variable associated w/ it, value that will be assigned to variable)'''
edit.add_radiobutton(label='One', variable=choice, value=1)
edit.add_radiobutton(label='Two', variable=choice, value=2)
edit.add_radiobutton(label='Three', variable=choice, value=3)

file.post(400, 300)     # Displays menu at specified location

root.mainloop()
