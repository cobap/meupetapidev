#-*- coding: utf-8 -*-
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
# from serializers import UsuarioSerializer

from . import models
from . import serializers

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class RegistrarUsuario(generics.GenericAPIView):
	serializer_class = serializers.UsuarioSerializer
	def post (login, request):
		# user = models.Usuario.objects.create_user(request.data['username'],request.data['email'], request.data['password'], request.data['primeiroNome'], request.data['segundoNome'],request.data['tipousuario'])
		user = models.Usuario.objects.create_user(request.data['username'],request.data['email'], request.data['password'])
		user.primeiroNome = request.data['primeiroNome']
		user.segundoNome = request.data['segundoNome']
		user.tipousuario = request.data['tipousuario']
		user.imagemUsuario = request.data['imagemUsuario']
		user.save()
		usuario_serializado = serializers.UsuarioSerializer(user)
		return Response(usuario_serializado.data, status=status.HTTP_200_OK)

class VerificarUsuario(generics.GenericAPIView):
	serializer_class = serializers.UsuarioSerializer
	def post (login, request):
		user = authenticate(username=request.data['username'],password=request.data['password'])
		
		if user is not None:
			usuario = models.Usuario.objects.get(pk=user.id)
			usuario_serializado = serializers.UsuarioSerializer(usuario)
			return Response(usuario_serializado.data, status=status.HTTP_200_OK)
		return Response({'result': 'User not Found'}, status=status.HTTP_401_UNAUTHORIZED)

#Métodos do Usuario
class ListarUsuario(generics.ListAPIView):
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

#passeios de um pet, para que seu dono possa planejar a agenda
class GetPasseiosByPet(generics.ListAPIView):
	serializer_class = serializers.PasseioSerializer
	def get_queryset(self):
		queryset = models.Passeio.objects.filter(pet=self.kwargs['pet'])
		return queryset

#passeios de um passeador, para que ele possa planejar sua agenda
class GetPasseiosByPasseador(generics.ListAPIView):
	serializer_class = serializers.PasseioSerializer
	def get_queryset(self):
		queryset = models.Passeio.objects.filter(servico__passeador=self.kwargs['passeador'])
		return queryset

#servicos oferecidos por um passeador, para que eu possa buscar na hora de contratar
class GetServicosByPasseador(generics.ListAPIView):
	serializer_class = serializers.ServicoSerializer
	def get_queryset(self):
		queryset = models.Servico.objects.filter(passeador=self.kwargs['passeador'])
		return queryset

#servicos oferecidos por um tipo de servico
class GetServicosByTipoServico(generics.ListAPIView):
	serializer_class = serializers.ServicoSerializer
	def get_queryset(self):
		queryset = models.Servico.objects.filter(tipoPasseio=self.kwargs['tiposervico'])
		return queryset

#provedores de servicos oferecidos por um tipo de servico
class GetProvedoresServicosByTipoServico(generics.ListAPIView):
	serializer_class = serializers.UsuarioSerializer
	def get_queryset(self):
		queryset = models.Usuario.objects.filter(servico__tipoPasseio=self.kwargs['tiposervico']).all()
		return queryset

#todos os passeios de todos os pets de um mesmo dono, para que ele possa programar sua agenda
class GetPasseiosByDono(generics.ListAPIView):
	serializer_class = serializers.PasseioSerializer
	def get_queryset(self):
		queryset = models.Passeio.objects.filter(pet__dono=self.kwargs['dono'])
		return queryset

#usuarios por tipo de usuario
class GetUsuariosByTipoUsuario(generics.ListAPIView):
	serializer_class = serializers.UsuarioSerializer
	def get_queryset(self):
		queryset = models.Usuario.objects.filter(tipousuario=self.kwargs['tipousuario'])
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