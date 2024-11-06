import sqlite3 as sql

con = sql.connect("users.db")

# создает бд если его нет
with con:
    data = con.execute(
        "select count(*) from sqlite_master where type='table' and name='clients'")
    for row in data:
        if row[0] == 0:
            with con:
                con.execute("""
                    CREATE TABLE clients 
                    (
                        f_name VARCHAR(20),
                        l_name VARCHAR(20),
                        login VARCHAR(10) UNIQUE,
                        password VARCHAR(20)
                    );
                """)

sql = "INSERT INTO clients (f_name, l_name, login, password) values(?, ?, ?, ?)"

data = ("Админ", "Админов", "admin", "1234",)

# добавляет админа (если он уже есть, то выведется ошибка)
with con:
    con.execute(sql, data)

# вывод всех пользователей и их данных
with con:
    data = con.execute("SELECT * FROM clients")
    for row in data:
        print(row)
