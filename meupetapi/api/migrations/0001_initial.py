# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-05 22:52
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import recurrence.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passeador',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('primeiroNome', models.CharField(max_length=255)),
                ('segundoNome', models.CharField(max_length=255)),
                ('idade', models.DateField()),
                ('regiao', models.CharField(max_length=100)),
                ('estaPasseando', models.BooleanField()),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Passeio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('duracao', models.DurationField()),
                ('origem', models.TextField()),
                ('local', models.TextField()),
                ('data', models.DateField()),
                ('descricaoPasseio', models.TextField()),
                ('recorrencias', recurrence.fields.RecurrenceField(blank=True, default=None, null=True)),
                ('idRecorrencia', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Passeio')),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('raca', models.CharField(max_length=255)),
                ('tamanho', models.CharField(choices=[(b'P', b'Pequeno'), (b'M', b'Medio'), (b'G', b'Grande')], max_length=1)),
                ('descricaoPet', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipoPasseio', models.CharField(choices=[(b'P', b'Passeio'), (b'B', b'Banho'), (b'V', b'Veterinario'), (b'T', b'Treinamento')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('primeiroNome', models.CharField(max_length=255)),
                ('segundoNome', models.CharField(max_length=255)),
                ('descricaoUsuario', models.TextField()),
                ('regiao', models.CharField(default=b'', max_length=100)),
                ('estaPasseando', models.BooleanField(default=False)),
                ('tipousuario', models.ManyToManyField(to='api.TipoUsuario')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='servico',
            name='passeador',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Usuario'),
        ),
        migrations.AddField(
            model_name='pet',
            name='dono',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Usuario'),
        ),
        migrations.AddField(
            model_name='passeio',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Pet'),
        ),
        migrations.AddField(
            model_name='passeio',
            name='servico',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Servico'),
        ),
    ]
