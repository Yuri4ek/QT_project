import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog


class ErrorWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/errorWindow.ui", self)

        try:
            file = str(sys.argv[1]).split('\\')[-1]

            if file == "registration.py":
                text = "Существует клиент с таким логином"
            elif file == "authorization.py":
                text = "Неправильный логин или пароль"

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
