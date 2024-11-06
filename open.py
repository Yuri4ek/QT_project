import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

import subprocess


class OpenWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/openWindow.ui", self)

        self.registration.clicked.connect(self.open_registration)
        self.authorization.clicked.connect(self.open_authorization)

    def open_registration(self):
        subprocess.run(['python', 'registration.py'])

    def open_authorization(self):
        subprocess.run(['python', 'authorization.py'])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OpenWidget()
    ex.show()
    sys.exit(app.exec())
