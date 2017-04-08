# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Wed Mar 29 03:51:33 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(679, 385)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 671, 336))
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableView(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 20, 651, 201))
        self.table.setObjectName("table")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(10, 290, 96, 26))
        self.addButton.setObjectName("addButton")
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setGeometry(QtCore.QRect(110, 290, 96, 26))
        self.removeButton.setObjectName("removeButton")
        self.amountLine = QtWidgets.QLineEdit(self.centralwidget)
        self.amountLine.setGeometry(QtCore.QRect(10, 250, 91, 27))
        self.amountLine.setObjectName("amountLine")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(550, 250, 110, 27))
        self.dateEdit.setObjectName("dateEdit")
        self.commentLine = QtWidgets.QLineEdit(self.centralwidget)
        self.commentLine.setGeometry(QtCore.QRect(210, 250, 331, 27))
        self.commentLine.setObjectName("commentLine")
        self.tagsLine = QtWidgets.QLineEdit(self.centralwidget)
        self.tagsLine.setGeometry(QtCore.QRect(110, 250, 91, 27))
        self.tagsLine.setObjectName("tagsLine")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 230, 101, 17))
        self.label.setObjectName("label")
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 679, 25))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setGeometry(QtCore.QRect(0, 0, 3, 22))
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Accounter"))
        self.addButton.setText(_translate("MainWindow", "add"))
        self.removeButton.setText(_translate("MainWindow", "remove"))
        self.label.setText(_translate("MainWindow", "NEW RECORD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

