from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from contatos.models import contato
from contatos.serializers import contatoSerializer


@api_view(['GET', 'POST'])
def contato_list(request):
    if request.method == 'GET':
        lista = contato.objects.all()
        serializer = contatoSerializer(lista, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = contatoSerializer(data=request.data) ## Captura os dados no POST
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def contato_busca_altera_deleta(request, pk):
    try:
        dado = contato.objects.get(pk=pk)

    except contato.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = contatoSerializer(dado)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = contatoSerializer(dado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) # nao precisa passar status pois ja gera status 200
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        dado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


