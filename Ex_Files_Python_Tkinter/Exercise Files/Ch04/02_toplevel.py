#!/usr/bin/python3
# toplevel.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *      
    
root = Tk()

window = Toplevel(root) # New top level window which is a child of the "root" window
window.title('New Window')  # Change title of new window

window.lower()  # Moves to the back of any other windows currently displayed
window.lift(root)   # Moves it above the root window

#Default state is "normal"
window.state('zoomed')  # Maximizes window
window.state('withdrawn')   # Hides window
window.state('iconic')  # Minimizes window
window.state('normal')  # Default state
print(window.state())   # View current state of video
window.state('normal')

window.iconify()    # Minimizes window
window.deiconify()  # Unminimizes window

window.geometry('640x480+50+100')   # window.geometry('WIDTHxHEIGHT+X+Y')
print(window.geometry())
window.resizable(False, False)  # Can no longer resize the window in x or y direction
window.maxsize(640, 480)    # Maximum size of video
window.minsize(200, 200)    # Min size
window.resizable(True, True)    # Resizable again

root.destroy()  # Will destroy the current window and all childs.

root.mainloop()
