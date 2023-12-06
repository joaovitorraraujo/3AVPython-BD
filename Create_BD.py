import sqlite3 as lite

con = lite.connect('DataBase.db')

with con:
    cur = con.cursor()
    cur.execute("""
            CREATE TABLE Usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome TEXT NOT NULL, 
                cpf TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE, 
                senha TEXT NOT NULL)""")

with con:
    cur = con.cursor()
    cur.execute("""
            CREATE TABLE Categoria (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome TEXT, 
                id_usuario INTEGER, 
                FOREIGN KEY (id_usuario) REFERENCES Usuario(id))""")

with con:
    cur = con.cursor()
    cur.execute("""
            CREATE TABLE Receita (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                categoria TEXT, 
                valor DECIMAL(15, 2),
                data DATE, 
                id_usuario INTEGER,
                FOREIGN KEY (id_usuario) REFERENCES Usuario(id))""")

with con:
    cur = con.cursor()
    cur.execute("""
            CREATE TABLE Despesa (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                categoria TEXT, 
                valor DECIMAL(15, 2),
                data DATE, 
                id_usuario INTEGER,
                FOREIGN KEY (id_usuario) REFERENCES Usuario(id))""")

