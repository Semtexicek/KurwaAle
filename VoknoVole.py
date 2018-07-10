from tkinter import *
from tkinter.ttk import *
import vvdeff as deff

def Save():
    quest = (qinfo.get(1.0, END))
    Savedic = {}
    Savedic['Asd'] = quest
    print(Save)

def Neco(self):
    if var.get() == 'Test':
        print('a')
    elif var.get() == 'Test1':
        print('b')
    elif var.get() == 'Test2':
        print('c')

def wgtadd():
    cbox.add['values'] = 'ValuesTest1'

root = Tk()
root.title('Asd')
root.geometry('800x600')


var = StringVar()
cbox = Combobox(root, textvariable = var)
cbox['values'] = 
cbox.current(0)
cbox.bind('<<ComboboxSelected>>', Neco)
cbox.grid(row = 1, column = 1)

labelQname = Label(root, text = 'Name of quest')
labelQname.grid(row = 2, column = 1)
labelQinfo = Label(root, text = 'Info about quest')
labelQinfo.grid(row = 3, column = 1)


qname = Entry(root)
qname.grid(row = 2, column = 2)
qinfo = Text(root, height=20, width=50)
qinfo.grid(row = 3, column = 2)

EnterButton = Button(root, text = 'Save', command = Save)
EnterButton.grid(row = 4, column = 1)

widgetadd = Entry(root)
widgetadd.grid(row = 6, column = 1)
EnterButton = Button(root, text = 'Menu add', command = wgtadd)
EnterButton.grid(row = 6, column = 2)


root.mainloop()