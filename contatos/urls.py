from django.urls import path
from contatos.views import *


urlpatterns = [
    path('', contato_list),
]