# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Sun Apr  9 00:44:02 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 355)
        icon = QtGui.QIcon.fromTheme("terminator")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 700, 331))
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 20, 690, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.table.setMouseTracking(False)
        self.table.setColumnCount(3)
        self.table.setObjectName("table")
        self.table.setRowCount(0)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setDefaultSectionSize(229)
        self.table.horizontalHeader().setMinimumSectionSize(100)
        self.amountLine = QtWidgets.QLineEdit(self.centralwidget)
        self.amountLine.setGeometry(QtCore.QRect(10, 260, 91, 27))
        self.amountLine.setObjectName("amountLine")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(110, 260, 91, 27))
        self.dateEdit.setObjectName("dateEdit")
        self.commentLine = QtWidgets.QLineEdit(self.centralwidget)
        self.commentLine.setGeometry(QtCore.QRect(210, 260, 481, 27))
        self.commentLine.setObjectName("commentLine")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(10, 300, 96, 26))
        self.addButton.setObjectName("addButton")
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setGeometry(QtCore.QRect(110, 300, 96, 26))
        self.removeButton.setObjectName("removeButton")
        self.tagsLine = QtWidgets.QLineEdit(self.centralwidget)
        self.tagsLine.setGeometry(QtCore.QRect(600, 300, 91, 27))
        self.tagsLine.setObjectName("tagsLine")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 240, 101, 17))
        self.label.setObjectName("label")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Accounter"))
        self.addButton.setText(_translate("MainWindow", "add"))
        self.removeButton.setText(_translate("MainWindow", "remove"))
        self.label.setText(_translate("MainWindow", "NEW RECORD"))

