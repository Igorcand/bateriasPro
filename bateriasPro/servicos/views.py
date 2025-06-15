from ninja import Router
from django.shortcuts import get_object_or_404
from .models import Servico
from servicos.schema import ServicoIn, ServicoOut

router = Router()

@router.post("", response=ServicoOut)
def criar_servico(request, payload: ServicoIn):
    servico = Servico.objects.create(
        tipo=payload.tipo,
        preco=payload.preco
    )
    return ServicoOut.from_orm(servico)

@router.get("", response=list[ServicoOut])
def listar_servicos(request):
    servicos = Servico.objects.all()
    return [ServicoOut.from_orm(s) for s in servicos]

@router.get("{servico_id}", response=ServicoOut)
def obter_servico(request, servico_id: int):
    servico = get_object_or_404(Servico, id=servico_id)
    return ServicoOut.from_orm(servico)

@router.put("{servico_id}", response=ServicoOut)
def atualizar_servico(request, servico_id: int, payload: ServicoIn):
    servico = get_object_or_404(Servico, id=servico_id)
    servico.tipo = payload.tipo
    servico.preco = payload.preco
    servico.save()
    return ServicoOut.from_orm(servico)

@router.delete("{servico_id}")
def deletar_servico(request, servico_id: int):
    servico = get_object_or_404(Servico, id=servico_id)
    servico.delete()
    return {"success": True}
