from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Nota
from .serializers import NotaSerializer

class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer
    permission_classes = [IsAuthenticated]  # Apenas usuários autenticados podem acessar

    def perform_create(self, serializer):
        # Realiza ações ao criar a nota, se necessário (por exemplo, verificação)
        serializer.save()
