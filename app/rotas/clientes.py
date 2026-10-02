from fastapi import APIRouter

from app.models.cliente import Cliente

# Cria um grupo de rotas. (serve para organizar as rotas)
router = APIRouter(
    prefix="/clientes"
)

CLIENT_LIST = [Cliente(id_=1, nome="Eduardo", email="teste@gmail.com", telefone="123456789"),
                    Cliente(id_=2, nome="Ste", email="2@gmail.com", telefone="123456789")]

@router.get("/", response_model=list[Cliente]) # Quando acesso essa rota
async def listar_clientes():
    return CLIENT_LIST

                            # A resposta será um objeto cliente ou None se não tiver nada
@router.get("/{cliente_id}", response_model=Cliente | None)
async def obter_cliente(cliente_id: int):
    for cliente in CLIENT_LIST:
        if cliente.id_ == cliente_id:
            return cliente

    return None