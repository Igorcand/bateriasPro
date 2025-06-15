
from django.shortcuts import get_object_or_404

from clientes.schema import ClienteIn, ClienteOut
from clientes.models import Cliente  # Ajuste o import conforme seu app

from ninja import Router

router = Router()

# 👉 Criar cliente
@router.post("", response=ClienteOut)
def criar_cliente(request, payload: ClienteIn):
    cliente = Cliente.objects.create(**payload.dict())
    return ClienteOut(
        id = cliente.id,
        nome = cliente.nome,
        telefone = cliente.telefone,
        email = cliente.email,
        cpf = cliente.cpf
    )

# 👉 Listar todos os clientes
@router.get("", response=list[ClienteOut])
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return [ClienteOut(
        id = cliente.id,
        nome = cliente.nome,
        telefone = cliente.telefone,
        email = cliente.email,
        cpf = cliente.cpf
    ) for cliente in clientes]

# 👉 Obter cliente por ID
@router.get("{cliente_id}", response=ClienteOut)
def obter_cliente(request, cliente_id: int):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return ClienteOut(
        id = cliente.id,
        nome = cliente.nome,
        telefone = cliente.telefone,
        email = cliente.email,
        cpf = cliente.cpf
    )


@router.delete("{cliente_id}")
def deletar_cliente(request, cliente_id: int):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.delete()
    return {"success": True}


@router.put("{cliente_id}", response=ClienteOut)
def atualizar_cliente(request, cliente_id: int, payload: ClienteIn):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    for attr, value in payload.dict().items():
        setattr(cliente, attr, value)
    cliente.save()
    return ClienteOut(
        id = cliente.id,
        nome = cliente.nome,
        telefone = cliente.telefone,
        email = cliente.email,
        cpf = cliente.cpf
    )
