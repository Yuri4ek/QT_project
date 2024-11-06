import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog


class RegistrationWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/registrationWindow.ui", self)

        self.make_button.clicked.connect(self.make_account)

    def make_account(self):
        first_name = self.fname_edit.text()
        last_name = self.lname_edit.text()
        login = self.login_edit.text()
        password = self.password_edit.text()




def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegistrationWidget()
    ex.show()
    sys.exit(app.exec())
