import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from accounter import Accounter
from ui_window import Ui_MainWindow
from view import *


def start():
    """Starts application"""
    app = QApplication(sys.argv)
    window = QDialog()
    QShortcut(QKeySequence("Ctrl+Q"), window, window.close)

    ui = Ui_MainWindow()
    ui.setupUi(window)
    ui.dateEdit.setDate(QDate.currentDate())
    ui.from_date.setDate(QDate.currentDate())
    ui.to_date.setDate(QDate.currentDate())

    acc = Accounter()

    acc.load_data()
    #acc.sort_by_date()
    load_to_table(ui, acc)

    ui.push_button.clicked.connect(make_push_button_clicked(acc, ui))
    ui.pop_button.clicked.connect(make_pop_button_clicked(acc, ui))
    ui.filter_button.clicked.connect(make_filter_button_clicked(acc, ui))

    window.show()
    app.exec_()
    acc.save_data()


if __name__ == "__main__":
    start()
    sys.exit()
