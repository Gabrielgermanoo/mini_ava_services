from django.apps import AppConfig
from django.db.models.signals import post_migrate

class AutenticacaoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "autenticacao"

    def ready(self):
        from django.contrib.auth.models import Group

        def criar_grupo_professor(sender, **kwargs):
            Group.objects.get_or_create(name='Professor')

        post_migrate.connect(criar_grupo_professor, sender=self)
