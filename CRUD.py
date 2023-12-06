import sqlite3 as lite
from decimal import Decimal  
import pandas as pd

con = lite.connect('DataBase.db')

# FUNÇOES INSERIR ===============================================================================

# inserir usuario
def insert_usuario(dados):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Usuario (nome, cpf, email, senha) VALUES (?, ?, ?, ?)"
        cur.execute(query, dados)
        last_id = cur.lastrowid  # Obtendo o último ID inserido
        return last_id

# inserir categoria
def insert_category(nome, id_usuario):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Categoria (nome, id_usuario) VALUES(?, ?)"
        cur.execute(query,(nome, id_usuario))
        
# inserir receita
def insert_revenue(categoria, valor, data, id_usuario):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Receita (categoria, valor, data, id_usuario) VALUES (?, ?, ?, ?)"
        cur.execute(query,(categoria, valor, data, id_usuario))

# inserir despesa
def insert_expense(categoria, valor, data, id_usuario):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Despesa (categoria, valor, data, id_usuario) VALUES (?, ?, ?, ?)"
        cur.execute(query, (categoria, valor, data, id_usuario))
# FUNÇÃO PARA ALTERAR OS DADOS DO USUARIO==============================

def update_data_user(novo_nome, cpf, email, senha, id):
    with con:
        cur = con.cursor()
        cur.execute("UPDATE Usuario SET nome=?, cpf=?, email=?, senha=? WHERE id=?", (novo_nome, cpf, email, senha, id))
        con.commit()
        
# FUNÇOES DELETAR ==========================================================================================================================

# Deletar receitas
def delete_revenue(id, id_usuario):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Receita WHERE id=? AND id_usuario=?"
        cur.execute(query,(id, id_usuario))
        
# Deletar categoria
def delete_category(nome, id_usuario):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Categoria WHERE nome=? AND id_usuario=?"
        cur.execute(query,(nome, id_usuario))
        
# Deletar despesas
def delete_expense(id, id_usuario):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Despesa WHERE id=? AND id_usuario=?"
        cur.execute(query,(id, id_usuario))
        
# FUNÇOES VERIFICAR DADOS EXISTENTES===============================================================================
def check_user_password_recover(nome,cpf,email):
    con = lite.connect('DataBase.db')  
    cur = con.cursor()

    cur.execute("SELECT * FROM Usuario WHERE nome=? AND cpf=? AND email=?", (nome,cpf,email))
    user_id = cur.fetchone()  # Retorna uma tupla com o ID do usuário ou None se não houver correspondência
    
    con.close()  

    return user_id

def check_user_password(email, senha):
    con = lite.connect('DataBase.db')  
    cur = con.cursor()

    cur.execute("SELECT * FROM Usuario WHERE email=? AND senha=?", (email, senha))
    user_id = cur.fetchone()  # Retorna uma tupla com o ID do usuário ou None se não houver correspondência
    
    con.close()  

    return user_id

def check_user_register(nome):
    con = lite.connect('DataBase.db')  
    cur = con.cursor()

    cur.execute("SELECT * FROM Usuario WHERE nome=?", (nome,))
    user = cur.fetchone()  # Retorna uma tupla ou None se não houver correspondência

    con.close()  

    return user

def check_cpf_register(cpf):
    con = lite.connect('DataBase.db')  
    cur = con.cursor()

    cur.execute("SELECT * FROM Usuario WHERE cpf=?", (cpf,))
    user = cur.fetchone()  # Retorna uma tupla ou None se não houver correspondência

    con.close()  

    return user

def check_email_register(email):
    con = lite.connect('DataBase.db')  
    cur = con.cursor()

    cur.execute("SELECT * FROM Usuario WHERE email=?", (email,))
    user = cur.fetchone()  # Retorna uma tupla ou None se não houver correspondência

    con.close()  

    return user

def check_category(nome,id_usuario):
    con = lite.connect('DataBase.db')  
    cur = con.cursor()

    cur.execute("SELECT * FROM Categoria WHERE nome=? AND id_usuario=?", (nome,id_usuario))
    user = cur.fetchone()  # Retorna uma tupla ou None se não houver correspondência

    con.close()  

    return user


# FUNÇÃO PARA BUSCAR CATEGORIAS=====================================
def view_category_search(item, id_usuario):
    list_items = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria WHERE nome LIKE ? AND id_usuario = ?", (f'{item}%', id_usuario))
        row = cur.fetchall()
        for r in row:
            list_items.append(r)
            
        return list_items


# FUNÇOES VER DADOS NO MENU PRINCIPAL===============================================================================

# ver categoria
def view_category(id_usuario):
    list_items = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Categoria WHERE id_usuario=?",(id_usuario,))
        row = cur.fetchall()
        for r in row:
            list_items.append(r)
            
        return list_items
    
# ver receitas
def view_revenue(id_usuario):
    list_items = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Receita WHERE id_usuario=?",(id_usuario,))
        row = cur.fetchall()
        for r in row:
            list_items.append(r)
            
        return list_items

# ver despesas
def view_expense(id_usuario):
    list_items = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Despesa WHERE id_usuario=?",(id_usuario,))
        row = cur.fetchall()
        for r in row:
            list_items.append(r)
            
        return list_items

# dados da tabela
def table(id_usuario):
    expense = view_expense(id_usuario)
    revenue = view_revenue(id_usuario)
    
    table_list = []
    
    for i in expense:
        table_list.append(i[:4])
        
    for i in revenue:
        table_list.append(i[:4])
        
    return table_list

# dados do grafico de barra
def bar_values(id_usuario):
    # receita total
    revenue = view_revenue(id_usuario)[:4]
    revenue_list_bar = []
    
    for i in revenue:
        revenue_list_bar.append(i[2]) 
    
    revenue_total = sum(revenue_list_bar)
    
    # Despesas totais
    expense = view_expense(id_usuario)[:4]
    expense_list_bar = []
    
    for i in expense:
        expense_list_bar.append(i[2]) 
    
    expense_total = sum(expense_list_bar)
        
    # Saldo total
    saldo_total =revenue_total - expense_total
    
    return[revenue_total,expense_total,saldo_total]

def pie_valores(id_usuario):
    expense = view_expense(id_usuario)
    
    table_list = []
    
    for i in expense:
        table_list.append(i)
        
    dataframe = pd.DataFrame(table_list, columns=['id', 'categoria', 'valor', 'data', 'id_usuario'])
    dataframe = dataframe.groupby('categoria')['valor'].sum() 
    
    list_values = dataframe.values.tolist()
    list_category = []
    
    for i in dataframe.index:
        list_category.append(i)
        
    return [list_category, list_values]

def porcentagem_value(id_usuario):
    # receita total
    revenue = view_revenue(id_usuario)
    revenue_list = []
    
    for i in revenue:
        revenue_list.append(i[2])
        
    revenue_total = sum(revenue_list)
    
    # despesa total
    expense = view_expense(id_usuario)
    expense_list = []
    
    for i in expense:
        expense_list.append(i[2])
        
    expense_total = sum(expense_list)
    
    # total
    if not revenue_total == 0:
        total = ((revenue_total - expense_total)/revenue_total)*100
    else:
        total = 0
    
    return[total]
    
    
