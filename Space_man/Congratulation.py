import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

"""
    Этот класс предназначен для поздравления нашего земляка, второго косманавта,
    Андрияна Николаева!
"""


class SpaceMan(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/spaceMan.ui", self)

        pixmap = QPixmap("Space_man/Nikolaev.jpg")
        self.image.setPixmap(pixmap)

        text = ("Это приложение создано в честь года космонавтики в Чувашии. \n"
                "Космонавтом ведь неудобно хранить пароля в бумажном виде, \n"
                "а мое приложение создано именно для таких условий, \n"
                "чтобы космонавтам всегда было удобно и безопасно хранить \n"
                "свои пароли.")

        self.congratulation.setText(text)
        self.congratulation.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # добавляет иконку приложения
        app.setWindowIcon(QIcon("Presentation files/logo.png"))

        # открытие окна входа
        self.application_button.clicked.connect(self.my_exit)

    def my_exit(self):
        sys.exit(app.exec())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SpaceMan()
    ex.show()
    sys.exit(app.exec())
