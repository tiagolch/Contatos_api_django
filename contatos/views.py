from rest_framework import viewsets
from contatos.models import contato
from contatos.serializers import contatoSerializer


class contatoViewSet(viewsets.ModelViewSet):
    queryset = contato.objects.all()
    serializer_class = contatoSerializer




