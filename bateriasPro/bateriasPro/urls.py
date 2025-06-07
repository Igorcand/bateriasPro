from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from vendas.views import router as vendas_router
from clientes.views import router as clientes_router
from estoque.views import router as estoque_router
from financeiro.views import router as financeiro_router
from fornecedores.views import router as fornecedores_router
from manutencao.views import router as manutencao_router
from servicos.views import router as servicos_router
from sucata.views import router as sucata_router


api = NinjaAPI()

api.add_router("/vendas/", vendas_router, tags=["Vendas"])
api.add_router("/clientes/", clientes_router, tags=["Clientes"])
api.add_router("/estoque/", estoque_router, tags=["Estoque"])
api.add_router("/financeiro/", financeiro_router, tags=["Financeiro"])
api.add_router("/fornecedores/", fornecedores_router, tags=["Fornecedores"])
api.add_router("/manutencao/", manutencao_router, tags=["Manutencao"])
api.add_router("/servicos/", servicos_router, tags=["Servicos"])
api.add_router("/sucata/", sucata_router, tags=["Sucata"])



urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
