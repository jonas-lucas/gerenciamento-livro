import sqlite3
from sqlite3 import Connection
from typing import Optional

# Conectar ao banco de dados
def connect() -> Connection:
    con: Connection = sqlite3.connect('dados.db')
    return con

# Função para inserir um novo livro
def insert_book(titulo: str, autor: str, editora: str, ano_publicacao: int, isbn: str, con: Optional[Connection] = None) -> None:
    if not con:
        con = connect()
    con.execute('INSERT INTO \
        livros (titulo, autor, editora, ano_publicacao, isbn) \
            VALUES (?, ?, ?, ?, ?)', (titulo, autor, editora, ano_publicacao, isbn))
    
# Função para inserir um novo usuário
def insert_user(nome: str, sobrenome: str, endereco: str, email: str, telefone: str, con: Optional[Connection] = None) -> None:
    if not con:
        con = connect()
    con.execute('INSERT INTO \
        usuarios (nome, sobrenome, endereco, email, telefone) \
            VALUES (?, ?, ?, ?, ?)', (nome, sobrenome, endereco, email, telefone))

if __name__ == '__main__':
    # insert_book('QualityLand', 'Marc-Uwe Kling', 'TusQuest', 2020, '978')
    insert_user('Jonas', 'Lucas', 'Rua MAANG', 'email@jonas.com', '(85) 9 9999-9999')