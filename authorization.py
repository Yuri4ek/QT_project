import sys

import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog

import subprocess

"""
    Этот класс предназначен для авторизации (входа в систему), если аккаунт уже 
    находится в БД
"""


class AuthorizationWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/authorizationWindow.ui", self)

        self.entrance_button.clicked.connect(self.open_account)

    def open_account(self):
        login = self.login_edit.text()
        password = self.password_edit.text()

        con = sqlite3.connect("DB files/users.db")

        with con:
            data = con.execute("""SELECT * FROM clients""")

        # проверка на то, есть ли клиент с таким login-ом и правильный ли
        # пароль
        flag = False
        for row in data:
            if row[2] == login and row[3] == password and \
                    login != "" and password != "":
                flag = True
                break

        # если существует пользователь с таким логином и паролем,
        # то он заходит в систему иначе выйдет окно ошибки
        if flag:
            # добавляет логин пользователя для дальнейшей работы
            with open("This moment client.txt", mode="w+") as f:
                f.write(login)

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
