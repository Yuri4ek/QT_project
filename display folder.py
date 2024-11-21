import sys

import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

import subprocess

"""
    Этот класс предназначен для показа данных папки
"""


class DisplayFolderWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/folderWindow.ui", self)

        # взятие данных папки
        with open("DB files/folder", mode="r") as file:
            data = file.read().split("\n")

        # вывод паролей
        try:
            passwords_id = data[1].split(" ")

            con = sqlite3.connect("DB files/users.db")

            with con:
                passwords_data = con.execute("""SELECT * FROM passwords""")
            for password_data in passwords_data:
                for id in passwords_id:
                    if int(id) == password_data[0]:
                        self.password_output(password_data)

                        break
        except Exception:
            print("Видимо БД пуст")

        # вывод названии папки на экран
        self.folder_name.setText(f"Название папки: {data[0]}")

        # изменение цвета названия папки на белый
        self.folder_name.setStyleSheet("color: white;")

        # делает фон звездным
        self.setStyleSheet("""
                QMainWindow { background-image:url(Space_man/phon.jpg); 
                background-repeat: no-repeat; background-position: center; } 
                                """)

    def password_output(self, password):
        # вывод пароля
        password_button = QPushButton(password[1])
        password_button.setFixedSize(540, 40)

        self.password_layout.addWidget(password_button)

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
                    file.write("\n".join(password_data[1:-1]))

                # вывод пароля
                subprocess.run(['python', 'display password.py'])

                # удаление пароля
                with open("DB files/password", mode="w+") as file:
                    pass

                break


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DisplayFolderWidget()
    ex.show()
    sys.exit(app.exec())
