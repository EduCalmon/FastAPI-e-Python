from app.banco_de_dados.local import BancoDeDadosLocal
from app.models.cliente import Cliente

class ClienteRepositorio:
    def __init__(self, banco_de_dados: BancoDeDadosLocal):
        self.db = banco_de_dados