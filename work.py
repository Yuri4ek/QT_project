import sys

import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

import subprocess

"""
    Этот класс предназначен для работы с паролями и папками
"""


class WorkWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/workWindow.ui", self)

        self.this_moment_task = None

        self.add_button.hide()

        # делает данное окно для работы с паролями
        self.passwords_button.clicked.connect(self.passwords_work)

        # делает данное окно для работы с папками
        self.folders_button.clicked.connect(self.folders_work)

        self.add_button.clicked.connect(self.add)

    def passwords_work(self):
        self.this_moment_task = "password"

        self.add_button.setText("Добавить пароль")
        self.add_button.show()

    def folders_work(self):
        self.this_moment_task = "folder"

        self.add_button.setText("Создать папку")
        self.add_button.show()

    def add(self):
        con = sqlite3.connect("DB files/users.db")
        sql = """
                INSERT INTO clients 
                (service_name, login, password, client_login) 
                values(?, ?, ?, ?)
                """

        if self.this_moment_task == "password":
            subprocess.run(['python', 'add password.py'])

        elif self.this_moment_task == "folder":
            subprocess.run(['python', 'add folder.py'])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WorkWidget()
    ex.show()
    sys.exit(app.exec())
