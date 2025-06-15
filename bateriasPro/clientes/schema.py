from pydantic import BaseModel
from typing import Optional

class ClienteIn(BaseModel):
    nome: str
    telefone: Optional[str] = None
    email: Optional[str] = None
    cpf: Optional[str] = None

class ClienteOut(BaseModel):
    id: int
    nome: str
    telefone: Optional[str]
    email: Optional[str]
    cpf: Optional[str]

    class Config:
        orm_mode = True
