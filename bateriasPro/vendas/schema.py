# vendas/schemas.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class ItemVendaIn(BaseModel):
    bateria: int
    quantidade: int

class VendaIn(BaseModel):
    cliente: int
    carro: int
    sucata_recebida_kg: float
    desconto_por_sucata: float
    itens: List[ItemVendaIn]

class VendaOut(BaseModel):
    id: int
    cliente: int
    carro: int
    data: date
    sucata_recebida_kg: float
    desconto_por_sucata: float
