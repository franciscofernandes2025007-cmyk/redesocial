from django.contrib import admin
from .models import Post, Comentario

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('autor', 'conteudo_curto', 'data_criacao')
    search_fields = ('conteudo', 'autor__username')
    list_filter = ('data_criacao', 'autor') # Corrigido aqui!

    def conteudo_curto(self, obj):
        if len(obj.conteudo) > 50:
            return f"{obj.conteudo[:50]}..."
        return obj.conteudo
    conteudo_curto.short_description = 'Conteúdo'

admin.site.register(Comentario)