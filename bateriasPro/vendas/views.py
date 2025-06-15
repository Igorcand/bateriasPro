# vendas/api.py
from ninja import Router
from vendas.schema import VendaIn, VendaOut
from vendas.service import VendaService
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404
from clientes.models import Cliente
from estoque.models import Bateria
from vendas.models import Carro, ItemVenda, Venda


router = Router()

@router.post("/", response=VendaOut)
def criar_venda(request, payload: VendaIn):
    cliente = get_object_or_404(Cliente, id=payload.cliente)
    carro = get_object_or_404(Carro, id=payload.carro)

    venda = Venda.objects.create(
        cliente=cliente,
        carro=carro,
        sucata_recebida_kg=payload.sucata_recebida_kg,
        desconto_por_sucata=payload.desconto_por_sucata
    )

    itens = []
    for item_data in payload.itens:
        bateria = get_object_or_404(Bateria, id=item_data.bateria)
        item = ItemVenda.objects.create(
            venda=venda,
            bateria=bateria,
            quantidade=item_data.quantidade
        )
        itens.append(item)


    VendaService.processar_venda(venda, itens)

    return VendaOut(
        id=venda.id,
        cliente=venda.cliente.id,
        carro=venda.carro.id,
        sucata_recebida_kg=float(venda.sucata_recebida_kg),
        desconto_por_sucata=float(venda.desconto_por_sucata)
    )