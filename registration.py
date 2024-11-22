import sys

import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.QtGui import QIcon

import subprocess

"""
    Этот класс предназначен для регистрации (добавления нового аккаунта в БД)
"""


class RegistrationWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/registrationWindow.ui", self)

        self.make_button.clicked.connect(self.make_account)

        # добавляет иконку приложения
        app.setWindowIcon(QIcon("Presentation files/logo.png"))

    def make_account(self):
        first_name = self.fname_edit.text()
        last_name = self.lname_edit.text()
        login = self.login_edit.text()
        password = self.password_edit.text()

        con = sqlite3.connect("DB files/users.db")

        with con:
            data = con.execute("""SELECT * FROM clients""")

        # проверка на то, есть ли клиент с таким login-ом
        flag = True
        for row in data:
            if row[2] == login:
                flag = False
                break

        # если пользователя с таким логином нету, то создается новый аккаунт
        # иначе выйдет окно ошибки
        if flag:
            sql = """INSERT INTO clients 
                    (f_name, l_name, login, password) values(?, ?, ?, ?)"""

            data = (first_name, last_name, login, password,)

            # добавляет пользователя
            with con:
                con.execute(sql, data)

            # добавляет логин пользователя для дальнейшей работы
            with open("DB files/This moment client.txt", mode="w+") as f:
                f.write(login)

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
