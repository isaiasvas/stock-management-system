from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Fornecedor, Movimentacao
from .forms import ProdutoForm, FornecedorForm, MovimentacaoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Listar produtos
@login_required
def listar_produtos(request):
    produtos = Produto.objects.all()
    # Filtros de busca
    busca = request.GET.get('busca')
    if busca:
        produtos = produtos.filter(nome__icontains=busca)
    return render(request, 'estoque/listar_produtos.html', {'produtos': produtos, 'busca': busca})
   

# Adicionar produto
@login_required
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto adicionado com sucesso!')
            return redirect('listar_produtos')
        else:
            messages.error(request, 'Erro ao adicionar produto. Verifique os dados e tente novamente.')
    else:
        form = ProdutoForm()
    return render(request, 'estoque/adicionar_produto.html', {'form': form})

# Editar produto
@login_required
def editar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto editado com sucesso!')
            return redirect('listar_produtos')
        else:
            messages.error(request, 'Erro ao editar produto. Verifique os dados e tente novamente.')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'estoque/editar_produto.html', {'form': form})

# Excluir produto
@login_required
def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto excluido com sucesso!')
        return redirect('listar_produtos')
    return render(request, 'estoque/excluir_produto.html', {'produto': produto})

# Listar fornecedores
@login_required
def listar_fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    # Filtros de busca
    busca = request.GET.get('busca')
    if busca:
        fornecedores = fornecedores.filter(nome__icontains=busca)
    return render(request, 'estoque/listar_fornecedores.html', {'fornecedores': fornecedores, 'busca': busca})

# Adicionar fornecedor
@login_required
def adicionar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fornecedor adicionado com sucesso!')
            return redirect('listar_fornecedores')
        else:
            messages.error(request, 'Erro ao adicionar fornecedor. Verifique os dados e tente novamente.')
    else:
        form = FornecedorForm()
    return render(request, 'estoque/adicionar_fornecedor.html', {'form': form})

# Editar fornecedor
@login_required
def editar_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fornecedor editado com sucesso!')
            return redirect('listar_fornecedores')
        else:
            messages.error(request, 'Erro ao editar fornecedor. Verifique os dados e tente novamente.')
    else:
        form = FornecedorForm(instance=fornecedor)
    return render(request, 'estoque/editar_fornecedor.html', {'form': form})

# Excluir fornecedor
@login_required
def excluir_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == 'POST':
        fornecedor.delete()
        messages.success(request, 'Fornecedor excluido com sucesso!')
        return redirect('listar_fornecedores')
    return render(request, 'estoque/excluir_fornecedor.html', {'fornecedor': fornecedor})

# Listar movimentações de estoque
@login_required
def listar_movimentacoes(request):
    movimentacoes = Movimentacao.objects.all() 
    
    # Filtros de busca
    busca = request.GET.get('busca')
    if busca:
        movimentacoes = movimentacoes.filter(produto__nome__icontains=busca)

    return render(request, 'estoque/listar_movimentacoes.html', {'movimentacoes': movimentacoes, 'busca': busca})

# Adicionar movimentação
@login_required
def adicionar_movimentacao(request):
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movimentação adicionada com sucesso!')
            return redirect('listar_movimentacoes')
        else:
            messages.error(request, 'Erro ao adicionar movimentação. Verifique os dados e tente novamente.')
    else:
        form = MovimentacaoForm()
    return render(request, 'estoque/adicionar_movimentacao.html', {'form': form})

# Editar movimentação
@login_required
def editar_movimentacao(request, pk):
    movimentacao = get_object_or_404(Movimentacao, pk=pk)
    if request.method == 'POST':
        form = MovimentacaoForm(request.POST, instance=movimentacao)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movimentação editada com sucesso!')
            return redirect('listar_movimentacoes')  # Redirecionar para a lista de movimentações
        else:
            messages.error(request, 'Erro ao editar movimentação. Verifique os dados e tente novamente.')
    else:
        form = MovimentacaoForm(instance=movimentacao)
    return render(request, 'estoque/editar_movimentacao.html', {'form': form})

# Excluir movimentação
@login_required
def excluir_movimentacao(request, pk):
    movimentacao = get_object_or_404(Movimentacao, pk=pk)
    if request.method == 'POST':
        movimentacao.delete()
        messages.success(request, 'Movimentação excluida com sucesso!')
        return redirect('listar_movimentacoes')
    return render(request, 'estoque/excluir_movimentacao.html', {'movimentacao': movimentacao})

@login_required
def relatorio_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'estoque/relatorio_produtos.html', {'produtos': produtos})
