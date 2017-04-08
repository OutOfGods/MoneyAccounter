import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Accounter import *
from Accounter import Accounter
from ui_window import Ui_MainWindow
import pandas as pd

def addButton_clicked():
    print("add")

def removeButton_clicked():
    print("remove")

def load_to_table(ui, acc):
    acc.load_data()
    print(acc)
    
    ui.table.setHorizontalHeaderItem(0, QTableWidgetItem("how much"))
    ui.table.setHorizontalHeaderItem(1, QTableWidgetItem("when"))
    ui.table.setHorizontalHeaderItem(2, QTableWidgetItem("comment"))
    ui.table.setColumnWidth(0, 100)
    ui.table.setColumnWidth(1, 100)
    ui.table.setColumnWidth(2, 500)

    for i, [ n, row ] in enumerate(acc.account.iterrows()):
        print(i)
        print(n)
        print(row['value'])
        print(row['date'])
        print(row['comment'])
        print('----')
        ui.table.insertRow(ui.table.rowCount())
        ui.table.setItem(i, 0, QTableWidgetItem(str(row['value'])))
        ui.table.setItem(i, 1, QTableWidgetItem(row['date'].strftime("%d/%m/%Y")))
        ui.table.setItem(i, 2, QTableWidgetItem(row['comment']))

def start():
    app = QApplication(sys.argv)
    window = QDialog()
    QShortcut(QKeySequence("Ctrl+Q"), window, window.close)
    
    ui = Ui_MainWindow()
    ui.setupUi(window)

    acc = Accounter()
    
    load_to_table(ui, acc)

    ui.addButton.clicked.connect(addButton_clicked)
    ui.removeButton.clicked.connect(removeButton_clicked)        
    
    window.show()
    sys.exit(app.exec_())

if __name__== "__main__":
    start()
