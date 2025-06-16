from ninja import Router
from django.shortcuts import get_object_or_404
from decimal import Decimal
from .models import MovimentacaoSucata, EstoqueSucata
from sucata.schema import MovimentacaoSucataIn, MovimentacaoSucataOut
from vendas.models import Venda

router = Router()

@router.post("/movimentacoes_sucata/", response=MovimentacaoSucataOut)
def criar_movimentacao(request, payload: MovimentacaoSucataIn):
    venda_obj = None
    if payload.venda is not None:
        venda_obj = get_object_or_404(Venda, id=payload.venda)

    # Cria a movimentação
    movimentacao = MovimentacaoSucata.objects.create(
        tipo=payload.tipo,
        quantidade_kg=payload.quantidade_kg,
        observacao=payload.observacao,
        venda=venda_obj
    )

    # Atualiza o estoque de sucata
    estoque, created = EstoqueSucata.objects.get_or_create(id=1)
    if movimentacao.tipo.startswith('entrada'):
        estoque.quantidade_kg += movimentacao.quantidade_kg
    elif movimentacao.tipo.startswith('saida'):
        estoque.quantidade_kg -= movimentacao.quantidade_kg

    # Evitar estoque negativo
    if estoque.quantidade_kg < 0:
        raise ValueError("Estoque de sucata não pode ficar negativo.")

    estoque.save()

    return MovimentacaoSucataOut(
        id = movimentacao.id,
        tipo = movimentacao.tipo,
        quantidade_kg=movimentacao.quantidade_kg,
        data = movimentacao.data,
        observacao=movimentacao.observacao,
    )
