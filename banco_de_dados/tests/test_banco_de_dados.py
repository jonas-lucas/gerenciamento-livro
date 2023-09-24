import unittest
import sqlite3
from ..dados import main
from ..view import insert_book, insert_user

class TestBancoDeDados(unittest.TestCase):
    
    def setUp(self):
        # Crie um banco de dados temporário em memória para os testes
        self.con = sqlite3.connect(':memory:')
        self.cursor = self.con.cursor()
        
        # Execute a função main para criar as tabelas
        main(self.con)
    
    def tearDown(self):
        # Feche a conexão com o banco de dados
        self.con.close()


class TestTabelas(TestBancoDeDados):
    def colunas(self, tabela: str) -> list[str]:
        """Retorna as colunas presentes em uma tabela."""
        self.cursor.execute(f'PRAGMA table_info({tabela});')
        return list(map(lambda x: x[1], self.cursor.fetchall()))
    
    def test_table_livros(self):
        colunas_criadas: list[str] = self.colunas('livros')
        colunas_desejadas: list[str] = ['id', 'titulo', 'autor', 'editora', 'ano_publicacao', 'isbn']
        self.assertEqual(sorted(colunas_desejadas), sorted(colunas_criadas))
            
    def test_table_usuarios(self):
        colunas_criadas: list[str] = self.colunas('usuarios')
        colunas_desejadas: list[str] = ['id', 'nome', 'sobrenome', 'endereco', 'email', 'telefone']
        self.assertEqual(sorted(colunas_desejadas), sorted(colunas_criadas))
        
    def test_table_emprestimos(self):
        colunas_criadas: list[str] = self.colunas('emprestimos')
        colunas_desejadas: list[str] = ['id', 'id_livro', 'id_usuario', 'data_emprestimo', 'data_devolucao']
        self.assertEqual(sorted(colunas_desejadas), sorted(colunas_criadas))


class TestInserirValores(TestBancoDeDados):
    def setUp(self):
        super().setUp()

        insert_book('QualityLand', 'Marc-Uwe Kling', 'TusQuest', 2020, '978', self.con)
        insert_user('Jonas', 'Lucas', 'Rua MAANG', 'email@jonas.com', '(85) 9 9999-9999', self.con)
        
    def test_livro(self):
        self.cursor.execute('SELECT * FROM livros WHERE titulo=?', ('QualityLand',))
        livro: tuple = self.cursor.fetchone()
        
        self.assertEqual(livro[1], 'QualityLand')
        self.assertEqual(livro[2], 'Marc-Uwe Kling')
        self.assertEqual(livro[3], 'TusQuest')
        self.assertEqual(livro[4], 2020)
        self.assertEqual(livro[5], '978')
        
    def test_usuario(self):
        self.cursor.execute('SELECT * FROM usuarios WHERE nome=?', ('Jonas',))
        usuario: tuple = self.cursor.fetchone()
        
        self.assertEqual(usuario[1], 'Jonas')
        self.assertEqual(usuario[2], 'Lucas')
        self.assertEqual(usuario[3], 'Rua MAANG')
        self.assertEqual(usuario[4], 'email@jonas.com')
        self.assertEqual(usuario[5], '(85) 9 9999-9999')

if __name__ == '__main__':
    unittest.main()
