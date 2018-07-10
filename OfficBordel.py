from tkinter import *
from tkinter.ttk import *
from Offic2 import *

        
    
class mainFrame():
    def __init__(self):
        self.root = Tk()
        self.root.title('Offic2')
        self.root.geometry('800x600')
            
        mainScreen = Text(self.root, width = 70, heigh = 24, border = 5, bg = 'black', fg = 'white')
        mainScreen.insert(END, 'Tady by bohl byt vypsanej text toho co se vzdycky deje, quest nebo nejakej takovej bordel.')
        mainScreen.configure(state = DISABLED)
        mainScreen.place(x = 0, y = 0)

        answerchoiceScreen = Text(self.root, width = 70, heigh = 9, border = 5, bg = 'black', fg = 'white')
        answerchoiceScreen.insert(END, 'Answer Window')
        answerchoiceScreen.configure(state = DISABLED)
        answerchoiceScreen.place(x = 0, y = 393)

        mapScreen = Text(self.root, width = 29, heigh = 15, bg = 'black', fg = 'white',)
        mapScreen.insert(END, 'Tady bude nejaka forma mapy')
        mapScreen.configure(state = DISABLED)
        mapScreen.place(x = 572, y = 0)

