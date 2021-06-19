from django.contrib import admin
from .models import Cargo, Produto, Funcionario, Galeria

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'icone', 'ativo', 'modificado')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')

@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'imagem', 'ativo', 'modificado')

#salvar(usar ctrl + S )
