# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-06 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_usuario_imagemusuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='passeador',
            name='imagemPasseador',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='pet',
            name='imagemPet',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
    ]
