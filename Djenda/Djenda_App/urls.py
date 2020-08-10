from django.urls import path
from .views import home, Contactos_lista, botao_ver_todos
from .models import Contactos

urlpatterns = [
    path('', home, name='index'),
    path('botao_ver_todos/', botao_ver_todos, name='botao_ver_todos'),
    path('ver_todos/', Contactos_lista.as_view(model=Contactos,
                                               paginate_by='10',
                                               queryset=Contactos.objects.all(),
                                               context_object_name='task',
                                               template_name='contactos_list.html'), name='ver_todos'),
]
