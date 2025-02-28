from rest_framework import serializers
from . import models

class TipoUsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'descricao',
		)
		model = models.TipoUsuario

class TipoUsuarioListingField(serializers.RelatedField):
	def to_internal_value(self, data):
		return data
	def to_representation(self, value):
		return '%d' % (value.id)
	def display_value(self, instance):
		return '%s' % (instance.descricao)

class UsuarioSerializer(serializers.ModelSerializer):
	#tipousuario = TipoUsuarioListingField(read_only=False, many=True, queryset=models.TipoUsuario.objects.all())
	class Meta:
		fields = (
			'id',
			'username',
			'password',
			'primeiroNome',
			'segundoNome',
			'email',
			'tipousuario',
			'imagemUsuario',
		)
		model = models.Usuario

class PetSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'nome',
			'raca',
			'dono',
			'tamanho',
			'descricaoPet',
			'imagemPet',
		)
		model = models.Pet

class PasseadorSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'primeiroNome',
			'segundoNome',
			'idade',
			'regiao',
			'estaPasseando',
			'email',
			'imagemPasseador',
		)
		model = models.Passeador

class PasseioSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'duracao',
			'origem',
			'local',
			'data',
			'descricaoPasseio',
			'pet',
			'idRecorrencia',
			'recorrencias',
			'servico',
		)
		model = models.Passeio

class ServicoSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
			'id',
			'tipoPasseio',
			'passeador',
		)
		model = models.Servico
