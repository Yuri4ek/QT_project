import sys

import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog, QCheckBox

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

        # сохранение паролей в виде индексов, если выбран чекбокс пустоты,
        # то получится пустая строка
        passwords = []
        if self.empty.isChecked():
            pass
        else:
            for check_box in self.checkBoxes:
                if check_box.isChecked():
                    passwords_data = self.taking_passwords_from_DB()

                    for password_data in passwords_data:
                        if password_data[1] == check_box.text():
                            id = password_data[0]
                            passwords.append(str(id))

        con = sqlite3.connect("DB files/users.db")

        sql = """
                INSERT INTO folders 
                (folders_name, passwords) 
                values(?, ?)
                """

        data = [folder_name, " ".join(passwords)]

        # добавляет папку в БД
        with con:
            con.execute(sql, data)

        sys.exit(app.exec())

    def taking_passwords_from_DB(self):
        con = sqlite3.connect("DB files/users.db")
        with con:
            passwords_data = list(con.execute("""SELECT * FROM passwords"""))

        return passwords_data


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddPasswordWidget()
    ex.show()
    sys.exit(app.exec())
