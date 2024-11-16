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

        self.ok_button.clicked.connect(self.exit)

        try:
            file = str(sys.argv[1]).split('\\')[-1]

            # Выбирается текст для вывода ошибки в зависимости от открытого
            # окна
            if file == "registration.py":
                text = "Существует клиент с таким логином"
            elif file == "authorization.py":
                text = "Неправильный логин или пароль"
            elif file == "add password.py":
                text = "Поле пусто или существует такой пароль"
            elif file == "add folder.py":
                text = "Поле пусто или существует такая папка"

            self.error_label.setText(text)
        except:
            pass

    def exit(self):
        sys.exit(app.exec())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ErrorWidget()
    ex.show()
    sys.exit(app.exec())
