from contatos.models import *
from rest_framework import serializers

class contatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = contato
        fields = ['id', 'nome', 'sobre_nome', 'ramal', 'celular', 'email']


class empresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = empresa
        fields = ['id', 'nome_empresa']


class setorSerializer(serializers.ModelSerializer):
    class Meta:
        model = setor
        fields = ['id', 'nome_setor']


