import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Accounter import *
from ui_window import Ui_MainWindow

def addButton_clicked():
    print("add")

def removeButton_clicked():
    print("remove")

if __name__== "__main__":
    app = QApplication(sys.argv)
    window = QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    ui.addButton.clicked.connect(addButton_clicked)
    ui.removeButton.clicked.connect(removeButton_clicked)

    window.show()
    sys.exit(app.exec_())
