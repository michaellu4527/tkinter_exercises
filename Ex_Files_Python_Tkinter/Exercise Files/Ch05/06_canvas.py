#!/usr/bin/python3
# canvas.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

root = Tk()

# Creating a canvas
canvas = Canvas(root)
canvas.pack()
canvas.config(width=640, height=480)    # Configuring size

# (xStart, yStart, xEnd, yEnd, color of line, width of line)
line = canvas.create_line(160, 360, 480, 120, fill='blue', width=5)
canvas.itemconfigure(line, fill='green')    # Change color
print(canvas.coords(line))      # Coordinates of line

# 2 lines here. One using the 1st and 2nd pair of coordinates. Second using 2nd and 3rd pair
canvas.coords(line, 0, 0, 320, 240, 640, 0)     # Change coordinates of line

canvas.itemconfigure(line, smooth=True)
canvas.itemconfigure(line, splinesteps=5)       # Uses 5 lines to make curve
canvas.itemconfigure(line, splinesteps=10000)     # Use 100
canvas.delete(line)     # Deletes object
canvas.delete(all)      # Completely clears canvas


rect = canvas.create_rectangle(160, 120, 480, 360)  # x,y coord pairs for opposite corners of rect.
canvas.itemconfigure(rect, fill='yellow')
oval = canvas.create_oval(160, 120, 480, 360)  # Bounding corners of oval
arc = canvas.create_arc(160, 1, 480, 240)   # Create arc of 90 degrees within specified bounds
canvas.itemconfigure(arc, start=0, extent=180, fill='green')    # Green arc of 180 degrees
poly = canvas.create_polygon(160, 360, 320, 480, 480, 360, fill='blue') # Creates triangle

# Displays text image center at specified coordinates
text = canvas.create_text(320, 240, text='Python', font=('Courier', 32, 'bold'))

logo = PhotoImage(file='python_logo.gif')  # Change path as needed
image = canvas.create_image(320, 240, image=logo)   # Coord. represents center of image


canvas.lift(text)   # Moves text into foreground
canvas.lower(image)     # Moves text all the way into background
canvas.lower(image, text)   # Lowers image into position just below specified in second argument

button = Button(canvas, text='Click Me')
canvas.create_window(320, 60, window=button)    # Creates button in specified location

canvas.itemconfigure(rect, tags=('shape'))  # Tag is similar to "class" in HTML
canvas.itemconfigure(oval, tags=('shape', 'round'))
canvas.itemconfigure('shape', fill='grey')  # Will change anything with tag "shape" to grey background
print(canvas.gettags(oval))     # Returns the tags associated with oval object

root.mainloop()
