import sys

import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog

import subprocess


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

        con = sqlite3.connect("users.db")

        with con:
            data = con.execute("""SELECT * FROM clients""")

        # проверка на то, есть ли клиент с таким login-ом
        flag = True
        for row in data:
            if row[2] == login:
                flag = False
                break

        if flag:
            sql = """INSERT INTO clients 
                    (f_name, l_name, login, password) values(?, ?, ?, ?)"""

            data = (first_name, last_name, login, password,)

            # добавляет пользователя
            with con:
                con.execute(sql, data)

            sys.exit(app.exec())
        else:
            file = __file__

            subprocess.run(['python', 'error.py', file])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegistrationWidget()
    ex.show()
    sys.exit(app.exec())
