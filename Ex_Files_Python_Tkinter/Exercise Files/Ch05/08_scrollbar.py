#!/usr/bin/python3
# scrollbar.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

root = Tk()

canvas = Canvas(root, scrollregion=(0, 0, 640, 480), bg='white')
xscroll = ttk.Scrollbar(root, orient=HORIZONTAL, command=canvas.xview)

# Vertical scrollbar, yview tells scrollbar how much it has been moved so it can adjust its view accordingly
yscroll = ttk.Scrollbar(root, orient=VERTICAL, command=canvas.yview)

# Makes it so scroll-pad can correctly track where in text you are percentage-wise
canvas.config(xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

canvas.grid(row=1, column=0)    # Place canvas
xscroll.grid(row=2, column=0, sticky='ew')  # Place x scroll bar
yscroll.grid(row=1, column=1, sticky='ns')  # Add to text box

# Places green oval on the canvas with each mouse click
def canvas_click(event):
    # Canvas x will notifies to Tk that the screen has been scrolled so it knows to place dot in
    # location off of original screen
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    canvas.create_oval((x - 5, y - 5, x + 5, y + 5), fill='green')

canvas.bind('<1>', canvas_click)    # After click, will execute canvas_click method

root.mainloop()
