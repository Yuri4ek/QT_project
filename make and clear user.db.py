import sqlite3 as sql

con = sql.connect("users.db")

# создает базу данных пользователей если его нет
with con:
    data = con.execute("""SELECT count(*) FROM sqlite_master 
                        WHERE type='table' and name='clients'""")
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

# удаляет всех клиентов
with con:
    con.execute("""DELETE FROM clients""")

sql = """INSERT INTO clients 
        (f_name, l_name, login, password) values(?, ?, ?, ?)"""

data = ("Админ", "Админов", "admin", "1234",)

# добавляет админа
with con:
    con.execute(sql, data)

# вывод всех пользователей и их данных
with con:
    data = con.execute("""SELECT * FROM clients""")
    for row in data:
        print(row)
