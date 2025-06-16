from pydantic import BaseModel
from decimal import Decimal
from typing import Optional
from datetime import date

class MovimentacaoSucataIn(BaseModel):
    tipo: str
    quantidade_kg: Decimal
    observacao: Optional[str] = None
    venda: Optional[int] = None  # id da venda, opcional

class MovimentacaoSucataOut(BaseModel):
    id: int
    tipo: str
    quantidade_kg: Decimal
    data: date
    observacao: Optional[str] = None

    class Config:
        from_attributes = True
