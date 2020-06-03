from django.urls import path
from contatos.views import *


urlpatterns = [
    path('',  contatoListCreate.as_view()),
    path('<int:pk>/', contato_busca_altera_deleta.as_view())
]