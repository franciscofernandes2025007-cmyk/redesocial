from django.urls import path
from . import views

urlpatterns = [
    # Páginas principais
    path('', views.feed, name='feed'),  # A raiz agora aponta corretamente para o feed!
    path('post/<int:post_id>/', views.detalhe_post, name='detalhe_post'),
    path('perfil/<str:username>/', views.perfil_utilizador, name='perfil_utilizador'),
    
    # Ações / Lógica
    path('post/<int:post_id>/like/', views.dar_like, name='dar_like'),
    path('post/<int:post_id>/apagar/', views.apagar_post, name='apagar_post'),
    path('comentario/<int:comentario_id>/apagar/', views.apagar_comentario, name='apagar_comentario'),
]