from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comentario

def feed(request):
    # Procurar todos os posts do mais recente para o mais antigo (Operação READ)
    posts = Post.objects.all().order_by('-criado_em')
    return render(request, 'core/feed.html', {'posts': posts})

@login_required
def criar_post(request):
    if request.method == 'POST':
        conteudo = request.POST.get('conteudo')
        if conteudo:
            # Criar o post associado ao utilizador logado (Operação CREATE)
            Post.objects.create(autor=request.user, conteudo=conteudo)
    return redirect('feed')

@login_required
def eliminar_post(request, post_id):
    # Procurar o post ou dar erro 404 se não existir
    post = get_object_or_404(Post, id=post_id)
    # Segurança: Apenas o autor pode apagar o seu próprio post
    if post.autor == request.user:
        post.delete() # Operação DELETE
    return redirect('feed')