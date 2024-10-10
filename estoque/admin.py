from django.contrib import admin
from .models import Produto, Fornecedor, Movimentacao

admin.site.register(Fornecedor)
admin.site.register(Produto)
admin.site.register(Movimentacao)
