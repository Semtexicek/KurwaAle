from tkinter import *
from tkinter.ttk import *


class mainFrame():
    def __init__(self):
        self.root = Tk()
        self.root.title('Offic2')
        self.root.geometry('800x600')


        self.menubar = Menu(self.root)
        filemenu = Menu(self.menubar, tearoff = 0)
        filemenu.add_command(label="New")
        filemenu.add_command(label = "Open")
        filemenu.add_command(label = "Save")
        filemenu.add_command(label = "Save as...")
        filemenu.add_command(label = "Close")
        filemenu.add_separator()
        filemenu.add_command(label = "Exit")
        self.menubar.add_cascade(label = "File")

        mainScreen = Text(self.root, wrap = WORD, width = 70, heigh = 24, border = 2, bg = 'black', fg = 'white')
        mainScreen.insert(END, 'Tady by bohl byt vypsanej text toho co se vzdycky deje, quest nebo nejakej takovej bordel.')
        mainScreen.configure(state = DISABLED)
        mainScreen.place(x = 0, y = 20)

        answerchoiceScreen = Text(self.root, wrap = WORD, width = 70, heigh = 10, border = 2, bg = 'black', fg = 'white')
        answerchoiceScreen.insert(END, 'Answer Window')
        answerchoiceScreen.configure(state = DISABLED)
        answerchoiceScreen.place(x = 0, y = 390)

        answerScreen = Entry(self.root, width = 94)
        answerScreen.place(x = 0, y = 578)

        mapScreen = Text(self.root, wrap = WORD, width = 29, heigh = 15, border = 2, bg = 'black', fg = 'white',)
        mapScreen.insert(END, 'Tady bude nejaka forma mapy')
        mapScreen.configure(state = DISABLED)
        mapScreen.place(x = 572, y = 20)

        infoScreen = Text(self.root, wrap = WORD, width = 29, border = 2, heigh = 20, bg = 'black', fg = 'white')
        infoScreen.insert(END, 'Tady by mohl byt nejakej completni log [combat log atd.]')
        infoScreen.configure(state = DISABLED)
        infoScreen.place(x = 572, y = 244)



mainFrame()


mainloop()