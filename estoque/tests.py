from django.test import TestCase
from django.urls import reverse
from .models import Produto, Fornecedor

class ProdutoTests(TestCase):
    def setUp(self):
        # Crie um fornecedor antes de criar o produto
        self.fornecedor = Fornecedor.objects.create(
            nome='Fornecedor Teste',
            telefone='1234567890',
            endereco='Rua Teste, 123'
        )
        
        # Agora você pode criar um produto usando a instância do fornecedor
        self.produto = Produto.objects.create(
            nome='Produto Teste',
            descricao='Descrição do Produto Teste',
            preco=10.0,
            fornecedor=self.fornecedor  # Atribua a instância do fornecedor
        )   

    def test_adicionar_produto(self):
        response = self.client.post(reverse('adicionar_produto'), {
            'nome': 'Produto Teste',
            'descricao': 'Descrição do Produto Teste',
            'preco': 10.0,
            'fornecedor': self.fornecedor.id,  # Adiciona o fornecedor se necessário
        })
        self.assertEqual(response.status_code, 302)  # Verifica se houve redirecionamento
        self.assertEqual(Produto.objects.count(), 2)  # Verifica se o número de produtos aumentou

    def test_editar_produto(self):
        response = self.client.post(reverse('editar_produto', args=[self.produto.pk]), {
            'nome': 'Produto Editado',
            'descricao': 'Descrição Editada',
            'preco': "20.0",
            'fornecedor': self.fornecedor.id,
        })
        self.produto.refresh_from_db()  # Atualiza o objeto do banco de dados
        self.assertEqual(self.produto.nome, 'Produto Editado')  # Verifica se o nome foi atualizado

    def test_excluir_produto(self):
        response = self.client.post(reverse('excluir_produto', args=[self.produto.pk]))
        self.assertEqual(response.status_code, 302)  # Verifica se redireciona após a exclusão
        self.assertEqual(Produto.objects.count(), 0)  # Verifica se o produto foi excluído
