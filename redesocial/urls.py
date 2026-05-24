from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.get_urls()), # Alterado ligeiramente para compatibilidade do admin
    path('', include('core.urls')),
]