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
                        service_name,
                        login VARCHAR(20),
                        password VARCHAR(20),
                        client_login VARCHAR(10)
                    );
                """)

# удаляет все пароли
with con:
    con.execute("""DELETE FROM passwords""")

# вывод всех паролей
with con:
    data = con.execute("""SELECT * FROM passwords""")
    for row in data:
        print(row)
