from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Garante que 'core.urls' existe e não inclui 'redesocial.urls' de volta!
]

# Inclui os ficheiros de média apenas em ambiente de desenvolvimento e se as URLs existirem
if settings.DEBUG and settings.MEDIA_URL:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)