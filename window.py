import tkinter
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import JAFN_Game
import JAFN_Menu

UiStart, _ = uic.loadUiType("startmenu.ui")
UiDiff, _ = uic.loadUiType("difficultymenu.ui")


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__();
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.startMenu()
        self.difficultyMenu()
        self.setCentralWidget(self.stacked_widget)
        self.resize(2000,1000)

    def startMenu(self):
        self.startMenu = QtWidgets.QMainWindow()
        UiStart().setupUi(self.startMenu)
        self.stacked_widget.addWidget(self.startMenu)
        self.startbutton = self.startMenu.findChild(QtWidgets.QPushButton, 'startbutton') # Find the button
        self.startbutton.clicked.connect(lambda : self.goto_page(self.difficultyMenu))
        self.exitbutton = self.startMenu.findChild(QtWidgets.QPushButton, 'exitbutton') # Find the button
        self.exitbutton.clicked.connect(lambda : self.goto_page(self.startMenu))

    def difficultyMenu(self):
        self.difficultyMenu = QtWidgets.QMainWindow()
        UiDiff().setupUi(self.difficultyMenu)
        self.stacked_widget.addWidget(self.difficultyMenu)
        self.easybutton = self.difficultyMenu.findChild(QtWidgets.QPushButton, 'easyMode') # Find the button
        self.easybutton.clicked.connect(lambda : JAFN_Game.runGame(40, 0))
        self.hardbutton = self.difficultyMenu.findChild(QtWidgets.QPushButton, 'hardMode') # Find the button
        self.hardbutton.clicked.connect(lambda : JAFN_Game.runGame(120, 0))
        self.backbutton = self.difficultyMenu.findChild(QtWidgets.QPushButton, 'backPress') # Find the button
        self.backbutton.clicked.connect(lambda : self.goto_page(self.startMenu))

    def goto_page(self, widget):
        index = self.stacked_widget.indexOf(widget)
        print(index, widget)
        if index >= 0:
            self.stacked_widget.setCurrentIndex(index)

    '''def startProcess(self):
        p = QProcess()
        p.start("python3", ['JAFN_Game.py'])'''

    '''def EasyMode(sc,Easy, Medium, Hard, Back,title,High_Score):
        title.forget()
        High_Score.forget()
        Easy.forget()
        Medium.forget()
        Hard.forget()
        Back.forget()
        import JAFN_Game
        JAFN_Game.runGame(40,sc)'''


    

#class StartMenuUi(QtWidgets.QMainWindow):
    '''def __init__(self):
        super(StartMenuUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('startmenu.ui', self) # Load the .ui file
        self.show() # Show the GUI

        self.startbutton = self.findChild(QtWidgets.QPushButton, 'startbutton') # Find the button
        self.startbutton.clicked.connect(self.printStartButtonPressed)

        self.exitbutton = self.findChild(QtWidgets.QPushButton, 'exitbutton') # Find the button
        self.exitbutton.clicked.connect(self.printExitButtonPressed)

        self.show()

    def printStartButtonPressed(self):
        app = QtWidgets.QApplication(sys.argv)
        window = DifficultyMenuUi()
        window.show()

    def printExitButtonPressed(self):
        print("exit button pressed")

    


class DifficultyMenuUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(DifficultyMenuUi, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('difficultymenu.ui', self) # Load the .ui file
        self.show() # Show the GUI'''


app = QtWidgets.QApplication(sys.argv) 
window = Ui()
window.show()
app.exec()

