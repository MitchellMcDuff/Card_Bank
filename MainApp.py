# This is the main file that will set all the functions for the Uis
# 
# How to compile the ui into python code: 
#       pyuic4 -x play_game.ui -o play_game.py
#       pyuic4 -x card_bank.ui -o card_bank.py
#       DO NOT EDIT THESE OUTPUTS BUT YOU CAN LOOK AT THEM
#



import sys
from PyQt4 import QtCore, QtGui
from card_bank import Ui_MainWindow

class MainMenu(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.setupUi(self)
        
        #set up buttons
        self.playButton.clicked.connect(self.playGameButtonClick)
        self.goBackButton.clicked.connect(self.goBackToMainMenuButtonClick)
        self.goBack2Button.clicked.connect(self.goBackToMainMenuButtonClick)
        self.editCardsButton.clicked.connect(self.editCardsMenuButtonClick)
        self.addPlayerButton.clicked.connect(self.addPlayer)
        
        #self.removePlayerButton.clicked.connect(self.removePlayer)


    def editCardsMenuButtonClick(self):
        self.stackedWidget.setCurrentIndex(2)
        
    def playGameButtonClick(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def goBackToMainMenuButtonClick(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def addPlayer(self):
        #if there is an letter add the player to the list
        if any(letter.isalpha() for letter in str(self.playerNameLineEdit.text())):
            listItem = QtGui.QListWidgetItem(self.playerNameLineEdit.text())
            tableItem = QtGui.QTableWidgetItem(self.playerNameLineEdit.text())
            self.playerNameLineEdit.clear()
            #check if player already exists
            
            #insert in list
            self.playerListWidget.addItem(listItem)
            #insert in score board
            self.scoreBoardTableWidget.insertRow(self.scoreBoardTableWidget.rowCount())
            self.scoreBoardTableWidget.setItem(self.scoreBoardTableWidget.rowCount()-1, 0, tableItem)
            self.scoreBoardTableWidget.setItem(self.scoreBoardTableWidget.rowCount()-1, 1, QtGui.QTableWidgetItem("0"))
            
    
    #def removePlayer(self):
        #for item in self.playerListWidget.selectedItems():
            #self.playerListWidget.takeItem(self.playerListWidget.row(item))
        #for item in self.scoreBoardTableWidget.
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    window1 = MainMenu()
    window1.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()