import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog

"""
    Этот класс предназначен для индивидуальных виджетов ошибок
"""


class ErrorWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/errorWindow.ui", self)

        try:
            file = str(sys.argv[1]).split('\\')[-1]

            # Выбирается текст для вывода ошибки в зависимости от открытого
            # окна
            if file == "registration.py":
                text = "Существует клиент с таким логином"
            elif file == "authorization.py":
                text = "Неправильный логин или пароль"
            elif file == "add password.py":
                text = "Одно из полей пусто"

            self.error_label.setText(text)
        except:
            pass


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ErrorWidget()
    ex.show()
    sys.exit(app.exec())
