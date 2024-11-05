import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog


class RegistrationWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/registrationWindow.ui", self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegistrationWidget()
    ex.show()
    sys.exit(app.exec())
