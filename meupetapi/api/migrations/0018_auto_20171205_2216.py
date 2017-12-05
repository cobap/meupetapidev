# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-05 22:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0002_logentry_remove_auto_add'),
        ('api', '0017_remove_usuario_idade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='user_ptr',
        ),
        migrations.RemoveField(
            model_name='passeio',
            name='passeador',
        ),
        migrations.AddField(
            model_name='passeio',
            name='servico',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Servico'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='passeador',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Usuario'),
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]
