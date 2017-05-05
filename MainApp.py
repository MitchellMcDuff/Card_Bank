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
from random import randint #for drawing random cards

class MainMenu(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.setupUi(self)

        #set up buttons
        self.playButton.clicked.connect(self.playGameButtonClick)
        self.goBackButton.clicked.connect(self.goBackToMainMenuButtonClick)
        self.goBack2Button.clicked.connect(self.goBackToMainMenu2ButtonClick)
        self.editChosenPlaylistButton.clicked.connect(self.editCardsMenuButtonClick)
        self.addPlayerButton.clicked.connect(self.addPlayer)
        self.addCardButton.clicked.connect(self.addCard)
        self.removeCardButton.clicked.connect(self.removeCard)
        self.nextButton.clicked.connect(self.nextCard)
        self.skipButton.clicked.connect(self.skipCard)
        self.startOverButton.clicked.connect(self.startOver)
        self.startButton.clicked.connect(self.startButtonClicked)
        self.removePlayerButton.clicked.connect(self.removePlayer)
        self.addPlaylistButton.clicked.connect(self.addPlaylist)
        self.chooseSelectedPlaylistButton.clicked.connect(self.choosePlaylist)
        self.saveEditsButton.clicked.connect(self.savePlaylist)
        self.removeSelectedPlaylistButton.clicked.connect(self.removePlaylist)

    	#reads each line of playlist.txt into a list which populates the cards
        self.loadListOfPlaylists()
    	self.chosenPlaylistLabel.setText(self.playlistListWidget.item(0).text())
        text_file = open(self.chosenPlaylistLabel.text() + ".txt", "r")
    	self.cards = text_file.readlines()
    	text_file.close()
    	self.updateCardTable()
    	self.playingCards = []
    	for item in self.cards:
    		self.playingCards.append(item)
    	self.totalCards = len(self.cards)
    	self.cardsPlayed = 0.0
    	self.skipCard() #draw first card
        self.cardsEdited = False

#these functions change the current layout
    def startButtonClicked(self):
        self.warningLabel.clear()
        self.stackedWidget.setCurrentIndex(0)

    def editCardsMenuButtonClick(self):
        self.warningLabel.clear()
        self.stackedWidget.setCurrentIndex(2)

    def playGameButtonClick(self):
        self.warningLabel.clear()
        #if play is pressed and there are no players this will add default players
        if (self.playerListWidget.count() == 0):
            listItem = QtGui.QListWidgetItem("Player 1")
            tableItem = QtGui.QTableWidgetItem("Player 1")
            self.playerListWidget.addItem(listItem)
            self.scoreBoardTableWidget.insertRow(self.scoreBoardTableWidget.rowCount())
            self.scoreBoardTableWidget.setItem(self.scoreBoardTableWidget.rowCount()-1, 0, tableItem)
            self.scoreBoardTableWidget.setItem(self.scoreBoardTableWidget.rowCount()-1, 1, QtGui.QTableWidgetItem("0"))

            listItem = QtGui.QListWidgetItem("Player 2")
            tableItem = QtGui.QTableWidgetItem("Player 2")
            self.playerListWidget.addItem(listItem)
            self.scoreBoardTableWidget.insertRow(self.scoreBoardTableWidget.rowCount())
            self.scoreBoardTableWidget.setItem(self.scoreBoardTableWidget.rowCount()-1, 0, tableItem)
            self.scoreBoardTableWidget.setItem(self.scoreBoardTableWidget.rowCount()-1, 1, QtGui.QTableWidgetItem("0"))
        self.startOver()
        self.stackedWidget.setCurrentIndex(1)

    def goBackToMainMenuButtonClick(self):
        self.warningLabel.clear()
        self.stackedWidget.setCurrentIndex(0)

    def goBackToMainMenu2ButtonClick(self):
        self.warningLabel.clear()
        self.stackedWidget.setCurrentIndex(0)
        self.loadPlaylist()

#these functions update the player list
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
        self.warningLabel.clear()

    def removePlayer(self):
        self.warningLabel.clear()
        rowCount = self.scoreBoardTableWidget.rowCount()
        rowNum = 0
        #get selected player widget
        for listItem in self.playerListWidget.selectedItems():
            self.playerListWidget.takeItem(self.playerListWidget.row(listItem))
            for row in xrange(0,rowCount):
                if (self.scoreBoardTableWidget.item(row,0).text() == listItem.text()):
                    rowNum = row
            self.scoreBoardTableWidget.removeRow(rowNum)

#these functions update the card table and playlist
    #this needs to populate the card table with the items from the currently selected playlist
    def updateCardTable(self):
        self.warningLabel.clear()
        #print "This needs to populate the card table with the items from the currently selected playlist"
        for i in reversed(range(self.cardTableWidget.rowCount())):
            self.cardTableWidget.removeRow(i)
    	#fill cardTableWidget with cards
    	for line in self.cards:
            tableItem = QtGui.QTableWidgetItem(line)
            self.cardTableWidget.insertRow(self.cardTableWidget.rowCount())
            self.cardTableWidget.setItem(self.cardTableWidget.rowCount()-1, 0, tableItem)

    def cleanCardTable(self):
        self.warningLabel.clear()
        #print "This needs to remove all rows that have empty card names"
        for i in reversed(range(self.cardTableWidget.rowCount())):
            if self.cardTableWidget.item(i,0) is None:
                self.cardTableWidget.removeRow(i)

    def addCard(self):
        self.warningLabel.clear()
        self.cardTableWidget.insertRow(self.cardTableWidget.rowCount())
        self.totalCards = self.totalCards + 1
        self.cardsEdited = True

    def removeCard(self):
        self.warningLabel.clear()
        #print "remove the selected card"
    	#gets selected row
    	rows = sorted(set(index.row() for index in self.cardTableWidget.selectedIndexes()))

    	#gets score from row and increases by 1
    	for row in reversed(rows):
            self.cards.pop(row)
            self.playingCards.pop(row)
            self.cardTableWidget.removeRow(row)
        self.cardsEdited = True

    def addPlaylist(self):
        self.warningLabel.clear()
        #if there is an letter add the playlist to the list
        if any(letter.isalpha() for letter in str(self.playlistNameLineEdit.text())):
            listItem = QtGui.QListWidgetItem(self.playlistNameLineEdit.text())
            #check if playlist already exists

            #insert in list
            self.playlistListWidget.addItem(listItem)
            text_file = open(listItem.text() + ".txt", "w")
            #text_file.write();
            text_file.close()
            self.writePlaylists()
            self.warningLabel.setText("Playlist " + listItem.text() + " added.")
        else:
            self.warningLabel.setText("Please enter a name for your playlist.")

        self.playlistNameLineEdit.clear()

    def choosePlaylist(self):
        self.warningLabel.clear()
        for listItem in self.playlistListWidget.selectedItems():
            self.chosenPlaylistLabel.setText(listItem.text())
        self.warningLabel.setText("Playlist " + self.chosenPlaylistLabel.text() + " chosen.")
        self.loadPlaylist()

    def savePlaylist(self):
        self.warningLabel.clear()
        text_file = open(self.chosenPlaylistLabel.text() + ".txt", "w")
        text_file.seek(0)
        self.cleanCardTable()
        for i in range(self.cardTableWidget.rowCount()):
            line = self.cardTableWidget.item(i,0).text()
            text_file.write(str(self.cardTableWidget.item(i,0).text()).rstrip() + "\n")
        text_file.truncate()
        text_file.close()
        #self.loadPlaylist()
        self.warningLabel.setText("Changes saved to playlist.")

    def removePlaylist(self):
        self.warningLabel.clear()
        if self.playlistListWidget.count() != 1:
            for listItem in self.playlistListWidget.selectedItems():
                self.playlistListWidget.takeItem(self.playlistListWidget.row(listItem))
            self.writePlaylists()
        else:
            self.warningLabel.setText("The last playlist cannot be deleted.")

    def loadListOfPlaylists(self):
        text_file = open("listOfPlaylists.txt", "r")
    	self.playlists = text_file.read().splitlines()
    	text_file.close()
    	for item in self.playlists:
            listItem = QtGui.QListWidgetItem(item)
            self.playlistListWidget.addItem(listItem)
        #self.chosenPlaylistLabel.setText(listItem.text())

    def writePlaylists(self):
        text_file = open("listOfPlaylists.txt", "w")
        for i in range(self.playlistListWidget.count()):
            text_file.write(self.playlistListWidget.item(i).text() + "\n")
        text_file.close()

    def loadPlaylist(self):
        text_file = open(self.chosenPlaylistLabel.text() + ".txt", "r")
        del self.cards[:]
    	self.cards = text_file.read().splitlines()
        for item in self.cards:
            item.rstrip()
    	text_file.close()
    	self.updateCardTable()
        self.cardsPlayed = 0.0
        self.totalCards = len(self.cards)
        self.playingCards = []
        for item in self.cards:
        	self.playingCards.append(item)

#these functions are the main gameplay functions
    #this will display the next card ONLY if a player has been selected
    def nextCard(self):
        self.warningLabel.clear()
        #print "display next card and giving a point to someone also updates the progress bar"
    	#gets selected row
    	rows = sorted(set(index.row() for index in
        self.scoreBoardTableWidget.selectedIndexes()))

        self.warningLabel.setText("Please select the winning player before advancing to next card.")


    	#gets score from row and increases by 1
	for row in rows:
		s = int(self.scoreBoardTableWidget.item(row,1).text()) + 1
		score = str(s)
		self.scoreBoardTableWidget.setItem(row, 1, QtGui.QTableWidgetItem(score))
		self.skipCard()

    def skipCard(self):
        self.warningLabel.clear()
        #print "displays next card without giving points also updates the progress bar"
	if self.cardsPlayed < self.totalCards:
		self.cardsPlayed = self.cardsPlayed + 1.0
		self.progressBar.setProperty("value", self.cardsPlayed/self.totalCards*100)
		randNum = randint(0,len(self.playingCards) - 1)
		cardText = self.playingCards[randNum]
		self.playingCards.pop(randNum)
		self.textBrowser.setText(cardText)
	else:
		self.textBrowser.setText("You've played all cards.\n\nGAME OVER")

    def startOver(self):
        #print "will start the game over and reset all scores to 0 also updates the progress bar"
    	#for i in reversed(range(self.cardTableWidget.rowCount())):
        		#self.cardTableWidget.removeRow(i)
    	#self.updateCardTable()
        self.stackedWidget.setCurrentIndex(1)
        for i in reversed(range(self.scoreBoardTableWidget.rowCount())):
            self.scoreBoardTableWidget.setItem(i, 1, QtGui.QTableWidgetItem("0"))
    	self.progressBar.setProperty("value", 0)
    	self.cardsPlayed = 0.0
        self.totalCards = len(self.cards)
        self.playingCards = []
        for item in self.cards:
        	self.playingCards.append(item)
        self.skipCard()


def main():
    app = QtGui.QApplication(sys.argv)
    window1 = MainMenu()
    window1.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
