#!/usr/bin/python3
# template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

# Treeview
from tkinter import *
from tkinter import ttk

root = Tk()

treeview = ttk.Treeview(root)
treeview.pack()

# Each item represents a node in the tree
treeview.insert('', '0', 'item1', text='First Item')  # (parent, index, item_id, text property)
treeview.insert('', '1', 'item2', text='Second Item')
treeview.insert('', 'end', 'item3', text='Third Item')

logo = PhotoImage(
    file='C:\\Users\\barron\\Dropbox\\Lynda Courses\\Python GUI Development with                        Tkinter\\Exercise Files - Current\\03 Widget Classes\\python_logo.gif'
    ).subsample(10, 10)

treeview.insert('item2', 'end', 'python', text='Python', image=logo)    # Subitem under item2

treeview.config(height=5)       # Resizes treeview so it only has room to show 5 items
treeview.move('item2', 'item1', 'end')      # (item, new parent you want to move to, index)

# Defaults items to be open
treeview.item('item1', open=True)
treeview.item('item2', open=True)
print(treeview.item('item1', 'open'))       # Checks status of open property

treeview.detach('item3')        # Detach item from treeview
treeview.move('item3', 'item2', '0')    # Move to new location
treeview.delete('item3')        # Completely deletes item (Destroyed)

treeview.configure(column=('version'))
treeview.column('version', width=50, anchor='center')
treeview.column('version', width=50, anchor='center')
treeview.column('#0', width=150)
treeview.heading('version', text='Version')
treeview.set('python', 'version', '3.4')
treeview.item('python', tags=('software'))
treeview.tag_configure('software', background='yellow')


def callback(event):
    print(treeview.selection())


treeview.bind('<<TreeviewSelect>>', callback)

treeview.config(selectmode='browse')
print(treeview.selection_add('python'))
print(treeview.selection_remove('python'))
print(treeview.selection_toggle('python'))

root.mainloop()
