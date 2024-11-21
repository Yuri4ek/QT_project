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
                        client_id INTEGER
                    );
                """)

# удаляет все пароли
with con:
    con.execute("""DELETE FROM passwords""")

sql = """INSERT INTO passwords 
        (service_name, login, password, client_id) values(?, ?, ?, ?)"""

# находит и записывает id админа
with con:
    admin_id = list(con.execute("""
                                SELECT id FROM clients WHERE login='admin' 
                    """))[0][0]

data = ("service_name", "login", "password", admin_id,)

# добавляет пароль админа
with con:
    con.execute(sql, data)

# находит и записывает id Юрика
with con:
    yurik_id = list(con.execute("""
                                SELECT id FROM clients WHERE login='yurik' 
                    """))[0][0]

data = (("майнкрафт", "yurik", "1234", yurik_id,),
        ("степик", "yurik", "1234", yurik_id,),
        ("гугл", "yurik", "1234", yurik_id,),
        ("телеграмм", "89083062970", "1234", yurik_id,),
        ("яндекс", "yura09antonov", "1234", yurik_id,),)

# добавляет пароли Юрика
with con:
    for small_data in data:
        con.execute(sql, small_data)

# вывод всех паролей
with con:
    data = con.execute("""SELECT * FROM passwords""")
    for row in data:
        print(row)
