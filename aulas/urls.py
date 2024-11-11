from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AulaViewSet, MaterialViewSet

router = DefaultRouter()
router.register(r'aulas', AulaViewSet)
router.register(r'materiais', MaterialViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
