import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.QtGui import QIcon

"""
    Этот класс предназначен для показа данных пароля
"""


class DisplayPasswordWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/displayPassword.ui", self)

        # взятие данных пароля
        with open("DB files/password", mode="r") as file:
            data = file.read().split("\n")

        # вывод данных на экран
        self.service.setText(f"Сервис: {data[0]}")
        self.login.setText(f"Логин: {data[1]}")
        self.password.setText(f"Пароль: {data[2]}")

        # добавляет иконку приложения
        app.setWindowIcon(QIcon("Presentation files/logo.png"))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DisplayPasswordWidget()
    ex.show()
    sys.exit(app.exec())
