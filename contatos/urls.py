from django.urls import path
from contatos.views import *


urlpatterns = [
    path('', contato_list),
    path('<int:pk>/', contato_busca_altera_deleta)
]