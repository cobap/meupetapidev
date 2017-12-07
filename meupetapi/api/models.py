from django.db import models
from recurrence.fields import RecurrenceField
from django.contrib.auth.models import User

class TipoUsuario(models.Model):
	id = models.AutoField(primary_key=True)
	descricao = models.CharField(max_length=255)

	def __str__(self):
		return self.descricao

class Usuario(User):
	primeiroNome = models.CharField(max_length=255)
	segundoNome = models.CharField(max_length=255)
	descricaoUsuario = models.TextField()
	regiao = models.CharField(max_length=100, default='')
	estaPasseando = models.BooleanField(default=False)
	tipousuario = models.ManyToManyField(TipoUsuario)
	imagemUsuario = models.ImageField(blank=True)

	def __str__(self):
		return self.primeiroNome

	@property
	def full_name(self):
		return '%s %s' % (self.primeiroNome, self.segundoNome)

class Pet(models.Model):
	TAM_CACHORRO = (
		('P', 'Pequeno'),
		('M', 'Medio'),
		('G', 'Grande'),
	)
	id = models.AutoField(primary_key=True)
	dono = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	nome = models.CharField(max_length=255)
	raca = models.CharField(max_length=255)
	tamanho = models.CharField(max_length=1, choices=TAM_CACHORRO)
	descricaoPet = models.TextField(blank=True)
	imagemPet = models.ImageField(blank=True)

	def __str__(self):
		return self.nome

class Passeador(models.Model):
	id = models.AutoField(primary_key=True)
	primeiroNome = models.CharField(max_length=255)
	segundoNome = models.CharField(max_length=255)
	idade = models.DateField(auto_now=False)
	regiao = models.CharField(max_length=100)
	estaPasseando = models.BooleanField()
	email = models.EmailField(max_length=255)
	imagemPasseador = models.ImageField(blank=True)

	def __str__(self):
		return self.primeiroNome

class Servico(models.Model):
	id = models.AutoField(primary_key=True)
	TIPO_PASSEIO = (
		('P', 'Passeio'),
		('B', 'Banho'),
		('V', 'Veterinario'),
		('T', 'Treinamento'),
	)
	tipoPasseio = models.CharField(max_length=1, choices=TIPO_PASSEIO)
	passeador = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, default=None)

	class Meta:
		unique_together = ('tipoPasseio', 'passeador',)

class Passeio(models.Model):
	id = models.AutoField(primary_key=True)
	duracao = models.DurationField()
	origem = models.TextField()
	local = models.TextField()
	data = models.DateField()
	descricaoPasseio = models.TextField()
	#passeador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
	idRecorrencia = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, default=None, null=True)
	recorrencias = RecurrenceField(include_dtstart=False, blank=True, default=None, null=True)
	# fotoDoPasseio = models.ImageField()
	servico = models.ForeignKey(Servico, on_delete=models.CASCADE, blank=True, default=None)