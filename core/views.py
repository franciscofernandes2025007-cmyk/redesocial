from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Post, Comentario

# PÁGINA 1: Feed Principal (Lista todos os posts e cria novos com texto e/ou imagem)
def feed(request):
    if request.method == 'POST' and request.user.is_authenticated:
        conteudo = request.POST.get('conteudo')
        imagem = request.FILES.get('imagem')  # Captura o ficheiro de imagem enviado
        if conteudo or imagem:
            Post.objects.create(autor=request.user, conteudo=conteudo, imagem=imagem)
        return redirect('feed')

    posts = Post.objects.all()
    return render(request, 'core/feed.html', {'posts': posts})

# PÁGINA 2: Detalhe do Post (Para ver a publicação e criar/ver Comentários)
def detalhe_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST' and request.user.is_authenticated:
        texto = request.POST.get('texto')
        if texto:
            Comentario.objects.create(post=post, autor=request.user, texto=texto)
        return redirect('detalhe_post', post_id=post.id)

    return render(request, 'core/detalhe.html', {'post': post})

# PÁGINA 3: Perfil do Utilizador (Ver apenas as publicações de uma pessoa específica)
def perfil_utilizador(request, username):
    perfil_user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(autor=perfil_user)
    return render(request, 'core/perfil.html', {'perfil_user': perfil_user, 'posts': posts})

# LÓGICA: Dar e Remover Like (Se já tiver gosto, remove; se não tiver, adiciona)
def dar_like(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=post_id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER', 'feed'))

# LÓGICA: Apagar uma Publicação (Segurança: apenas o próprio autor do post o pode apagar)
def apagar_post(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=post_id, autor=request.user)
        post.delete()
    return redirect('feed')

# LÓGICA: Apagar um Comentário (Segurança: apenas o próprio autor do comentário o pode apagar)
def apagar_comentario(request, comentario_id):
    if request.user.is_authenticated:
        comentario = get_object_or_404(Comentario, id=comentario_id, autor=request.user)
        post_id = comentario.post.id
        comentario.delete()
        return redirect('detalhe_post', post_id=post_id)
    return redirect('feed')