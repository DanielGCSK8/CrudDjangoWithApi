from django.urls import path
from . import views
from django.conf import Settings, settings
from django.contrib.staticfiles.urls import static
from .views import AutorApi

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('libros/editar/<int:id>', views.editar, name='editar'),
    path('autores/', AutorApi.as_view(), name='autores_list'),
    path('autores/<int:id>', AutorApi.as_view(), name='autores_process')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)