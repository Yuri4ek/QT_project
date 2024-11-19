import sys

import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

"""
    Этот класс предназначен для просмотра и изменения данных клиента
"""


class WorkWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/displayClientWindow.ui", self)

        # логин клиента
        with open("DB files/This moment client.txt", mode="r") as file:
            self.client = file.read()

        con = sqlite3.connect("DB files/users.db")

        with con:
            data = con.execute("""SELECT * FROM clients""")

        for client in data:
            if client[2] == self.client:
                first_name = client[0]
                last_name = client[1]
                password = client[3]

                break

        # делает фон звездным
        self.setStyleSheet("""
                QMainWindow { background-image:url(Space_man/phon.jpg); 
                background-repeat: no-repeat; background-position: center; } 
                                """)

        # делает текст белый
        self.client_name.setStyleSheet("color: white;")
        self.client_login.setStyleSheet("color: white;")
        self.client_password.setStyleSheet("color: white;")

        # заполняет label-ы данными
        self.client_name.setText(f"{first_name} {last_name}")
        self.client_login.setText(self.client)
        self.client_password.setText(password)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WorkWidget()
    ex.show()
    sys.exit(app.exec())