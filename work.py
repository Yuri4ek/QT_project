import sys

import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout

import subprocess

"""
    Этот класс предназначен для работы с паролями и папками
"""


class WorkWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/workWindow.ui", self)

        self.this_moment_task = None

        self.buttons_group = []
        self.last_button = None

        self.add_button.hide()

        # делает данное окно для работы с паролями
        self.passwords_button.clicked.connect(self.passwords_work)

        # делает данное окно для работы с папками
        self.folders_button.clicked.connect(self.folders_work)

        self.add_button.clicked.connect(self.add)

    def passwords_work(self):
        if self.this_moment_task != "password":
            try:
                # смена режима окна на добавления паролей
                self.this_moment_task = "password"

                # показ кнопки добавления пароля
                self.add_button.setText("Добавить пароль")
                self.add_button.show()

                # взятие паролей для вывода
                con = sqlite3.connect("DB files/users.db")
                with con:
                    passwords_data = list(
                        con.execute("""SELECT * FROM passwords"""))

                # вывод паролей
                for i in range(len(passwords_data)):
                    password_button = QPushButton(passwords_data[i][0])
                    password_button.setFixedSize(760, 40)

                    self.password_layout.addWidget(password_button)

                    self.buttons_group.append(password_button)

                self.last_button = passwords_data[-1]
            except Exception:
                print("Видимо БД пуст")

    def folders_work(self):
        # показ кнопки добавления папки
        self.add_button.setText("Создать папку")
        self.add_button.show()

        for password_button in self.buttons_group:
            password_button.hide()

        # смена режима окна на добавления папок
        self.this_moment_task = "folder"

    def add(self):
        if self.this_moment_task == "password":
            try:
                subprocess.run(['python', 'add password.py'])

                # взятие пароля для вывода
                con = sqlite3.connect("DB files/users.db")
                with con:
                    password_data = list(con.execute("""
                                                        SELECT * FROM passwords
                                                    """))[-1]

                if password_data != self.last_button:
                    # вывод пароля
                    password_button = QPushButton(password_data[0])
                    password_button.setFixedSize(760, 40)

                    self.password_layout.addWidget(password_button)

                    self.buttons_group.append(password_button)
                    self.last_button = password_data
            except Exception:
                print("Видимо БД пуст")
        elif self.this_moment_task == "folder":
            subprocess.run(['python', 'add folder.py'])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WorkWidget()
    ex.show()
    sys.exit(app.exec())
