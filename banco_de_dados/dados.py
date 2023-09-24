import sqlite3
from sqlite3 import Connection
from typing import Optional

def main(con: Optional[Connection] = None) -> None:
    # Criar um novo banco de dados
    if not con:
        con = sqlite3.connect('dados.db')

    # Criar tabela de Livros
    try:
        con.execute('CREATE TABLE livros (\
                        id INTEGER PRIMARY KEY,\
                        titulo TEXT,\
                        autor TEXT,\
                        editora TEXT,\
                        ano_publicacao INTEGER,\
                        isbn TEXT)')
    except:
        pass

    # Criar tabela de Usuários
    try:
        con.execute('CREATE TABLE usuarios (\
                        id INTEGER PRIMARY KEY,\
                        nome TEXT,\
                        sobrenome TEXT,\
                        endereco TEXT,\
                        email TEXT,\
                        telefone TEXT)')
    except:
        pass

    # Criar tabela de Empréstimo
    try:
        con.execute('CREATE TABLE emprestimos (\
                        id INTEGER PRIMARY KEY,\
                        id_livro INTEGER,\
                        id_usuario INTEGER,\
                        data_emprestimo TEXT,\
                        data_devolucao TEXT,\
                        FOREIGN KEY (id_livro) REFERENCES livros (id),\
                        FOREIGN KEY (id_usuario) REFERENCES usuarios (id))')
    except:
        pass

if __name__ == '__main__':
    main()