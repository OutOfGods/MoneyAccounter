from PyQt5.QtWidgets import *


def row_to_table(ui, row_series, num=None):
    """Writes row_series to ui.table"""
    if num is None:
        num = ui.table.rowCount()
    ui.table.insertRow(num)
    ui.table.setItem(num, 0, QTableWidgetItem(str(row_series['value'])))
    ui.table.setItem(num, 1, QTableWidgetItem(row_series['date'].strftime("%d/%m/%Y")))
    ui.table.setItem(num, 2, QTableWidgetItem(row_series['comment']))


def load_to_table(ui, acc):
    """Loads contents of acc to table widget"""
    # print(acc)

    # do things i didn't find a way to do with qt designer
    ui.table.setHorizontalHeaderItem(0, QTableWidgetItem("how much"))
    ui.table.setHorizontalHeaderItem(1, QTableWidgetItem("when"))
    ui.table.setHorizontalHeaderItem(2, QTableWidgetItem("comment"))
    ui.table.setColumnWidth(0, 100)
    ui.table.setColumnWidth(1, 100)
    ui.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

    print(acc)
    ui.balance_l.setText("0")
    for i, row in acc.account.iloc[::-1].iterrows():
        # print(i)
        # print(row)
        row_to_table(ui, row)
    ui.balance_l.setText(str(acc.get_sum()))


def make_push_button_clicked(acc, ui):
    """Function for push button clocking"""
    def push_button_clicked():
        # print(acc.account)
        value = ui.amountLine.text()
        comment = ui.commentLine.text()
        # print(ui.checkBox.isChecked())
        # print(date)
        if ui.use_this_date_cb.isChecked():
            date = ui.dateEdit.date().toPyDate().strftime("%Y%m%d")
            acc.add_new_data(value=value, comment=comment, date=date)
        else:
            acc.add_new_data(value=value, comment=comment)
        row_to_table(ui, acc.account.iloc[len(acc.account.index)-1], 0)
        ui.balance_l.setText(str(acc.get_sum()))
    return push_button_clicked


def make_pop_button_clicked(acc, ui):
    """Function for pop button clocking"""
    def pop_button_clicked():
        acc.account = acc.account.drop(acc.account.tail(1).index)
        ui.balance_l.setText(str(acc.get_sum()))
        # print(acc)
        ui.table.removeRow(0)
    return pop_button_clicked


def make_filter_button_clicked(acc, ui):
    """Function for filter button clocking"""
    def filter_button_clicked():
        print("filter")
        new_acc = acc
        if ui.by_date_cb.isChecked():
            print("by date")
            new_acc = new_acc.get_by_date(ui.from_date.date().toPyDate().strftime("%Y%m%d"),
                                          ui.to_date.date().toPyDate().strftime("%Y%m%d"))
        if ui.sort_by_value_cb.isChecked():
            print("by val")
            new_acc.account = new_acc.account.sort_values(["value"])
        if ui.by_comment_cb.isChecked():
            print("by comment")
            new_acc = new_acc.get_by_comment(ui.by_comment_le.text())
        print(new_acc)
        while ui.table.rowCount() > 0:
            ui.table.removeRow(0)
        load_to_table(ui, new_acc)
    return filter_button_clicked


def update_balance(ui, acc):
    res = 0
    for i, row in acc.account:
        res += int(row['value'])
    ui.balance_l.setText(str(res))
