import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog

"""
    Этот класс предназначен для взятие данных для создания пароля
"""


class AddPasswordWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/addPassword.ui", self)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddPasswordWidget()
    ex.show()
    sys.exit(app.exec())
