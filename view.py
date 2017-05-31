from PyQt5.QtWidgets import *
import _datetime as dt


class Helper:
    def row_to_table(self, ui, row_series, num=None):
        """Writes row_series to ui.table"""
        if num is None:
            num = ui.table.rowCount()
        ui.table.insertRow(num)
        ui.table.setItem(num, 0, QTableWidgetItem(str(row_series['value'])))
        ui.table.setItem(num, 1, QTableWidgetItem(row_series['date'].strftime("%Y%m%d")))
        ui.table.setItem(num, 2, QTableWidgetItem(row_series['comment']))

    def load_to_table(self, ui, acc):
        """Loads contents of acc to table widget"""
        # print(acc)

        # do things i didn't find a way to do with qt designer
        ui.table.setHorizontalHeaderItem(0, QTableWidgetItem("how much"))
        ui.table.setHorizontalHeaderItem(1, QTableWidgetItem("when"))
        ui.table.setHorizontalHeaderItem(2, QTableWidgetItem("comment"))
        ui.table.setColumnWidth(0, 100)
        ui.table.setColumnWidth(1, 100)
        ui.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

        # print(acc)
        ui.balance_l.setText("0")
        for i, row in acc.account.iloc[::-1].iterrows():
            # print(i)
            # print(row)
            self.row_to_table(ui, row)
        ui.balance_l.setText(str(acc.get_sum()))

    def update_balance(self, ui, acc):
        res = 0
        for i, row in acc.account:
            res += int(row['value'])
        ui.balance_l.setText(str(res))


class Interface:
    def make_push_button_clicked(self, acc, ui):
        """Function for push button clocking"""

        def push_button_clicked():
            # print(acc.account)
            value = ui.amountLine.text()
            comment = ui.commentLine.text()
            # print(ui.checkBox.isChecked())
            # print(date)
            try:
                intvalue = int(value)
            except ValueError:
                pass
            else:
                if ui.use_this_date_cb.isChecked():
                    date = ui.dateEdit.date().toPyDate().strftime("%Y%m%d")
                    acc.add_new_data(value=value, comment=comment, date=date)
                else:
                    acc.add_new_data(value=int(value), comment=comment)

                ui_helper = Helper()
                ui_helper.row_to_table(ui, acc.account.iloc[len(acc.account.index) - 1], 0)
                ui.balance_l.setText(str(acc.get_sum()))

        return push_button_clicked

    def make_pop_button_clicked(self, acc, ui):
        """Function for pop button clocking"""

        def pop_button_clicked():
            acc.drop_last()
            ui.balance_l.setText(str(acc.get_sum()))
            # print(acc)
            ui.table.removeRow(0)

        return pop_button_clicked

    def make_filter_button_clicked(self, acc, ui):
        """Function for filter button clocking"""

        def filter_button_clicked():
            new_acc = acc
            if ui.by_date_cb.isChecked():
                new_acc = new_acc.get_by_date(ui.from_date.date().toPyDate().strftime("%Y%m%d"),
                                              ui.to_date.date().toPyDate().strftime("%Y%m%d"))
            if ui.sort_by_value_cb.isChecked():
                new_acc.account = new_acc.account.sort_values(["value"])
            if ui.by_comment_cb.isChecked():
                new_acc = new_acc.get_by_comment(ui.by_comment_le.text())
            while ui.table.rowCount() > 0:
                ui.table.removeRow(0)
            ui_helper = Helper()
            ui_helper.load_to_table(ui, new_acc)

        return filter_button_clicked
