from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    # Qualquer campo personalizado que você queira adicionar

    professor = models.BooleanField(default=False, help_text="Indica se o usuário é um professor.")

    groups = models.ManyToManyField(
        Group,
        related_name="usuarios_grupo",  # Nome exclusivo para evitar o conflito
        blank=True,
        help_text="Grupos aos quais o usuário pertence.",
        verbose_name="grupos",
        related_query_name="usuario",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="usuarios_permissao",  # Nome exclusivo para evitar o conflito
        blank=True,
        help_text="Permissões específicas do usuário.",
        verbose_name="permissões de usuário",
        related_query_name="usuario",
    )
