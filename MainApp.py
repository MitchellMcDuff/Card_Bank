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
        self.goBack2Button.clicked.connect(self.goBackToMainMenu2ButtonClick)
        self.editCardsButton.clicked.connect(self.editCardsMenuButtonClick)
        self.addPlayerButton.clicked.connect(self.addPlayer)
        self.addCardButton.clicked.connect(self.addCard)
        self.removeCardButton.clicked.connect(self.removeCard)
        self.nextButton.clicked.connect(self.nextCard)
        self.skipButton.clicked.connect(self.skipCard)
        self.startOverButton.clicked.connect(self.startOver)
        #self.removePlayerButton.clicked.connect(self.removePlayer)


    def editCardsMenuButtonClick(self):
        self.stackedWidget.setCurrentIndex(2)
        self.updateCardTable()
        
    def playGameButtonClick(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def goBackToMainMenuButtonClick(self):
        self.stackedWidget.setCurrentIndex(0)

    def goBackToMainMenu2ButtonClick(self):
        self.stackedWidget.setCurrentIndex(0)
        self.cleanCardTable()
    
    #this needs to populate the card table with the items from the currently selected playlist
    def updateCardTable(self):
        print "This needs to populate the card table with the items from the currently selected playlist"

    def cleanCardTable(self):
        print "This needs to remove all rows that have empty card names"
        
    def addPlayer(self):
        #if there is an letter add the player to the list
        if any(letter.isalpha() for letter in str(self.playerNameLineEdit.text())):
            listItem = QtGui.QListWidgetItem(self.playerNameLineEdit.text())
            tableItem = QtGui.QTableWidgetItem(self.playerNameLineEdit.text())
            #check if player already exists
            
            #insert in list
            self.playerListWidget.addItem(listItem)
            #insert in score board
            self.scoreBoardTableWidget.insertRow(self.scoreBoardTableWidget.rowCount())
            self.scoreBoardTableWidget.setItem(self.scoreBoardTableWidget.rowCount()-1, 0, tableItem)
            self.scoreBoardTableWidget.setItem(self.scoreBoardTableWidget.rowCount()-1, 1, QtGui.QTableWidgetItem("0"))
        self.playerNameLineEdit.clear()

    
    def addCard(self):
        self.cardTableWidget.insertRow(self.cardTableWidget.rowCount())
        
    def removeCard(self):
        print "remove the selected card"
    
    #this will display the next card ONLY if a player has been selected
    def nextCard(self):
        print "display next card and giving a point to someone also updates the progress bar"
    
    def skipCard(self):
        print "displays next card without giving points also updates the progress bar"
    
    def startOver(self):
        print "will start the game over and reset all scores to 0 also updates the progress bar"
    
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