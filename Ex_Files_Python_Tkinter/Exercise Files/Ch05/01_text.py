#!/usr/bin/python3
# text.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *

root = Tk()

text = Text(root, width=40, height=10)      # Set size of text box, text will wrap
text.pack()
text.config(wrap='word')        # Change so text will wrap at the nearest space

print(text.get('1.0', 'end'))       # Returns entire text box from start to end
print(text.get('1.0', '1.end'))     # Returns first "logical" line
text.insert('1.0 + 2 lines', 'Inserted message')        # Inserts text down 2 logical lines

# START inserted text at the end of 2 lines down
text.insert('1.0 + 2 lines lineend', ' and\nmore and\nmore.')

text.delete('1.0')      # Deletes character at index number
text.delete('1.0', '1.0 lineend')       # Deletes up until end of 1st line (but excluding end)
text.delete('1.0', '3.0 lineend + 1 chars')     # Deletes 1st 3 lines and includes \n character

# Replaces w/ new text in specified range
text.replace('1.0', '1.0 lineend', 'This is the first line.')

text.config(state='disabled')       # Disables text field
text.delete('1.0', 'end')       # Doesn't work since text field is disabled
text.config(state='normal')     # Get rid of disabled state

text.tag_add('my_tag', '1.0', '1.0 wordend')    # tag_add(name, start, end)

# Options include background, font, foreground, justify, wrap, strike-through, etc.
text.tag_configure('my_tag', background='yellow')

text.tag_remove('my_tag', '1.1', '1.3')     # (name, start (NON inclusive), end (NON inclusive))
print(text.tag_ranges('my_tag'))    # Returns range of what specified tag covers
print(text.tag_names())     # Shows tags
print(text.tag_names('1.0'))     # Shows tags that cover that index

text.replace('my_tag.first', 'my_tag.last', 'That was')     # (start, end, replaced text)
text.tag_delete('my_tag')       # Deletes tags

text.mark_names()       # List of marks
text.insert('insert', '_')      # Inserts mark in front of where cursor is in text box
text.mark_set('my_mark', 'end')     # Add mark in specified location (name, location)
text.mark_gravity('my_mark', 'right')       # Will stick to right when placed in between characters
text.mark_unset('my_mark')      # Removes mark

image = PhotoImage(file='python_logo.gif')  # Change path as needed
text.image_create('insert', image=image)    # References "insert" mark
text.image_create('insert', image=image)

button = Button(text, text='Click Me')
text.window_create('insert', window=button)

root.mainloop()
