import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon

import subprocess

"""
    Этот класс предназначен для связки всех других окон, с этого файла 
    начинается путь к программе
"""


class OpenWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/openWindow.ui", self)

        # при нажатии открывает окно регистрации, после, если регистрация
        # успешна, открывает рабочее окно
        self.registration.clicked.connect(self.open_registration)

        # при нажатии открывает окно авторизации, после, если вход успешен,
        # открывает рабочее окно
        self.authorization.clicked.connect(self.open_authorization)

        # открывает окно о Андрияне Николаеве
        self.andrian_congratulate()

        # делает фон звездным
        self.setStyleSheet("""
        QMainWindow { background-image:url(Space_man/phon.jpg); 
        background-repeat: no-repeat; background-position: center; } 
                        """)

        # добавляет иконку приложения
        app.setWindowIcon(QIcon("Presentation files/logo.png"))

    def resizeEvent(self, event):
        geometry = self.geometry()
        x, y = geometry.width(), geometry.height()

        self.registration.move(x // 2 - 100, y // 2 - 70)
        self.authorization.move(x // 2 - 100, y // 2 + 8)

    def open_registration(self):
        subprocess.run(['python', 'registration.py'])

        # если данные правильны, то открывает рабочее окно
        with open("DB files/This moment client.txt", mode="r") as f:
            if f.read() != "":
                ex.hide()

                subprocess.run(['python', 'work.py'])

                # удаляет логин
                with open("DB files/This moment client.txt", mode="w") as f:
                    pass

                self.show()

    def open_authorization(self):
        subprocess.run(['python', 'authorization.py'])

        # если данные правильны, то открывает рабочее окно
        with open("DB files/This moment client.txt", mode="r") as f:
            if f.read() != "":
                ex.hide()

                subprocess.run(['python', 'work.py'])

                # удаляет логин
                with open("DB files/This moment client.txt", mode="w") as f:
                    pass

                self.show()

    def andrian_congratulate(self):
        subprocess.run(['python', 'Space_man/Congratulation.py'])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OpenWidget()
    ex.show()
    sys.exit(app.exec())
