from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(null=True, blank=True)
    endereco = models.TextField(blank=True)
    tipo_fornecimento = models.CharField(max_length=50, choices=[('carne', 'Carne'), ('tempero', 'Tempero'), ('embalagem', 'Embalagem')])

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True)
    categoria = models.CharField(max_length=50, choices=[('carne', 'Carne'), ('tempero', 'Tempero'), ('acompanhamento', 'Acompanhamento'), ('bebida', 'Bebida')])
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Peso em kg
    data_validade = models.DateField(null=True, blank=True)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)  # Requer configuração de media files
    quantidade = models.IntegerField(default=0)  # Campo para quantidade em estoque
    
    def __str__(self):
        return self.nome

class Movimentacao(models.Model):
    TIPO_MOVIMENTACAO = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    tipo = models.CharField(max_length=7, choices=TIPO_MOVIMENTACAO)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo.capitalize()} - {self.produto.nome} ({self.quantidade})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Primeiro salva a movimentação

        # Atualizar o estoque do produto
        if self.tipo == 'entrada':
            self.produto.quantidade += self.quantidade
        elif self.tipo == 'saida':
            if self.produto.quantidade >= self.quantidade:
                self.produto.quantidade -= self.quantidade
            else:
                raise ValueError('Não há estoque suficiente para realizar a saída.')

        self.produto.save()  # Salva o produto com a nova quantidade