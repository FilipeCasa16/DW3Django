from django.contrib import admin
from .models import Curso, Estudante, Matricula

@admin.register(Estudante)
class EstudanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email') # Colunas que vão aparecer na lista
    list_display_links = ('id', 'nome')    # Quais clicam para editar
    search_fields = ('nome',)             # Barra de busca por nome

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo')
    list_display_links = ('id', 'titulo')

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'estudante', 'curso')