import sys

import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog

import subprocess


class AuthorizationWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/authorizationWindow.ui", self)

        self.entrance_button.clicked.connect(self.open_account)

    def open_account(self):
        login = self.login_edit.text()
        password = self.password_edit.text()

        con = sqlite3.connect("users.db")

        with con:
            data = con.execute("""SELECT * FROM clients""")

        # проверка на то, есть ли клиент с таким login-ом и правильный ли
        # пароль
        flag = False
        for row in data:
            if row[2] == login and row[3] == password:
                flag = True
                break

        if flag:
            sys.exit(app.exec())
        else:
            file = __file__

            subprocess.run(['python', 'error.py', file])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AuthorizationWidget()
    ex.show()
    sys.exit(app.exec())
