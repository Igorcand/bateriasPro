# vendas/api.py
from ninja import Router
from vendas.schema import VendaIn, VendaOut
from vendas.service import VendaService
from ninja.errors import HttpError

router = Router()

@router.post("/", response=VendaOut)
def criar_venda(request, data: VendaIn):
    try:
        venda = VendaService.criar_venda_com_itens_e_processar(
            {
                "cliente_id": data.cliente,
                "carro_id": data.carro,
                "sucata_recebida_kg": data.sucata_recebida_kg,
                "desconto_por_sucata": data.desconto_por_sucata
            },
            [
                {"bateria_id": item.bateria, "quantidade": item.quantidade}
                for item in data.itens
            ]
        )
        return venda
    except ValueError as e:
        raise HttpError(400, str(e))
