from django.contrib import admin
from contatos.models import contato, empresa, setor


@admin.register(contato)
class contatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobre_nome', 'ramal', 'celular', 'email', 'ativo']
    list_editable = ['ativo']
    search_fields = ['nome', 'sobre_nome', 'ramal']
    list_filter = ['setor', 'empresa', 'ativo']

@admin.register(empresa)
class contatoAdmin(admin.ModelAdmin):
    list_display = ['nome_empresa']

@admin.register( setor )
class contatoAdmin( admin.ModelAdmin ):
    list_display = ['nome_setor']