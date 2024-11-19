import sqlite3 as sql

con = sql.connect("users.db")

# создает таблицу папок
with con:
    data = con.execute("""SELECT count(*) FROM sqlite_master 
                        WHERE type='table' and name='folders'""")
    for row in data:
        if row[0] == 0:
            with con:
                con.execute("""
                    CREATE TABLE folders 
                    (
                        folder_name,
                        passwords VARCHAR(1000),
                        client_login
                    );
                """)

# удаляет все папки
with con:
    con.execute("""DELETE FROM folders""")

sql = """INSERT INTO folders 
        (folder_name, passwords, client_login) values(?, ?, ?)"""

data = ("folder", "1", "admin",)

# добавляет папку админа
with con:
    con.execute(sql, data)

data = (("игры", "8", "yurik",),
        ("аккаунты", "10 12", "yurik",),
        ("общение", "8 9 10 11 12", "yurik",),)

# добавляет папки Юрика
with con:
    for small_data in data:
        con.execute(sql, small_data)

# вывод всех папок
with con:
    data = con.execute("""SELECT * FROM folders""")
    for row in data:
        print(row)
