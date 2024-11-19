import sqlite3 as sql

con = sql.connect("users.db")

# создает таблицу паролей
with con:
    data = con.execute("""SELECT count(*) FROM sqlite_master 
                        WHERE type='table' and name='passwords'""")
    for row in data:
        if row[0] == 0:
            with con:
                con.execute("""
                    CREATE TABLE passwords 
                    (
                        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                        service_name,
                        login VARCHAR(20),
                        password VARCHAR(20),
                        client_login VARCHAR(10)
                    );
                """)

# удаляет все пароли
with con:
    con.execute("""DELETE FROM passwords""")

sql = """INSERT INTO passwords 
        (service_name, login, password, client_login) values(?, ?, ?, ?)"""

data = ("service_name", "login", "password", "admin",)

# добавляет пароль админа
with con:
    con.execute(sql, data)

data = (("майнкрафт", "yurik", "1234", "yurik",),
        ("степик", "yurik", "1234", "yurik",),
        ("гугл", "yurik", "1234", "yurik",),
        ("телеграмм", "89083062970", "1234", "yurik",),
        ("яндекс", "yura09antonov", "1234", "yurik",),)

# добавляет пароли Юрика
with con:
    for small_data in data:
        con.execute(sql, small_data)

# вывод всех паролей
with con:
    data = con.execute("""SELECT * FROM passwords""")
    for row in data:
        print(row)
