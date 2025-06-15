from ninja import Router



from financeiro.schema import (
    PendenciaFinanceiraIn, PendenciaFinanceiraOut,
    FinanceiroIn, FinanceiroOut,
)
from fornecedores.models import Fornecedor
from vendas.models import Venda
from financeiro.models import PendenciaFinanceira, Financeiro
from django.shortcuts import get_object_or_404
from ninja.errors import HttpError

router = Router()


@router.post("/pendencias/", response=PendenciaFinanceiraOut)
def criar_pendencia(request, payload: PendenciaFinanceiraIn):
    fornecedor = get_object_or_404(Fornecedor, id=payload.fornecedor)
    pendencia = PendenciaFinanceira.objects.create(
        fornecedor=fornecedor,
        descricao=payload.descricao,
        valor=payload.valor,
        prazo_pagamento=payload.prazo_pagamento,
        sucata_prometida_kg=payload.sucata_prometida_kg
    )
    return PendenciaFinanceiraOut(
        id=pendencia.id,
        fornecedor=pendencia.fornecedor.id,
        descricao=pendencia.descricao,
        valor=pendencia.valor,
        data_registro=pendencia.data_registro,
        prazo_pagamento=pendencia.prazo_pagamento,
        sucata_prometida_kg=pendencia.sucata_prometida_kg,
    )
@router.get("/pendencias/", response=list[PendenciaFinanceiraOut])
def listar_pendencias(request):
    pendencias = PendenciaFinanceira.objects.all()
    return [PendenciaFinanceiraOut(
        id=pendencia.id,
        fornecedor=pendencia.fornecedor.id,
        descricao=pendencia.descricao,
        valor=pendencia.valor,
        data_registro=pendencia.data_registro,
        prazo_pagamento=pendencia.prazo_pagamento,
        sucata_prometida_kg=pendencia.sucata_prometida_kg,
    ) for pendencia in pendencias]

@router.get("/pendencias/{pendencia_id}", response=PendenciaFinanceiraOut)
def obter_pendencia(request, pendencia_id: int):
    pendencia = get_object_or_404(PendenciaFinanceira, id=pendencia_id)
    return PendenciaFinanceiraOut(
        id=pendencia.id,
        fornecedor=pendencia.fornecedor.id,
        descricao=pendencia.descricao,
        valor=pendencia.valor,
        data_registro=pendencia.data_registro,
        prazo_pagamento=pendencia.prazo_pagamento,
        sucata_prometida_kg=pendencia.sucata_prometida_kg,
    )

@router.put("/pendencias/{pendencia_id}", response=PendenciaFinanceiraOut)
def atualizar_pendencia(request, pendencia_id: int, payload: PendenciaFinanceiraIn):
    pendencia = get_object_or_404(PendenciaFinanceira, id=pendencia_id)
    fornecedor = get_object_or_404(Fornecedor, id=payload.fornecedor)
    pendencia.fornecedor = fornecedor
    pendencia.descricao = payload.descricao
    pendencia.valor = payload.valor
    pendencia.prazo_pagamento = payload.prazo_pagamento
    pendencia.sucata_prometida_kg = payload.sucata_prometida_kg
    pendencia.save()
    return PendenciaFinanceiraOut(
        id=pendencia.id,
        fornecedor=pendencia.fornecedor.id,
        descricao=pendencia.descricao,
        valor=pendencia.valor,
        data_registro=pendencia.data_registro,
        prazo_pagamento=pendencia.prazo_pagamento,
        sucata_prometida_kg=pendencia.sucata_prometida_kg,
    )

@router.delete("/pendencias/{pendencia_id}")
def deletar_pendencia(request, pendencia_id: int):
    pendencia = get_object_or_404(PendenciaFinanceira, id=pendencia_id)
    pendencia.delete()
    return {"success": True}


@router.post("", response=FinanceiroOut)
def criar_financeiro(request, payload: FinanceiroIn):
    venda_obj = None
    if payload.venda:
        venda_obj = get_object_or_404(Venda, id=payload.venda)
    pendencia_obj = None
    if payload.pendencia:
        pendencia_obj = get_object_or_404(PendenciaFinanceira, id=payload.pendencia)

    financeiro = Financeiro.objects.create(
        tipo=payload.tipo,
        valor=payload.valor,
        descricao=payload.descricao,
        venda=venda_obj,
        pendencia=pendencia_obj
    )
    return FinanceiroOut.from_orm(financeiro)

@router.get("", response=list[FinanceiroOut])
def listar_financeiros(request):
    financeiros = Financeiro.objects.all()
    return [FinanceiroOut.from_orm(f) for f in financeiros]

@router.get("{financeiro_id}", response=FinanceiroOut)
def obter_financeiro(request, financeiro_id: int):
    financeiro = get_object_or_404(Financeiro, id=financeiro_id)
    return FinanceiroOut.from_orm(financeiro)

@router.put("{financeiro_id}", response=FinanceiroOut)
def atualizar_financeiro(request, financeiro_id: int, payload: FinanceiroIn):
    financeiro = get_object_or_404(Financeiro, id=financeiro_id)
    venda_obj = None
    if payload.venda:
        venda_obj = get_object_or_404(Venda, id=payload.venda)
    pendencia_obj = None
    if payload.pendencia:
        pendencia_obj = get_object_or_404(PendenciaFinanceira, id=payload.pendencia)

    financeiro.tipo = payload.tipo
    financeiro.valor = payload.valor
    financeiro.descricao = payload.descricao
    financeiro.venda = venda_obj
    financeiro.pendencia = pendencia_obj
    financeiro.save()
    return FinanceiroOut.from_orm(financeiro)

@router.delete("{financeiro_id}")
def deletar_financeiro(request, financeiro_id: int):
    financeiro = get_object_or_404(Financeiro, id=financeiro_id)
    financeiro.delete()
    return {"success": True}
