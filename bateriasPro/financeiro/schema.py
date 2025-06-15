# api/schemas.py

from pydantic import BaseModel
from typing import Optional
from datetime import date

class PendenciaFinanceiraIn(BaseModel):
    fornecedor: int
    descricao: str
    valor: float
    prazo_pagamento: date
    sucata_prometida_kg: float

class PendenciaFinanceiraOut(BaseModel):
    id: int
    fornecedor: int
    descricao: str
    valor: float
    data_registro: date
    prazo_pagamento: date
    sucata_prometida_kg: float

    class Config:
        from_attributes = True



class FinanceiroIn(BaseModel):
    tipo: str
    valor: float
    descricao: Optional[str] = None
    venda: Optional[int] = None
    pendencia: Optional[int] = None

class FinanceiroOut(BaseModel):
    id: int
    tipo: str
    valor: float
    data: date
    descricao: Optional[str]
    venda: Optional[int]
    pendencia: Optional[int]

    class Config:
        from_attributes = True
