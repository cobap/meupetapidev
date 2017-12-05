#-*- coding: utf-8 -*-
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

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
		user = models.Usuario.objects.create_user(request.data['username'],request.data['email'], request.data['password'])
		user.save()
		return JSONResponse({'result':1})

class VerificarUsuario(generics.GenericAPIView):
	serializer_class = serializers.UsuarioSerializer
	def post (login, request):
		user = authenticate(username=request.data['username'],password=request.data['password'])
		if user is not None:
			return JSONResponse({'result':1})
		return JSONResponse({'result':0})

#Métodos do Usuario
class ListarUsuario(generics.ListAPIView):
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

#Métodos do Login
class Login(generics.GenericAPIView):
	serializer_class = serializers.UsuarioSerializer
	def post(login, request):
		queryset = models.Usuario.objects.filter(email=request.data['email'],senha=request.data['senha'])
		if(queryset.count() == 1): 
			#token = Token.objects.create(user=queryset[0])
			#print token.key
			usuario = {'id': queryset[0].id, 'primeiroNome': queryset[0].primeiroNome, 'segundoNome': queryset[0].segundoNome, 'idade': queryset[0].idade, 'email': queryset[0].email, 'descricaoUsuario': queryset[0].descricaoUsuario, 'regiao': queryset[0].regiao, 'estaPasseando': queryset[0].estaPasseando, 'tipousuario':[]}
			#tipousuario = []
			#for val in queryset[0].tipousuario.all():
			#	tipousuario += val
			#usuario['tipousuario'] = tipousuario
			#print usuario
			return JSONResponse({'result':'OK', 'usuario': usuario})
		return JSONResponse({'result':'NOK', 'message': 'Login failed'})
		

class Logout(generics.RetrieveUpdateDestroyAPIView):
	queryset = models.Servico.objects.all()
	serializer_class = serializers.ServicoSerializer
