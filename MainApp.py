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
        self.playButton.clicked.connect(self.playButtonClick)

    def playButtonClick(self):
        print "clicked"
        self.stackedWidget.setCurrentIndex(1)

        
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    window1 = MainMenu()
    window1.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
