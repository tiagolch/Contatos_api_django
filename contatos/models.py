from django.db import models

class setor(models.Model):
    nome_setor = models.CharField(max_length=25, null=False, blank=False, verbose_name='Setor')

    class Meta:
        db_table = 'setor'

    def __str__(self):
        return self.nome_setor


class empresa(models.Model):
    nome_empresa = models.CharField(max_length=60, null=False, blank=False, verbose_name='Empresa')

    class Meta:
        db_table = 'empresa'

    def __str__(self):
        return self.nome_empresa


class contato(models.Model):
    nome = models.CharField(max_length=60, null=False, blank=False, verbose_name='Nome')
    sobre_nome = models.CharField(max_length=60, null=False, blank=False, verbose_name='Sobre Nome')
    setor = models.ForeignKey(setor, on_delete=models.DO_NOTHING)
    empresa = models.ForeignKey(empresa, on_delete=models.DO_NOTHING)
    ramal = models.CharField(max_length=4, blank=True, null=True, verbose_name='Ramal')
    celular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Celular')
    email = models.EmailField(null=True, blank=True)
    data_cadastro = models.DateField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'contato'

    def __str__(self):
        return self.nome + str(self.setor)+ str(self.empresa)

    def get_data_cadastro(self):
        return self.data_cadastro.strftime('%d/%m/%Y')
