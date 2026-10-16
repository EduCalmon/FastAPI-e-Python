from fastapi import Depends
from typing import Annotated

from app.banco_de_dados.local import BancoDeDadosLocal
from app.banco_de_dados.cliente_repositorio import ClienteRepositorio


banco_de_dados = BancoDeDadosLocal()


def obter_banco_de_dados() -> BancoDeDadosLocal:
    return banco_de_dados

def obter_cliente_repositorio(
        banco_de_dados_local: 
        Annotated[BancoDeDadosLocal, # Variável do tipo banco de dados local
                  Depends(obter_banco_de_dados)] # executa se estiver dentro do contexto do fastAPI
        ) -> ClienteRepositorio:
    return ClienteRepositorio(banco_de_dados_local)