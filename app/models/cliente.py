from pydantic import BaseModel

class Cliente(BaseModel): # Consigo converter Json para objeto, ou Objeto para Json
    id_: int
    nome: str
    email: str
    telefone: str