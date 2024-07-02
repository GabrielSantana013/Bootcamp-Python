import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "clientes.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

# def criar_tabela(cursor, conexao):
#     cursor.execute("CREATE TABLE clientes (Id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")
#     conexao.commit()

# data = ("cleitom", "cleitola@gmail.com")

# def inserir_registro(cursor, conexao, nome, email):
#     data = (nome, email)
#     cursor.execute("INSERT INTO clientes (nome, email) VALUES(?, ?);", data)
#     conexao.commit()

# def atualizar_registro(cursor, conexao, nome, email, id):
#     data = (nome, email, id)    
#     cursor.execute("UPDATE clientes SET nome=?, email = ? WHERE id =?;", data)
#     conexao.commit()

# def excluir_registro(cursor,conexao,id):
#     data = (id, )
#     cursor.execute("DELETE FROM clientes WHERE id=?;", data)
#     conexao.commit()

# def inserir_muitos(conexao, cursor, dados):
#     cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?);", dados)
#     conexao.commit()

# def recuperar_cliente(cursor, id):
#     cursor.row_factory = sqlite3.Row
#     cursor.execute("SELECT * FROM clientes WHERE id = ?;", (id, ))
#     return cursor.fetchone()

# def listar_clientes(cursor):
#     return cursor.execute("SELECT * FROM clientes ORDER BY id DESC;")
    
# clientes = listar_clientes(cursor)
# for cliente in clientes:
#     print(dict(cliente))

# cliente = recuperar_cliente(cursor, 1)
# print(dict(cliente))
# print(cliente["id"], cliente["nome"], cliente["email"])

# print(f'seja bem vindo cliente {cliente["nome"]}')

# dados = [
#     ("Gabriel", "teste@gmail.com"),
#     ("luan", "gameplay@gmail.com"),
#     ("Dj", "andremarques@gmail.com"),
# ]

#inserir_muitos(conexao,cursor,dados)
#excluir_registro(cursor, conexao, 2)
#atualizar_registro(cursor, conexao, "Gabas Santana", "gabasreidelas@gmail.com", 1)

#=========================================================================================
#Aula Transação
#=========================================================================================

try:
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", ("Teste3", "Teste3@gmail.com"))
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?,?,?)", (1, "Teste4", "Teste4@gmail.com"))
    conexao.commit()
except Exception as error:
    print(f"Ops!, um erro ocorreu: {error}")
    conexao.rollback()
finally:
    conexao.commit()