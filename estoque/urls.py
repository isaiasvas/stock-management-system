from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('produtos/adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('produtos/editar/<int:pk>/', views.editar_produto, name='editar_produto'),
    path('produtos/excluir/<int:pk>/', views.excluir_produto, name='excluir_produto'),
    path('fornecedores/', views.listar_fornecedores, name='listar_fornecedores'),
    path('fornecedores/adicionar/', views.adicionar_fornecedor, name='adicionar_fornecedor'),
    path('fornecedores/editar/<int:pk>/', views.editar_fornecedor, name='editar_fornecedor'),
    path('fornecedores/excluir/<int:pk>/', views.excluir_fornecedor, name='excluir_fornecedor'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('movimentacoes/', views.listar_movimentacoes, name='listar_movimentacoes'),
    path('movimentacoes/adicionar/', views.adicionar_movimentacao, name='adicionar_movimentacao'),
    path('movimentacoes/editar/<int:pk>/', views.editar_movimentacao, name='editar_movimentacao'),
    path('movimentacoes/excluir/<int:pk>/', views.excluir_movimentacao, name='excluir_movimentacao'),  # Atualizado para pk
    path('relatorio/produtos/', views.relatorio_produtos, name='relatorio_produtos'),

]


