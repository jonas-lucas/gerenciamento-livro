import sqlite3
from sqlite3 import Connection
from typing import Optional
from datetime import date

# Conectar ao banco de dados
def connect() -> Connection:
    con: Connection = sqlite3.connect('dados.db')
    return con

# Função para inserir um novo livro
def insert_book(titulo: str, autor: str, editora: str, ano_publicacao: int, 
                isbn: str, con: Optional[Connection] = None) -> None:
    if not con:
        con = connect()
    con.execute('INSERT INTO \
        livros (titulo, autor, editora, ano_publicacao, isbn) \
            VALUES (?, ?, ?, ?, ?)', (titulo, autor, editora, ano_publicacao, isbn))
    con.commit()
    
# Função para inserir um novo usuário
def insert_user(nome: str, sobrenome: str, endereco: str, email: str, 
                telefone: str, con: Optional[Connection] = None) -> None:
    if not con:
        con = connect()
    con.execute('INSERT INTO \
        usuarios (nome, sobrenome, endereco, email, telefone) \
            VALUES (?, ?, ?, ?, ?)', (nome, sobrenome, endereco, email, telefone))
    con.commit()

# Função para exibir livros
def show_books(con: Optional[Connection] = None) -> None:
    if not con:
        con = connect()
    livros = con.execute('SELECT * FROM livros').fetchall()
    con.close()
    
    if not livros:
        print('Nenhum livro encontrado! :(')
        return
    
    print('Livros na biblioteca: ')
    for livro in livros:
        print(f'ID: {livro[0]}')
        print(f'Título: {livro[1]}')
        print(f'Autor: {livro[2]}')
        print(f'Editora: {livro[3]}')
        print(f'Ano de Publicação: {livro[4]}')
        print(f'ISBN: {livro[5]}')
        print()
        
# Função para realizar empréstimos
def insert_loan(id_livro: int, id_usuario: int, data_emprestimo: date, 
                data_devolucao: Optional[date], con: Optional[Connection] = None) -> None:
    if not con:
        con = connect()
    con.execute('INSERT INTO \
        emprestimos (id_livro, id_usuario, data_emprestimo, data_devolucao) \
            VALUES (?, ?, ?, ?)', (id_livro, id_usuario, str(data_emprestimo), 
                                   str(data_devolucao) if data_devolucao else None))
    con.commit()
    
# Função para exibir os livros emprestados no momento
def show_books_on_loan(con: Optional[Connection] = None) -> list[tuple]:
    if not con:
        con = connect()
    result = con.execute('SELECT \
        emprestimos.id, livros.titulo, usuarios.nome, usuarios.sobrenome, \
        emprestimos.data_emprestimo, emprestimos.data_devolucao \
            FROM livros \
                INNER JOIN emprestimos ON livros.id = emprestimos.id_livro \
                INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario \
                    WHERE emprestimos.data_devolucao IS NULL').fetchall()
    return result

# Função para atualizar a data de devolução de empréstimo
def update_loan_return_date(id_emprestimo: int, data_devolucao: date, con: Optional[Connection] = None) -> None:
    if not con:
        con = connect()
    con.execute('UPDATE emprestimos \
        SET data_devolucao = ? WHERE id = ?', 
            (str(data_devolucao), id_emprestimo))
    con.commit()

if __name__ == '__main__':
    # insert_book('QualityLand', 'Marc-Uwe Kling', 'TusQuest', 2020, '978')
    # insert_user('Jonas', 'Lucas', 'Rua MAANG', 'email@jonas.com', '(85) 9 9999-9999')
    # insert_loan(1, 1, date(2023, 9, 13), None)
    # livros_emprestados = show_books_on_loan()
    # print(livros_emprestados)    
    # update_loan_return_date(3, date(2023, 9, 22))
    # show_books()
    ...
    