from django.db import models
from django.contrib.auth.models import User

# Tabela das Publicações
class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    conteudo = models.TextField(max_length=500)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __format__(self):
        return f"{self.autor.username}: {self.conteudo[:20]}..."

# Tabela dos Comentários (Relacionamento 1-para-Muitos com o Post)
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField(max_length=200)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor.username} no post {self.post.id}"