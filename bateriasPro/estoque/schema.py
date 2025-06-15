from pydantic import BaseModel
from typing import Optional


class MarcaIn(BaseModel):
    nome: str

class MarcaOut(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes = True



class BateriaIn(BaseModel):
    marca: int
    modelo: str
    amperagem: int
    peso_kg: float
    quantidade_em_estoque: int

class BateriaOut(BaseModel):
    id: int
    marca: MarcaOut
    modelo: str
    amperagem: int
    peso_kg: float
    quantidade_em_estoque: int

    class Config:
        from_attributes = True


