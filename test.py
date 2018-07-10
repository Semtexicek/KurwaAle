from tkinter import *
from tkinter.ttk import *

def Test():
    print('Test Definice')

def Neco(self):
    if var.get() == 'Test':
        print('a')
    elif var.get() == 'Test1':
        print('b')
    elif var.get() == 'Test2':
        print('c')
   

var = StringVar()

cbox = Combobox(root, textvariable = var)
cbox['values'] = 'Test', 'Test1', 'Test2'
cbox.current(0)
cbox.bind('<<ComboboxSelected>>', Neco)
cbox.grid(row = 0, column = 0)
