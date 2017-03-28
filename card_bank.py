# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'card_bank.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.mainGridWidget = QtGui.QWidget(MainWindow)
        self.mainGridWidget.setObjectName(_fromUtf8("mainGridWidget"))
        self.gridLayout_6 = QtGui.QGridLayout(self.mainGridWidget)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.stackedWidget = QtGui.QStackedWidget(self.mainGridWidget)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.mainmenu = QtGui.QWidget()
        self.mainmenu.setObjectName(_fromUtf8("mainmenu"))
        self.gridLayout = QtGui.QGridLayout(self.mainmenu)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.initialVerticalLayout = QtGui.QVBoxLayout()
        self.initialVerticalLayout.setObjectName(_fromUtf8("initialVerticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.initialVerticalLayout.addItem(spacerItem)
        self.playButton = QtGui.QPushButton(self.mainmenu)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.initialVerticalLayout.addWidget(self.playButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.initialVerticalLayout.addItem(spacerItem1)
        self.lowerLevelGridLayout = QtGui.QGridLayout()
        self.lowerLevelGridLayout.setObjectName(_fromUtf8("lowerLevelGridLayout"))
        self.exit1Button = QtGui.QPushButton(self.mainmenu)
        self.exit1Button.setObjectName(_fromUtf8("exit1Button"))
        self.lowerLevelGridLayout.addWidget(self.exit1Button, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.lowerLevelGridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.initialVerticalLayout.addLayout(self.lowerLevelGridLayout)
        self.gridLayout.addLayout(self.initialVerticalLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.mainmenu)
        self.playgame = QtGui.QWidget()
        self.playgame.setObjectName(_fromUtf8("playgame"))
        self.gridLayout_3 = QtGui.QGridLayout(self.playgame)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.botButtonsGridLayout = QtGui.QGridLayout()
        self.botButtonsGridLayout.setObjectName(_fromUtf8("botButtonsGridLayout"))
        self.startOverButton = QtGui.QPushButton(self.playgame)
        self.startOverButton.setObjectName(_fromUtf8("startOverButton"))
        self.botButtonsGridLayout.addWidget(self.startOverButton, 2, 0, 1, 1)
        self.goBackButton = QtGui.QPushButton(self.playgame)
        self.goBackButton.setObjectName(_fromUtf8("goBackButton"))
        self.botButtonsGridLayout.addWidget(self.goBackButton, 1, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.botButtonsGridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.playgame)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.botButtonsGridLayout.addWidget(self.progressBar, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.botButtonsGridLayout)
        self.topButtonsGridLayout = QtGui.QGridLayout()
        self.topButtonsGridLayout.setObjectName(_fromUtf8("topButtonsGridLayout"))
        self.textBrowser = QtGui.QTextBrowser(self.playgame)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.topButtonsGridLayout.addWidget(self.textBrowser, 0, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.topButtonsGridLayout.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.topButtonsGridLayout.addItem(spacerItem5, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.topButtonsGridLayout)
        self.playGameGridLayout = QtGui.QGridLayout()
        self.playGameGridLayout.setObjectName(_fromUtf8("playGameGridLayout"))
        self.nextButton = QtGui.QPushButton(self.playgame)
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.playGameGridLayout.addWidget(self.nextButton, 0, 2, 1, 1)
        self.exit2Button = QtGui.QPushButton(self.playgame)
        self.exit2Button.setObjectName(_fromUtf8("exit2Button"))
        self.playGameGridLayout.addWidget(self.exit2Button, 0, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.playGameGridLayout.addItem(spacerItem6, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.playGameGridLayout)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.playgame)
        self.gridLayout_6.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.mainGridWidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.exit1Button, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.exit2Button, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.playButton.setText(_translate("MainWindow", "Play", None))
        self.exit1Button.setText(_translate("MainWindow", "Exit", None))
        self.startOverButton.setText(_translate("MainWindow", "Start OVer", None))
        self.goBackButton.setText(_translate("MainWindow", "Go Back", None))
        self.nextButton.setText(_translate("MainWindow", "Next", None))
        self.exit2Button.setText(_translate("MainWindow", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

