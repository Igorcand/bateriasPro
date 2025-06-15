from ninja import Router
from django.shortcuts import get_object_or_404
from .models import Fornecedor
from fornecedores.schema import FornecedorIn, FornecedorOut

router = Router()

@router.post("", response=FornecedorOut)
def criar_fornecedor(request, payload: FornecedorIn):
    fornecedor = Fornecedor.objects.create(**payload.dict())
    return FornecedorOut.from_orm(fornecedor)

@router.get("", response=list[FornecedorOut])
def listar_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return [FornecedorOut.from_orm(f) for f in fornecedores]

@router.get("{fornecedor_id}", response=FornecedorOut)
def obter_fornecedor(request, fornecedor_id: int):
    fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)
    return FornecedorOut.from_orm(fornecedor)

@router.put("{fornecedor_id}", response=FornecedorOut)
def atualizar_fornecedor(request, fornecedor_id: int, payload: FornecedorIn):
    fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)
    for attr, value in payload.dict().items():
        setattr(fornecedor, attr, value)
    fornecedor.save()
    return FornecedorOut.from_orm(fornecedor)

@router.delete("{fornecedor_id}")
def deletar_fornecedor(request, fornecedor_id: int):
    fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)
    fornecedor.delete()
    return {"success": True}
