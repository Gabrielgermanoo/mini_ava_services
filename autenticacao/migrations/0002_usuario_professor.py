# Generated by Django 5.1.3 on 2024-11-18 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='professor',
            field=models.BooleanField(default=False, help_text='Indica se o usuário é um professor.'),
        ),
    ]