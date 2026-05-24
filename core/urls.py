from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('post/criar/', views.criar_post, name='criar_post'),
    path('post/eliminar/<int:post_id>/', views.eliminar_post, name='eliminar_post'),
]