from tkinter import *
from tkinter.ttk import *
from OfficBordel import *



root = Tk()
root.geometry('800x600')
root.title('Game')



mainScreen = Text(root, width = 70, heigh = 24, border = 5, bg = 'black', fg = 'white')
mainScreen.insert(END, 'Tady by bohl byt vypsanej text toho co se vzdycky deje, quest nebo nejakej takovej bordel.')
mainScreen.configure(state = DISABLED)
mainScreen.grid(row = 1, column = 1)

answerchoiceScreen = Text(root, width = 70, heigh = 9, border = 5, bg = 'black', fg = 'white')
answerchoiceScreen.insert(END, test)
answerchoiceScreen.configure(state = DISABLED)
answerchoiceScreen.grid(row = 2, column = 1)

mapScreen = Text(root, width = 29, heigh = 15, bg = 'black', fg = 'white',)
mapScreen.insert(END, 'Tady bude nejaka forma mapy')
mapScreen.configure(state = DISABLED)
mapScreen.place(x = 572, y = 0)

infoScreen = Text(root, width = 29, heigh = 20, bg = 'black', fg = 'white')
infoScreen.insert(END, 'Tady by mohl byt nejakej completni log [combat log atd.]')
infoScreen.configure(state = DISABLED)
infoScreen.place(x = 572, y = 244)

answerScreen = Entry(root, width = 94)
answerScreen.grid(row = 3, column = 1)






root.mainloop()