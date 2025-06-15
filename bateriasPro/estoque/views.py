from ninja import Router
from django.shortcuts import get_object_or_404

from estoque.schema import (
    MarcaIn, MarcaOut,
    BateriaIn, BateriaOut
)
from estoque.models import Marca, Bateria

router = Router()


@router.post("/marcas/", response=MarcaOut)
def criar_marca(request, payload: MarcaIn):
    marca = Marca.objects.create(**payload.dict())
    return MarcaOut.from_orm(marca)

@router.get("/marcas/", response=list[MarcaOut])
def listar_marcas(request):
    marcas = Marca.objects.all()
    return [MarcaOut.from_orm(m) for m in marcas]

@router.get("/marcas/{marca_id}", response=MarcaOut)
def obter_marca(request, marca_id: int):
    marca = get_object_or_404(Marca, id=marca_id)
    return MarcaOut.from_orm(marca)

@router.put("/marcas/{marca_id}", response=MarcaOut)
def atualizar_marca(request, marca_id: int, payload: MarcaIn):
    marca = get_object_or_404(Marca, id=marca_id)
    marca.nome = payload.nome
    marca.save()
    return MarcaOut.from_orm(marca)

@router.delete("/marcas/{marca_id}")
def deletar_marca(request, marca_id: int):
    marca = get_object_or_404(Marca, id=marca_id)
    marca.delete()
    return {"success": True}


@router.post("/baterias/", response=BateriaOut)
def criar_bateria(request, payload: BateriaIn):
    marca_obj = get_object_or_404(Marca, id=payload.marca)
    bateria = Bateria.objects.create(
        marca=marca_obj,
        modelo=payload.modelo,
        amperagem=payload.amperagem,
        peso_kg=payload.peso_kg,
        quantidade_em_estoque=payload.quantidade_em_estoque,
    )
    return BateriaOut.from_orm(bateria)

@router.get("/baterias/", response=list[BateriaOut])
def listar_baterias(request):
    baterias = Bateria.objects.select_related("marca").all()
    return [BateriaOut.from_orm(b) for b in baterias]

@router.get("/baterias/{bateria_id}", response=BateriaOut)
def obter_bateria(request, bateria_id: int):
    bateria = get_object_or_404(Bateria.objects.select_related("marca"), id=bateria_id)
    return BateriaOut.from_orm(bateria)

@router.put("/baterias/{bateria_id}", response=BateriaOut)
def atualizar_bateria(request, bateria_id: int, payload: BateriaIn):
    bateria = get_object_or_404(Bateria, id=bateria_id)
    for attr, value in payload.dict().items():
        setattr(bateria, attr, value)
    bateria.save()
    return BateriaOut.from_orm(bateria)

@router.delete("/baterias/{bateria_id}")
def deletar_bateria(request, bateria_id: int):
    bateria = get_object_or_404(Bateria, id=bateria_id)
    bateria.delete()
    return {"success": True}
