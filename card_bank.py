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
        self.initialVerticalLayout = QtGui.QVBoxLayout()
        self.initialVerticalLayout.setObjectName(_fromUtf8("initialVerticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.initialVerticalLayout.addItem(spacerItem)
        self.playButton = QtGui.QPushButton(self.mainGridWidget)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.initialVerticalLayout.addWidget(self.playButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.initialVerticalLayout.addItem(spacerItem1)
        self.lowerLevelGridLayout = QtGui.QGridLayout()
        self.lowerLevelGridLayout.setObjectName(_fromUtf8("lowerLevelGridLayout"))
        self.exitButton = QtGui.QPushButton(self.mainGridWidget)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.lowerLevelGridLayout.addWidget(self.exitButton, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.lowerLevelGridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.initialVerticalLayout.addLayout(self.lowerLevelGridLayout)
        self.gridLayout_6.addLayout(self.initialVerticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.mainGridWidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.exitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.playButton.setText(_translate("MainWindow", "Play", None))
        self.exitButton.setText(_translate("MainWindow", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

