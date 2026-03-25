from rest_framework import viewsets
from .models import *
from .serializers import *

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    filterset_fields = ['nome', 'email']

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    filterset_fields = ['titulo']

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    filterset_fields = ['estudante', 'curso']