import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Accounter import *
from Accounter import Accounter
from ui_window import Ui_MainWindow
import pandas as pd
    
def removeButton_clicked():
    print("remove")

def row_to_table(ui, row_num, row_series):
    ui.table.insertRow(row_num)
    ui.table.setItem(row_num, 0, QTableWidgetItem(str(row_series['value'])))
    ui.table.setItem(row_num, 1, QTableWidgetItem(row_series['date'].strftime("%d/%m/%Y")))
    ui.table.setItem(row_num, 2, QTableWidgetItem(row_series['comment']))

def load_to_table(ui, acc):
    acc.load_data()
    print(acc)

    # do things i didn't find a way to do with qt designer
    ui.table.setHorizontalHeaderItem(0, QTableWidgetItem("how much"))
    ui.table.setHorizontalHeaderItem(1, QTableWidgetItem("when"))
    ui.table.setHorizontalHeaderItem(2, QTableWidgetItem("comment"))
    ui.table.setColumnWidth(0, 100)
    ui.table.setColumnWidth(1, 100)
    ui.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
    #ui.table.setColumnWidth(2, 350)

    # init table
    for i, [ n, row ] in enumerate(acc.account.iloc[::-1].iterrows()): # костылёк вышел, поцоны
        row_to_table(ui, i, row)
        # ui.table.insertRow(ui.table.rowCount())
        # ui.table.setItem(i, 0, QTableWidgetItem(str(row['value'])))
        # ui.table.setItem(i, 1, QTableWidgetItem(row['date'].strftime("%d/%m/%Y")))
        # ui.table.setItem(i, 2, QTableWidgetItem(row['comment']))

def make_push_button_clicked(acc, ui):
    def push_button_clicked():
        value=ui.amountLine.text()
        comment=ui.commentLine.text()
        acc.add_new_data(value=value, comment=comment)
        row_to_table(ui, 0, acc.account.iloc[len(acc.account.index) - 1])
        # ui.table.insertRow(0)
        # ui.table.setItem(0, 0, QTableWidgetItem(str(value)))
        # ui.table.setItem(0, 1, QTableWidgetItem(dt.datetime.now().strftime("%d/%m/%Y")))
        # ui.table.setItem(0, 2, QTableWidgetItem(comment))
        
        print("add")
        print(ui.dateEdit.date().toString())
        print(acc)
        print("------")
    return push_button_clicked

def start():
    app = QApplication(sys.argv)
    window = QDialog()
    QShortcut(QKeySequence("Ctrl+Q"), window, window.close)
    
    ui = Ui_MainWindow()
    ui.setupUi(window)

    acc = Accounter()
    
    load_to_table(ui, acc)

    ui.push_button.clicked.connect(make_push_button_clicked(acc, ui))
    ui.pop_button.clicked.connect(removeButton_clicked)        
    
    window.show()
    sys.exit(app.exec_())

if __name__== "__main__":
    start()
