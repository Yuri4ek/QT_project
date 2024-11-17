import sys

import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog, QCheckBox

import subprocess

"""
    Этот класс предназначен для взятие данных для создания папки
"""


class AddPasswordWidget(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("QT_layouts/addFolder.ui", self)

        self.checkBoxes = []

        self.create_checkBoxes()

        self.add_button.clicked.connect(self.add_folder)

    def create_checkBoxes(self):
        passwords_data = self.taking_passwords_from_DB()

        # вывод чекбоксов
        for password_data in passwords_data:
            check_box = QCheckBox(password_data[1])

            self.verticalLayout.addWidget(check_box)

            self.checkBoxes.append(check_box)

    def add_folder(self):
        folder_name = self.name_edit.text()

        client = self.taking_client()

        # сохранение паролей в виде индексов, если выбран чекбокс пустоты,
        # то получится пустая строка
        passwords = []
        if self.empty.isChecked():
            passwords.append("")
        else:
            for check_box in self.checkBoxes:
                if check_box.isChecked():
                    passwords_data = self.taking_passwords_from_DB()

                    for password_data in passwords_data:
                        if password_data[1] == check_box.text():
                            id = password_data[0]
                            passwords.append(str(id))

        # Если название папки не ввел или не выбрал один из чекбоксов,
        # то выведется ошибка
        if folder_name != "" and len(passwords) > 0:
            con = sqlite3.connect("DB files/users.db")

            # взятие папок
            with con:
                folders_data = con.execute("""SELECT * FROM folders""")

            for folder_data in folders_data:
                # проверка на существование папки с таким названием
                if folder_name == folder_data[0]:
                    file = __file__

                    subprocess.run(['python', 'error.py', file])

                    return

            sql = """
                    INSERT INTO folders 
                    (folder_name, passwords, client_login) 
                    values(?, ?, ?)
                    """

            data = [folder_name, " ".join(passwords), client]

            # добавляет папку в БД
            with con:
                con.execute(sql, data)

            sys.exit(app.exec())
        else:
            file = __file__

            subprocess.run(['python', 'error.py', file])

    def taking_client(self):
        # достаем название текущего пользователя/клиента
        with open("DB files/This moment client.txt", mode="r") as f:
            client = f.read()

        return client

    def taking_passwords_from_DB(self):
        client = self.taking_client()

        con = sqlite3.connect("DB files/users.db")
        with con:
            passwords_data = list(con.execute("""SELECT * FROM passwords"""))

        new_passwords_data = []
        for password_data in passwords_data:
            if password_data[-1] == client:
                new_passwords_data.append(password_data)

        return new_passwords_data


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddPasswordWidget()
    ex.show()
    sys.exit(app.exec())
