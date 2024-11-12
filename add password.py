import sys

import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog

import subprocess

"""
    Этот класс предназначен для взятие данных для создания пароля
"""


class AddPasswordWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/addPassword.ui", self)

        self.add_button.clicked.connect(self.safe_password)

    def safe_password(self):
        con = sqlite3.connect("DB files/users.db")

        # достаем название текущего пользователя/клиента
        with open("This moment client.txt", mode="r") as f:
            client = f.read()

        service = self.name_edit.text()
        login = self.login_edit.text()
        password = self.password_edit.text()

        # проверка на пустоту одну из переменных
        if service != "" and login != "" and password != "":
            with con:
                passwords_data = con.execute("""SELECT * FROM passwords""")
            for password_data in passwords_data:
                # проверка на существование пароля с таким логином в таком
                # сервисе
                if service == password_data[0] and login == password_data[1]:
                    file = __file__

                    subprocess.run(['python', 'error.py', file])

                    return

            sql = """
                INSERT INTO passwords 
                (service_name, login, password, client_login) 
                values(?, ?, ?, ?)
                """

            data = (service, login, password, client)

            # добавляет пароль в БД
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
    ex = AddPasswordWidget()
    ex.show()
    sys.exit(app.exec())
