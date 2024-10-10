from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15, blank=True)
    endereco = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

class Movimentacao(models.Model): 
    TIPO_CHOICES = (
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    )
    
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.produto.nome} ({self.quantidade})"