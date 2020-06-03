from rest_framework.decorators import api_view
from rest_framework.response import Response
from contatos.models import contato
from contatos.serializers import contatoSerializer


@api_view(['GET'])
def contato_list(request):
    lista = contato.objects.all()
    serializer = contatoSerializer(lista, many=True)
    return Response(serializer.data)