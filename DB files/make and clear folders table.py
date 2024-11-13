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
                        folders_name,
                        passwords VARCHAR(1000)
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
