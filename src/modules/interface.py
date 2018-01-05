# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication , QMainWindow, QWidget , QFileDialog
from src.ui.main import Ui_MainWindow
from src.modules.act import fetch_act_by_id


class MainForm(QMainWindow , Ui_MainWindow):
    def __init__(self):
        super(MainForm,self).__init__()
        self.setupUi(self)
        self.act_id_edit.returnPressed.connect(self.onQuery)


    def onQuery(self):
        data = fetch_act_by_id(self.act_id_edit.text())
        self.mongo_id_edit.setText(data.get('mongo_id'))
        self.title_edit.setText(data.get('title'))