import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Accounter import *
from Accounter import Accounter
from ui_window import Ui_MainWindow
import pandas as pd

def row_to_table(ui, row_num, row_series):
    ui.table.insertRow(row_num)
    ui.table.setItem(row_num, 0, QTableWidgetItem(str(row_series['value'])))
    ui.table.setItem(row_num, 1, QTableWidgetItem(row_series['date'].strftime("%d/%m/%Y")))
    ui.table.setItem(row_num, 2, QTableWidgetItem(row_series['comment']))

def load_to_table(ui, acc):
    acc.load_data()
    # print(acc)

    # do things i didn't find a way to do with qt designer
    ui.table.setHorizontalHeaderItem(0, QTableWidgetItem("how much"))
    ui.table.setHorizontalHeaderItem(1, QTableWidgetItem("when"))
    ui.table.setHorizontalHeaderItem(2, QTableWidgetItem("comment"))
    ui.table.setColumnWidth(0, 100)
    ui.table.setColumnWidth(1, 100)
    ui.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

    # init table
    acc.sort_by_indexes()
    for i, row in acc.account.iterrows():
        row_to_table(ui, i, row)

def make_push_button_clicked(acc, ui):
    def push_button_clicked():
        # print(acc.account)
        value = ui.amountLine.text()
        comment = ui.commentLine.text()
        # print(ui.checkBox.isChecked())
        # print(date)
        if ui.checkBox.isChecked():
            date = ui.dateEdit.date().toPyDate().strftime("%Y%m%d")
            acc.add_new_data(value=value, comment=comment, date=date)
        else:
            acc.add_new_data(value=value, comment=comment)
        row_to_table(ui, 0, acc.account.iloc[len(acc.account.index) - 1])
        
    return push_button_clicked

def make_pop_button_clicked(acc, ui):
    def pop_button_clicked():
        acc.account = acc.account.drop(acc.account.tail(1).index)
        print(acc)
        ui.table.removeRow(0)

    return pop_button_clicked

def start(acc):
    app = QApplication(sys.argv)
    window = QDialog()
    QShortcut(QKeySequence("Ctrl+Q"), window, window.close)
    
    ui = Ui_MainWindow()
    ui.setupUi(window)

    # acc = Accounter()
    
    load_to_table(ui, acc)

    ui.push_button.clicked.connect(make_push_button_clicked(acc, ui))
    ui.pop_button.clicked.connect(make_pop_button_clicked(acc, ui))
    
    window.show()
    app.exec_()

if __name__== "__main__":
    acc = Accounter()
    start(acc)
    acc.save_data()
    # sys.exit()
