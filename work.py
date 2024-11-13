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

        self.passwords_buttons_group = []
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
                passwords_data = self.taking_passwords_from_DB()

                # вывод и сохранение паролей
                for password_data in passwords_data:
                    self.password_output_safe(password_data)

                self.last_button = passwords_data[-1]
            except Exception:
                print("Видимо БД пуст")

    def folders_work(self):
        if self.this_moment_task != "folder":
            # смена режима окна на добавления папок
            self.this_moment_task = "folder"

            # показ кнопки добавления папки
            self.add_button.setText("Создать папку")
            self.add_button.show()

            for password_button in self.passwords_buttons_group:
                password_button.hide()

    def add(self):
        if self.this_moment_task == "password":
            try:
                subprocess.run(['python', 'add password.py'])

                # взятие пароля для вывода
                password_data = self.taking_passwords_from_DB()[-1]

                if password_data != self.last_button:
                    # вывод и сохранение пароля
                    self.password_output_safe(password_data)

                    self.last_button = password_data
            except Exception:
                print("Видимо БД пуст")
        elif self.this_moment_task == "folder":
            subprocess.run(['python', 'add folder.py'])

    def taking_passwords_from_DB(self):
        con = sqlite3.connect("DB files/users.db")
        with con:
            passwords_data = list(con.execute("""SELECT * FROM passwords"""))

        return passwords_data

    def password_output_safe(self, password):
        # вывод пароля
        password_button = QPushButton(password[0])
        password_button.setFixedSize(760, 40)

        self.password_layout.addWidget(password_button)

        # сохранение пароля в список
        self.passwords_buttons_group.append(password_button)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WorkWidget()
    ex.show()
    sys.exit(app.exec())
