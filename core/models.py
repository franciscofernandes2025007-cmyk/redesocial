from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    conteudo = models.TextField(max_length=500)
    # Adicionámos o campo de imagem (pode ser deixado em branco)
    imagem = models.ImageField(upload_to='posts_imagens/', blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    class Meta:
        ordering = ['-data_criacao']

    def __str__(self):
        return f'{self.autor.username}: {self.conteudo[:20]}...'

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField(max_length=300)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['data_criacao']

    def __str__(self):
        return f'{self.autor.username} comentou no post de {self.post.autor.username}'