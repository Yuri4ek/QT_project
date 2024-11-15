import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

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

        text = ("Андриян Григорьевич – звездный сын чувашского народа, \n"
                "человек, открывший космос многим поколениям. Его жизненный \n"
                "путь – это умение мечтать, трудолюбиво делать все, чтобы эта \n"
                "мечта стала реальностью. Для всех нас это яркий пример. Мы \n"
                "должны помнить, сохранять и передавать из поколения в \n"
                "поколение все его достижения и подвиги.")
        self.congratulation.setText(text)
        self.congratulation.setAlignment(Qt.AlignmentFlag.AlignCenter)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SpaceMan()
    ex.show()
    sys.exit(app.exec())
