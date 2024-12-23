import sys

import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import (QApplication, QMainWindow, QInputDialog,
                             QFileDialog)
from PyQt6.QtGui import QIcon, QPixmap

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

        # находит и записывает id пользователя
        with con:
            sql = f"""SELECT id FROM clients WHERE login='{self.client}' """
            client_id = list(con.execute(sql))[0][0]

        with con:
            data = con.execute("""SELECT * FROM clients""")

        for client in data:
            if client[0] == client_id:
                first_name = client[1]
                last_name = client[2]
                password = client[4]

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

        self.change_login.clicked.connect(self.change_client_login)
        self.change_password.clicked.connect(self.change_client_password)
        self.change_image.clicked.connect(self.change_client_image)

        # добавляет иконку приложения
        app.setWindowIcon(QIcon("Presentation files/logo.png"))

    def change_client_login(self):
        new_client, ok_pressed = QInputDialog.getText(
            self, "Изменение логина", "Введите новый логин")

        if ok_pressed:
            con = sqlite3.connect("DB files/users.db")

            with con:
                sql = f"""
                    UPDATE clients SET login = '{new_client}'
                    WHERE login = '{self.client}'
                    """
                con.execute(sql)

            # изменение логина клиента
            with open("DB files/This moment client.txt", mode="w") as file:
                file.write(new_client)

            self.client_login.setText(new_client)

            self.client = new_client

    def change_client_password(self):
        new_password, ok_pressed = QInputDialog.getText(
            self, "Изменение пароля", "Введите новый пароль")

        if ok_pressed:
            con = sqlite3.connect("DB files/users.db")

            with con:
                sql = f"""
                    UPDATE clients SET password = '{new_password}'
                    WHERE login = '{self.client}'
                    """
                con.execute(sql)

            self.client_password.setText(new_password)

    def change_client_image(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]

        pixmap = QPixmap(fname)

        self.image_label.setPixmap(pixmap)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WorkWidget()
    ex.show()
    sys.exit(app.exec())
