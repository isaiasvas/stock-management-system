from django import forms
from .models import Produto, Fornecedor, Movimentacao

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'fornecedor']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'fornecedor': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco < 0:
            raise forms.ValidationError("O preço não pode ser negativo.")
        return preco

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'telefone', 'endereco']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def clean_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if not telefone.isdigit() or len(telefone) < 10:
            raise forms.ValidationError("O telefone deve conter apenas dígitos e ter pelo menos 10 caracteres.")
        return telefone

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao  # Certifique-se que o nome do modelo é "Movimentacao"
        fields = ['produto', 'quantidade', 'tipo']
        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
        }
