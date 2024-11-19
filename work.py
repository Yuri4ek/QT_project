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

        # логин клиента
        with open("DB files/This moment client.txt", mode="r") as file:
            self.client = file.read()

        # показ текущего клиента
        self.client_button.setText(self.client)
        self.client_button.clicked.connect(self.display_client)

        self.this_moment_task = None

        # переменные для упрощения работы с паролями
        self.password_menu_open_flag = True
        self.passwords_buttons_group = []
        self.last_password_data = None

        # переменные для упрощения работы с папками
        self.folder_menu_open_flag = True
        self.folders_buttons_group = []
        self.last_folder_data = None

        self.add_button.hide()

        # делает данное окно для работы с паролями
        self.passwords_button.clicked.connect(self.passwords_work)

        # делает данное окно для работы с папками
        self.folders_button.clicked.connect(self.folders_work)

        self.add_button.clicked.connect(self.add)

        # делает фон звездным
        self.setStyleSheet("""
                QMainWindow { background-image:url(Space_man/phon.jpg); 
                background-repeat: no-repeat; background-position: center; } 
                                """)

    def display_client(self):
        subprocess.run(['python', 'display and change client data.py'])

        # логин клиента
        with open("DB files/This moment client.txt", mode="r") as file:
            self.client = file.read()

        self.client_button.setText(self.client)

    def passwords_work(self):
        if self.this_moment_task != "password":
            # смена режима окна на добавления паролей
            self.this_moment_task = "password"

            # показ кнопки добавления пароля
            self.add_button.setText("Добавить пароль")
            self.add_button.show()

            try:
                if self.password_menu_open_flag:
                    # взятие паролей для вывода
                    passwords_data = self.taking_passwords_from_DB()

                    # вывод и сохранение паролей
                    for password_data in passwords_data:
                        if password_data[-1] == self.client:
                            self.password_output_safe(password_data)

                    self.last_password_data = passwords_data[-1]

                    self.password_menu_open_flag = False
                else:
                    for password_button in self.passwords_buttons_group:
                        password_button.show()
            except Exception:
                print("Видимо БД пуст")

            for folder_button in self.folders_buttons_group:
                folder_button.hide()

    def folders_work(self):
        if self.this_moment_task != "folder":
            # смена режима окна на добавления папок
            self.this_moment_task = "folder"

            # показ кнопки добавления папки
            self.add_button.setText("Создать папку")
            self.add_button.show()

            try:
                if self.folder_menu_open_flag:
                    # взятие папок для вывода
                    folders_data = self.taking_folders_from_DB()

                    # вывод и сохранение папок
                    for folder_data in folders_data:
                        if folder_data[-1] == self.client:
                            self.folder_output_safe(folder_data)

                    self.last_folder_data = folders_data[-1]

                    self.folder_menu_open_flag = False
                else:
                    for folder_button in self.folders_buttons_group:
                        folder_button.show()
            except Exception:
                print("Видимо БД пуст")

            for password_button in self.passwords_buttons_group:
                password_button.hide()

    def add(self):
        if self.this_moment_task == "password":
            try:
                subprocess.run(['python', 'add password.py'])

                # взятие пароля для вывода
                password_data = self.taking_passwords_from_DB()[-1]

                if password_data != self.last_password_data:
                    if password_data[-1] == self.client:
                        # вывод и сохранение пароля
                        self.password_output_safe(password_data)

                    self.last_password_data = password_data
            except Exception:
                print("Видимо БД пуст")
        elif self.this_moment_task == "folder":
            try:
                subprocess.run(['python', 'add folder.py'])

                # взятие папки для вывода
                folder_data = self.taking_folders_from_DB()[-1]

                if folder_data != self.last_folder_data:
                    if folder_data[-1] == self.client:
                        # вывод и сохранение папки
                        self.folder_output_safe(folder_data)

                    self.last_folder_data = folder_data
            except Exception:
                print("Видимо БД пуст")

    def taking_passwords_from_DB(self):
        con = sqlite3.connect("DB files/users.db")
        with con:
            passwords_data = list(con.execute("""SELECT * FROM passwords"""))

        return passwords_data

    def password_output_safe(self, password):
        # вывод пароля
        password_button = QPushButton(password[1])
        password_button.setFixedSize(760, 40)

        self.password_layout.addWidget(password_button)

        # сохранение пароля в список
        self.passwords_buttons_group.append(password_button)

        # вывод данных пароля при нажатии кнопки
        password_button.clicked.connect(self.display_password_data)

    def display_password_data(self):
        service = self.sender().text()

        con = sqlite3.connect("DB files/users.db")

        sql = """SELECT * FROM passwords"""

        with con:
            passwords_data = list(con.execute(sql))

        for password_data in passwords_data:
            if password_data[1] == service:
                # запись пароля
                with open("DB files/password", mode="w+") as file:
                    file.write("\n".join(password_data[1:]))

                # вывод пароля
                subprocess.run(['python', 'display password.py'])

                # удаление пароля
                with open("DB files/password", mode="w+") as file:
                    pass

                break

    def taking_folders_from_DB(self):
        con = sqlite3.connect("DB files/users.db")
        with con:
            folders_data = list(con.execute("""SELECT * FROM folders"""))

        return folders_data

    def folder_output_safe(self, folder):
        # вывод папки
        folder_button = QPushButton(folder[0])
        folder_button.setFixedSize(760, 40)

        self.folder_layout.addWidget(folder_button)

        # сохранение папки в список
        self.folders_buttons_group.append(folder_button)

        # вывод данных папки при нажатии кнопки
        folder_button.clicked.connect(self.display_folder_data)

    def display_folder_data(self):
        folder_name = self.sender().text()

        con = sqlite3.connect("DB files/users.db")

        sql = """SELECT * FROM folders"""

        with con:
            folders_data = list(con.execute(sql))

        for folder_data in folders_data:
            if folder_data[0] == folder_name:
                # запись папки
                with open("DB files/folder", mode="w+") as file:
                    file.write("\n".join(folder_data))

                # вывод папки
                subprocess.run(['python', 'display folder.py'])

                # удаление папки
                with open("DB files/folder", mode="w+") as file:
                    pass

                break


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WorkWidget()
    ex.show()
    sys.exit(app.exec())
