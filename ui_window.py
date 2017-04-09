# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Sun Apr  9 20:34:29 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(617, 355)
        icon = QtGui.QIcon.fromTheme("terminator")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 617, 331))
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 20, 600, 200))
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
        self.table.horizontalHeader().setDefaultSectionSize(100)
        self.table.horizontalHeader().setMinimumSectionSize(100)
        self.table.verticalHeader().setVisible(True)
        self.amountLine = QtWidgets.QLineEdit(self.centralwidget)
        self.amountLine.setGeometry(QtCore.QRect(10, 260, 91, 27))
        self.amountLine.setObjectName("amountLine")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(110, 260, 121, 27))
        self.dateEdit.setObjectName("dateEdit")
        self.commentLine = QtWidgets.QLineEdit(self.centralwidget)
        self.commentLine.setGeometry(QtCore.QRect(240, 260, 371, 27))
        self.commentLine.setObjectName("commentLine")
        self.push_button = QtWidgets.QPushButton(self.centralwidget)
        self.push_button.setGeometry(QtCore.QRect(10, 300, 96, 26))
        self.push_button.setObjectName("push_button")
        self.pop_button = QtWidgets.QPushButton(self.centralwidget)
        self.pop_button.setGeometry(QtCore.QRect(110, 300, 96, 26))
        self.pop_button.setObjectName("pop_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 230, 101, 17))
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(110, 230, 151, 22))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Accounter"))
        self.push_button.setText(_translate("MainWindow", "push"))
        self.pop_button.setText(_translate("MainWindow", "pop"))
        self.label.setText(_translate("MainWindow", "NEW RECORD"))
        self.checkBox.setText(_translate("MainWindow", "use this date?"))

