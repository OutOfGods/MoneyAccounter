from unittest.mock import patch, create_autospec
import unittest as ut

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QShortcut
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QKeySequence
import sys 

import ui_controller as uic
import ui_window as uiw
import accounter
from view import Helper, Interface

class TestStuff(ut.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a = accounter.Accounter()
        cls.a.load_data()
        cls.a.sort_by_date()
        cls.ap = QApplication(sys.argv)
        cls.mw = QDialog()
        cls.ui = uiw.Ui_MainWindow()
        cls.ui.setupUi(cls.mw)

    @patch.object(QApplication, "__init__")
    @patch.object(QDialog, "__init__")
    @patch.object(QShortcut, "__init__")
    @patch.object(QKeySequence, "__init__")
    def test_app_init(self, mock_ks_init, mock_sh_init, mock_qd_init, mock_qa_init):
        args = "args to call with"
        sys.argv = args
        
        mock_ks_init.return_value = None
        mock_sh_init.return_value = None
        mock_qd_init.return_value = None
        mock_qa_init.return_value = None
        
        uic.UIController().app_init()
        mock_qa_init.assert_called_with(args)
        mock_qd_init.assert_called()
        mock_ks_init.assert_called_with("Ctrl+Q")
        mock_sh_init.assert_called()

        sys.argv = []

    @patch.object(QApplication, "exec_")
    @patch.object(QDialog, "show")
    @patch("ui_controller.sys.exit")
    def test_setup_and_run(self, mock_sysexit, mock_dia_show, mock_app_exec):
        uic.UIController().setup_and_run()
        mock_dia_show.assert_called()
        mock_app_exec.assert_called()
        mock_sysexit.assert_called()

    @patch.object(accounter.Accounter, "add_new_data")
    def test_push_button(self, mock_add):
        self.ui.use_this_date_cb.setChecked(False)
        self.ui.amountLine.setText("123")
        self.ui.commentLine.setText("opana")
        
        Interface().make_push_button_clicked(self.a, self.ui)()
        mock_add.assert_called_with(comment="opana", value=123)

    @patch.object(accounter.Accounter, "drop_last")
    def test_pop_button(self, mock_drop):
        Interface().make_pop_button_clicked(self.a, self.ui)()
        mock_drop.assert_called()

    def test_filter_button(self):
        self.ui.by_date_cb.setChecked(True)
        self.ui.sort_by_value_cb.setChecked(True)
        self.ui.by_comment_cb.setChecked(True)
        Interface().make_filter_button_clicked(self.a, self.ui)()
        
    
if __name__ == "__main__":
    ut.main()
