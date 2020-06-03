from contatos.models import *
from rest_framework import serializers

class empresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = empresa
        fields = '__all__'

class setorSerializer(serializers.ModelSerializer):
    class Meta:
        model = setor
        fields = '__all__'

class contatoSerializer(serializers.ModelSerializer):
    nome_empresa = serializers.CharField(source='empresa.nome_empresa')  ## necessario porque é um campo Foreign Key
    nome_setor = serializers.CharField(source='setor.nome_setor')        ## necessario porque é um campo Foreign Key

    class Meta:
        model = contato
        fields = '__all__'