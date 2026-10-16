from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated

from app.models.cliente import Cliente
from app.banco_de_dados.cliente_repositorio import ClienteRepositorio
from app.depends import obter_cliente_repositorio

# Cria um grupo de rotas. (serve para organizar as rotas)
router = APIRouter(
    prefix="/clientes"
)

CLIENT_LIST = [Cliente(id_=1, nome="Eduardo", email="teste@gmail.com", telefone="123456789"),
                    Cliente(id_=2, nome="Ste", email="2@gmail.com", telefone="123456789")]

@router.get("/", response_model=list[Cliente]) # Quando acesso essa rota
async def listar_clientes(cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)]):
    return await cliente_repositorio.listar_clientes()

                            # A resposta será um objeto cliente ou None se não tiver nada
@router.get("/{cliente_id}", response_model=Cliente | None)
async def obter_cliente(cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)],
                        cliente_id: int):

    cliente = await cliente_repositorio.obter_cliente(cliente_id)

    if not cliente:
        # Quando dá erro HTTP 404 ele mostra uma mensagem
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    return cliente