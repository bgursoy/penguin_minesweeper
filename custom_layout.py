# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'custom_layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CustomWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 314)
        MainWindow.setMinimumSize(QtCore.QSize(350, 314))
        MainWindow.setMaximumSize(QtCore.QSize(350, 314))
        MainWindow.setStyleSheet("background-color: #181830")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.widthHorizontalLayout = QtWidgets.QHBoxLayout()
        self.widthHorizontalLayout.setObjectName("widthHorizontalLayout")
        self.widthLabel = QtWidgets.QLabel(self.centralwidget)
        self.widthLabel.setStyleSheet("color: white")
        self.widthLabel.setObjectName("widthLabel")
        self.widthHorizontalLayout.addWidget(self.widthLabel)
        self.widthNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.widthNumber.setStyleSheet("color: white")
        self.widthNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.widthNumber.setProperty("intValue", 8)
        self.widthNumber.setObjectName("widthNumber")
        self.widthHorizontalLayout.addWidget(self.widthNumber)
        self.widthPlusButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widthPlusButton.sizePolicy().hasHeightForWidth())
        self.widthPlusButton.setSizePolicy(sizePolicy)
        self.widthPlusButton.setMaximumSize(QtCore.QSize(40, 30))
        self.widthPlusButton.setStyleSheet("color: white")
        self.widthPlusButton.setObjectName("widthPlusButton")
        self.widthHorizontalLayout.addWidget(self.widthPlusButton)
        self.widthMinusButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widthMinusButton.sizePolicy().hasHeightForWidth())
        self.widthMinusButton.setSizePolicy(sizePolicy)
        self.widthMinusButton.setMaximumSize(QtCore.QSize(40, 30))
        self.widthMinusButton.setStyleSheet("color: white")
        self.widthMinusButton.setObjectName("widthMinusButton")
        self.widthHorizontalLayout.addWidget(self.widthMinusButton)
        self.widthHorizontalLayout.setStretch(0, 2)
        self.widthHorizontalLayout.setStretch(1, 1)
        self.gridLayout.addLayout(self.widthHorizontalLayout, 1, 1, 1, 1)
        self.minesHorizontalLayout = QtWidgets.QHBoxLayout()
        self.minesHorizontalLayout.setObjectName("minesHorizontalLayout")
        self.minesLabel = QtWidgets.QLabel(self.centralwidget)
        self.minesLabel.setStyleSheet("color: white")
        self.minesLabel.setObjectName("minesLabel")
        self.minesHorizontalLayout.addWidget(self.minesLabel)
        self.minesNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.minesNumber.setStyleSheet("color: white")
        self.minesNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.minesNumber.setProperty("intValue", 8)
        self.minesNumber.setObjectName("minesNumber")
        self.minesHorizontalLayout.addWidget(self.minesNumber)
        self.minesPlusButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minesPlusButton.sizePolicy().hasHeightForWidth())
        self.minesPlusButton.setSizePolicy(sizePolicy)
        self.minesPlusButton.setMaximumSize(QtCore.QSize(40, 30))
        self.minesPlusButton.setStyleSheet("color: white")
        self.minesPlusButton.setObjectName("minesPlusButton")
        self.minesHorizontalLayout.addWidget(self.minesPlusButton)
        self.minesMinusButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minesMinusButton.sizePolicy().hasHeightForWidth())
        self.minesMinusButton.setSizePolicy(sizePolicy)
        self.minesMinusButton.setMaximumSize(QtCore.QSize(40, 30))
        self.minesMinusButton.setStyleSheet("color: white")
        self.minesMinusButton.setObjectName("minesMinusButton")
        self.minesHorizontalLayout.addWidget(self.minesMinusButton)
        self.minesHorizontalLayout.setStretch(0, 2)
        self.minesHorizontalLayout.setStretch(1, 1)
        self.gridLayout.addLayout(self.minesHorizontalLayout, 3, 1, 1, 1)
        self.buttonHorizontalLayout = QtWidgets.QHBoxLayout()
        self.buttonHorizontalLayout.setObjectName("buttonHorizontalLayout")
        self.buttonVerticalLayout = QtWidgets.QVBoxLayout()
        self.buttonVerticalLayout.setSpacing(2)
        self.buttonVerticalLayout.setObjectName("buttonVerticalLayout")
        self.playGameButton = QtWidgets.QPushButton(self.centralwidget)
        self.playGameButton.setStyleSheet("color: white; background-color: red")
        self.playGameButton.setObjectName("playGameButton")
        self.buttonVerticalLayout.addWidget(self.playGameButton)
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setStyleSheet("color: white")
        self.cancelButton.setObjectName("cancelButton")
        self.buttonVerticalLayout.addWidget(self.cancelButton)
        self.buttonHorizontalLayout.addLayout(self.buttonVerticalLayout)
        self.gridLayout.addLayout(self.buttonHorizontalLayout, 4, 1, 1, 1)
        self.heightHorizontalLayout = QtWidgets.QHBoxLayout()
        self.heightHorizontalLayout.setObjectName("heightHorizontalLayout")
        self.heightLabel = QtWidgets.QLabel(self.centralwidget)
        self.heightLabel.setStyleSheet("color: white")
        self.heightLabel.setObjectName("heightLabel")
        self.heightHorizontalLayout.addWidget(self.heightLabel)
        self.heightNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.heightNumber.setStyleSheet("color: white")
        self.heightNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.heightNumber.setProperty("intValue", 8)
        self.heightNumber.setObjectName("heightNumber")
        self.heightHorizontalLayout.addWidget(self.heightNumber)
        self.heightPlusButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heightPlusButton.sizePolicy().hasHeightForWidth())
        self.heightPlusButton.setSizePolicy(sizePolicy)
        self.heightPlusButton.setMaximumSize(QtCore.QSize(40, 30))
        self.heightPlusButton.setStyleSheet("color: white")
        self.heightPlusButton.setObjectName("heightPlusButton")
        self.heightHorizontalLayout.addWidget(self.heightPlusButton)
        self.heightMinusButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heightMinusButton.sizePolicy().hasHeightForWidth())
        self.heightMinusButton.setSizePolicy(sizePolicy)
        self.heightMinusButton.setMaximumSize(QtCore.QSize(40, 30))
        self.heightMinusButton.setStyleSheet("color: white")
        self.heightMinusButton.setObjectName("heightMinusButton")
        self.heightHorizontalLayout.addWidget(self.heightMinusButton)
        self.heightHorizontalLayout.setStretch(0, 2)
        self.heightHorizontalLayout.setStretch(1, 1)
        self.gridLayout.addLayout(self.heightHorizontalLayout, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.widthLabel.setText(_translate("MainWindow", "Width"))
        self.widthPlusButton.setText(_translate("MainWindow", "+"))
        self.widthMinusButton.setText(_translate("MainWindow", "-"))
        self.minesLabel.setText(_translate("MainWindow", "Mines"))
        self.minesPlusButton.setText(_translate("MainWindow", "+"))
        self.minesMinusButton.setText(_translate("MainWindow", "-"))
        self.playGameButton.setText(_translate("MainWindow", "Play Game"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.heightLabel.setText(_translate("MainWindow", "Height"))
        self.heightPlusButton.setText(_translate("MainWindow", "+"))
        self.heightMinusButton.setText(_translate("MainWindow", "-"))
