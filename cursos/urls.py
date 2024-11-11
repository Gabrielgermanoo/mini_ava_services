from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CursoViewSet, MatriculaViewSet

router = DefaultRouter()
router.register(r'cursos', CursoViewSet)
router.register(r'matriculas', MatriculaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
