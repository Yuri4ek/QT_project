import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog

"""
    Этот класс предназначен для взятие данных для создания пароля
"""


class AddPasswordWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/addPassword.ui", self)

        self.add_button.clicked.connect(self.safe_password)

    def safe_password(self):
        # достаем название текущего пользователя/клиента
        with open("This moment client.txt", mode="r") as f:
            client = f.read()

        service = self.name_edit.text()
        login = self.login_edit.text()
        password = self.password_edit.text()

        # сохраняем пароль в файл, чтобы потом из него достать и добавить в БД
        with open("last password.txt", mode="w+") as f:
            f.write("\t".join([service, login, password, client]))

        sys.exit(app.exec())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddPasswordWidget()
    ex.show()
    sys.exit(app.exec())
