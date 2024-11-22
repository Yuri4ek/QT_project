import sys

import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.QtGui import QIcon

import subprocess

"""
    Этот класс предназначен для взятие данных для создания пароля
"""


class AddPasswordWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/addPassword.ui", self)

        self.add_button.clicked.connect(self.safe_password)

        # добавляет иконку приложения
        app.setWindowIcon(QIcon("Presentation files/logo.png"))

    def safe_password(self):
        service = self.name_edit.text()
        login = self.login_edit.text()
        password = self.password_edit.text()
        client = self.taking_client()

        # проверка на пустоту одну из переменных
        if service != "" and login != "" and password != "":
            con = sqlite3.connect("DB files/users.db")

            # взятие паролей
            with con:
                passwords_data = con.execute("""SELECT * FROM passwords""")

            for password_data in passwords_data:
                # проверка на существование пароля с таким логином в таком
                # сервисе
                if service == password_data[1] and login == password_data[2]:
                    file = __file__

                    subprocess.run(['python', 'error.py', file])

                    return

            # находит и записывает id пользователя
            with con:
                sql = f"""SELECT id FROM clients WHERE login='{client}' """
                client_id = list(con.execute(sql))[0][0]

            sql = """
                INSERT INTO passwords 
                (service_name, login, password, client_id) 
                values(?, ?, ?, ?)
                """

            data = (service, login, password, client_id)

            # добавляет пароль в БД
            with con:
                con.execute(sql, data)

            sys.exit(app.exec())
        else:
            file = __file__

            subprocess.run(['python', 'error.py', file])

    def taking_client(self):
        # достаем название текущего пользователя/клиента
        with open("DB files/This moment client.txt", mode="r") as f:
            client = f.read()

        return client


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddPasswordWidget()
    ex.show()
    sys.exit(app.exec())
