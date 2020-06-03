from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from contatos.models import contato
from contatos.serializers import contatoSerializer
from rest_framework.views import APIView
from rest_framework import generics


class contatoListCreate(generics.ListCreateAPIView):
    queryset = contato.objects.all()
    serializer_class = contatoSerializer


class contato_busca_altera_deleta(generics.RetrieveUpdateDestroyAPIView):
    queryset = contato.objects.all()
    serializer_class = contatoSerializer




