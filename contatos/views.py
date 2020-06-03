from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from contatos.models import contato
from contatos.serializers import contatoSerializer
from rest_framework.views import APIView


class contatoListCreate(APIView):
    def get(self, request):
        lista = contato.objects.all()
        serializer = contatoSerializer( lista, many=True )
        return Response( serializer.data )

    def post(self, request):
        serializer = contatoSerializer( data=request.data )  ## Captura os dados no POST
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED )
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )



class contato_busca_altera_deleta(APIView):
    def get_object(self, pk):
        try:
            return contato.objects.get( pk=pk )
        except contato.DoesNotExists:
            raise NotFound()

    def get(self, request, pk):
        dado = self.get_object(pk)
        serializer = contatoSerializer(dado)
        return Response( serializer.data )

    def put(self, request, pk):
        dado = self.get_object(pk)
        serializer = contatoSerializer( dado, data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data )  # nao precisa passar status pois ja gera status 200
        return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )

    def delete(self, request, pk):
        dado = self.get_object(pk)
        dado.delete()
        return Response( status=status.HTTP_204_NO_CONTENT )



