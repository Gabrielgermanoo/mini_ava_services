from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Curso, Matricula
from .serializers import CursoSerializer, MatriculaSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticated] 

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    permission_classes = [IsAuthenticated]
