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
                        client_id INTEGER
                    );
                """)

# удаляет все папки
with con:
    con.execute("""DELETE FROM folders""")

# находит и записывает id админа
with con:
    admin_id = list(con.execute("""
                                SELECT id FROM clients WHERE login='admin' 
                    """))[0][0]

sql = f"""SELECT id FROM passwords WHERE client_id='{admin_id}' """

# находит и записывает пароли админа
with con:
    admin_passwords_id = " ".join(list(map(str, list(con.execute(sql))[0])))

sql = """INSERT INTO folders 
        (folder_name, passwords, client_id) values(?, ?, ?)"""

data = ("folder", admin_passwords_id, admin_id,)

# добавляет папку админа
with con:
    con.execute(sql, data)

# находит и записывает id Юрика
with con:
    yurik_id = list(con.execute("""
                                SELECT id FROM clients WHERE login='yurik' 
                    """))[0][0]

sql = f"""SELECT id FROM passwords WHERE client_id='{yurik_id}' """

# находит и записывает пароли Юрика
with con:
    yurik_passwords_id = []
    for id in con.execute(sql):
        yurik_passwords_id.append(str(*id))
    yurik_passwords_id = " ".join(yurik_passwords_id)

data = (("игры", yurik_passwords_id, yurik_id,),
        ("аккаунты", yurik_passwords_id, yurik_id,),
        ("общение", yurik_passwords_id, yurik_id,),)

sql = """INSERT INTO folders 
        (folder_name, passwords, client_id) values(?, ?, ?)"""

# добавляет папки Юрика
with con:
    for small_data in data:
        con.execute(sql, small_data)

# вывод всех папок
with con:
    data = con.execute("""SELECT * FROM folders""")
    for row in data:
        print(row)
