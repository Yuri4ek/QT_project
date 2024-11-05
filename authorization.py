import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog


class AuthorizationWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/authorizationWindow.ui", self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AuthorizationWidget()
    ex.show()
    sys.exit(app.exec())
