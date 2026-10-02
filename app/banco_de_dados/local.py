import sqlite3
from contextlib import contextmanager

class BancoDeDadosLocal():
    def __init__(self,nome_do_arquivo='techlog.db'):
        self.nome_do_arquivo = nome_do_arquivo
        self.inicializar_banco()

    @contextmanager
    def conectar(self):
        conexao = sqlite3.connect(self.nome_do_arquivo)
        try:
            yield conexao
            conexao.commit()
        except Exception as e:
            conexao.rollback()
            raise e
        finally:
            conexao.close()

    def inicializar_banco(self):
        with self.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS clientes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    telefone TEXT NOT NULL
                """
            )
            conexao.commit()