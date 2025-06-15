from pydantic import BaseModel, Field
from decimal import Decimal

class ServicoIn(BaseModel):
    tipo: str = Field(..., max_length=20)
    preco: Decimal

class ServicoOut(BaseModel):
    id: int
    tipo: str
    preco: Decimal

    class Config:
        from_attributes = True
