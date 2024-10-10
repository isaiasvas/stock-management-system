from django import forms
from .models import Produto, Fornecedor, Movimentacao

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'fornecedor', 'categoria', 'peso', 'data_validade', 'imagem']
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'data_validade': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'fornecedor': forms.Select(attrs={'class': 'form-control'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control'}),
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
        model = Movimentacao 
        fields = ['produto', 'quantidade', 'tipo']
        widgets = {
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
            cleaned_data = super().clean()
            tipo = cleaned_data.get('tipo')
            quantidade = cleaned_data.get('quantidade')
            produto = cleaned_data.get('produto')

            # Validação para garantir que há estoque suficiente em caso de saída
            if tipo == 'saida' and produto and quantidade:
                if produto.quantidade < quantidade:
                    raise forms.ValidationError('Quantidade de saída maior do que o estoque disponível.')
            return cleaned_data
