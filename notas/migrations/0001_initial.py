# Generated by Django 5.1.3 on 2024-11-11 14:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aulas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notas', to=settings.AUTH_USER_MODEL)),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notas', to='aulas.aula')),
            ],
            options={
                'unique_together': {('aluno', 'aula')},
            },
        ),
    ]