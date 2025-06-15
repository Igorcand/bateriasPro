from pydantic import BaseModel
from typing import Optional

class FornecedorIn(BaseModel):
    nome: str
    cnpj: Optional[str] = None
    telefone: Optional[str] = None

class FornecedorOut(BaseModel):
    id: int
    nome: str
    cnpj: Optional[str]
    telefone: Optional[str]

    class Config:
        from_attributes = True
