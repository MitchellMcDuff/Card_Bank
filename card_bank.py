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
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.gridLayout = QtGui.QGridLayout(self.page_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.initialVerticalLayout = QtGui.QVBoxLayout()
        self.initialVerticalLayout.setObjectName(_fromUtf8("initialVerticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.initialVerticalLayout.addItem(spacerItem)
        self.playButton = QtGui.QPushButton(self.page_2)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.initialVerticalLayout.addWidget(self.playButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.initialVerticalLayout.addItem(spacerItem1)
        self.lowerLevelGridLayout = QtGui.QGridLayout()
        self.lowerLevelGridLayout.setObjectName(_fromUtf8("lowerLevelGridLayout"))
        self.exitButton = QtGui.QPushButton(self.page_2)
        self.exitButton.setObjectName(_fromUtf8("exitButton"))
        self.lowerLevelGridLayout.addWidget(self.exitButton, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.lowerLevelGridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.initialVerticalLayout.addLayout(self.lowerLevelGridLayout)
        self.gridLayout.addLayout(self.initialVerticalLayout, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_1 = QtGui.QWidget()
        self.page_1.setObjectName(_fromUtf8("page_1"))
        self.gridLayout_3 = QtGui.QGridLayout(self.page_1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_3 = QtGui.QPushButton(self.page_1)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout_2.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.goBackButton = QtGui.QPushButton(self.page_1)
        self.goBackButton.setObjectName(_fromUtf8("goBackButton"))
        self.gridLayout_2.addWidget(self.goBackButton, 1, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 1, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.page_1)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_2.addWidget(self.progressBar, 2, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem4, 0, 2, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem5, 0, 0, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(self.page_1)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout_7.addWidget(self.textBrowser, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_7)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.pushButton = QtGui.QPushButton(self.page_1)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_8.addWidget(self.pushButton, 0, 2, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem6, 0, 1, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.page_1)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout_8.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_8, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_1)
        self.gridLayout_6.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.mainGridWidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.exitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.playButton.setText(_translate("MainWindow", "Play", None))
        self.exitButton.setText(_translate("MainWindow", "Exit", None))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton", None))
        self.goBackButton.setText(_translate("MainWindow", "Go Back", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

