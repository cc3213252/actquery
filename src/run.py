__author__ = 'yudan.chen'

import sys
from src.modules.interface import MainForm
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

