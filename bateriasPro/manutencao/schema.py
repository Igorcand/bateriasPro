from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class ManutencaoIn(BaseModel):
    cliente: int
    bateria: Optional[int] = None
    status: Optional[str] = 'analise'
    data_saida: Optional[date] = None
    codigo_unico: str

class ManutencaoOut(BaseModel):
    id: int
    cliente: int
    bateria: Optional[int] = None
    status: str
    data_entrada: date
    data_saida: Optional[date]
    codigo_unico: str

    class Config:
        from_attributes = True
