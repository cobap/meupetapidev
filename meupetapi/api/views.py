#-*- coding: utf-8 -*-
from rest_framework import generics

from . import models
from . import serializers

#Método do Usuário
class ListCreateUsuario(generics.ListCreateAPIView):
	queryset = models.Usuario.objects.all()
	serializer_class = serializers.UsuarioSerializer

class RetrieveUpdateDestroyUsuario(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Usuario.objects.all()
	serializer_class = serializers.UsuarioSerializer

#Métodos do Pet
class ListCreatePet(generics.ListCreateAPIView):
	queryset = models.Pet.objects.all()
	serializer_class = serializers.PetSerializer

class RetrieveUpdateDestroyPet(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Pet.objects.all()
	serializer_class = serializers.PetSerializer

#Métodos do Passeador
class ListCreatePasseador(generics.ListCreateAPIView):
	queryset = models.Passeador.objects.all()
	serializer_class = serializers.PasseadorSerializer

class RetrieveUpdateDestroyPasseador(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Passeador.objects.all()
	serializer_class = serializers.PasseadorSerializer

#Métodos do Passeio
class ListCreatePasseio(generics.ListCreateAPIView):
	queryset = models.Passeio.objects.all()
	serializer_class = serializers.PasseioSerializer

class RetrieveUpdateDestroyPasseio(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Passeio.objects.all()
	serializer_class = serializers.PasseioSerializer

class GetPasseiosByPet(generics.ListAPIView):
	serializer_class = serializers.PasseioSerializer
	def get_queryset(self):
		queryset = models.Passeio.objects.filter(pet=self.kwargs['pet'])
		return queryset

class GetPasseiosByPasseador(generics.ListAPIView):
	serializer_class = serializers.PasseioSerializer
	def get_queryset(self):
		queryset = models.Passeio.objects.filter(passeador=self.kwargs['passeador'])
		return queryset

#Métodos do TipoUsuario
class ListCreateTipoUsuario(generics.ListCreateAPIView):
	queryset = models.TipoUsuario.objects.all()
	serializer_class = serializers.TipoUsuarioSerializer

class RetrieveUpdateDestroyTipoUsuario(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.TipoUsuario.objects.all()
	serializer_class = serializers.TipoUsuarioSerializer

#Métodos do TipoUsuario
class ListCreateServico(generics.ListCreateAPIView):
	queryset = models.Servico.objects.all()
	serializer_class = serializers.ServicoSerializer

class RetrieveUpdateDestroyServico(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Servico.objects.all()
	serializer_class = serializers.ServicoSerializer
