# PYTHON Y LAS BASES DE DATOS

import sqlite3

con = sqlite3.connect("miaplicacion.db")
cur = con.cursor()

# Crear una tabla:
cur.execute('''CREATE TABLE users
            (id INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL)
            ''')

# Insertar una fila de datos:
cur.execute('''INSERT INTO users(id, username, password)
            VALUES (1, 'vroman', 'miclave')
            ''')
cur.execute('''INSERT INTO users(id, username, password)
            VALUES (2, 'usuario', 'clave')
            ''')
rows = cur.execute('SELECT * FROM users')
for row in rows:
    print(row)

cur.close()
con.commit()
con.close()