from ninja import Router
from django.shortcuts import get_object_or_404
from .models import Manutencao
from clientes.models import Cliente
from estoque.models import Bateria
from manutencao.schema import ManutencaoIn, ManutencaoOut

router = Router()

@router.post("", response=ManutencaoOut)
def criar_manutencao(request, payload: ManutencaoIn):
    cliente = get_object_or_404(Cliente, id=payload.cliente)
    bateria = None
    if payload.bateria:
        bateria = get_object_or_404(Bateria, id=payload.bateria)
    manutencao = Manutencao.objects.create(
        cliente=cliente,
        bateria=bateria,
        status=payload.status,
        data_saida=payload.data_saida,
        codigo_unico=payload.codigo_unico
    )
    return ManutencaoOut(
        id = manutencao.id,
        cliente = cliente.id,
        bateria = bateria.id if bateria else None,
        status = manutencao.status,
        data_entrada=manutencao.data_entrada,
        data_saida=manutencao.data_saida,
        codigo_unico=manutencao.codigo_unico
    )

@router.get("", response=list[ManutencaoOut])
def listar_manutencoes(request):
    manutencoes = Manutencao.objects.all()
    return [ManutencaoOut.from_orm(m) for m in manutencoes]

@router.get("{manutencao_id}", response=ManutencaoOut)
def obter_manutencao(request, manutencao_id: int):
    manutencao = get_object_or_404(Manutencao, id=manutencao_id)
    return ManutencaoOut.from_orm(manutencao)

@router.put("{manutencao_id}", response=ManutencaoOut)
def atualizar_manutencao(request, manutencao_id: int, payload: ManutencaoIn):
    manutencao = get_object_or_404(Manutencao, id=manutencao_id)
    manutencao.cliente = get_object_or_404(Cliente, id=payload.cliente)
    manutencao.bateria = get_object_or_404(Bateria, id=payload.bateria) if payload.bateria else None
    manutencao.status = payload.status
    manutencao.data_saida = payload.data_saida
    manutencao.codigo_unico = payload.codigo_unico
    manutencao.save()
    return ManutencaoOut.from_orm(manutencao)

@router.delete("{manutencao_id}")
def deletar_manutencao(request, manutencao_id: int):
    manutencao = get_object_or_404(Manutencao, id=manutencao_id)
    manutencao.delete()
    return {"success": True}
