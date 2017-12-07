from django.conf.urls import url

from . import views
from django.views.i18n import JavaScriptCatalog

# If you already have a js_info_dict dictionary, just add
# 'recurrence' to the existing 'packages' tuple.
js_info_dict = {
    'packages': ('recurrence', ),
}

urlpatterns = [
	#URLs do Usuario
	url(r'^usuario/tipousuario/(?P<tipousuario>\d+)/$', views.GetUsuariosByTipoUsuario.as_view(), name='usuario_tipousuario'),

	url(r'^usuario/registrar/$', views.RegistrarUsuario.as_view(), name='usuario_registrar'),
	url(r'^usuario/login/$', views.VerificarUsuario.as_view(), name='usuario_verificar'),
	url(r'^usuario/listar/$', views.ListarUsuario.as_view(), name='usuario_listar'),
	url(r'^usuario/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyUsuario.as_view(), name='usuario_detail'),
	url(r'^usuario/(?P<idUsuario>\d+)/picture/$', views.RetrieveFotoUsuario, name='usuario_picture'),

	#URLs do Pet
	url(r'^pet/$', views.ListCreatePet.as_view(), name='pets_list'),
	url(r'^pet/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyPet.as_view(), name='pets_detail'),

	#URLs do Passeador
	url(r'^passeador/$', views.ListCreatePasseador.as_view(), name='passeador_list'),
	url(r'^passeador/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyPasseador.as_view(), name='passeador_detail'),

	#URLs do Passeio
	url(r'^passeio/$', views.ListCreatePasseio.as_view(), name='passeio_list'),
	url(r'passeio/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyPasseio.as_view(), name='passeio_detail'),
	url(r'passeio/pet/(?P<pet>\d+)/$', views.GetPasseiosByPet.as_view(), name='passeio_pet'),
	url(r'^passeio/passeador/(?P<passeador>\d+)/$', views.GetPasseiosByPasseador.as_view(), name='passeio_passeador'),
	url(r'passeio/dono/(?P<dono>\d+)/$', views.GetPasseiosByDono.as_view(), name='passeio_dono'),

	#URLs do TipoUsuario
	url(r'^tipousuario/$', views.ListCreateTipoUsuario.as_view(), name='tipousuario_list'),
	url(r'^tipousuario/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyTipoUsuario.as_view(), name='tipousuario_detail'),

	#URLs do Servico
	url(r'^servico/$', views.ListCreateServico.as_view(), name='servico_list'),
	url(r'servico/(?P<pk>\d+)/$', views.RetrieveUpdateDestroyServico.as_view(), name='servico_detail'),
	url(r'servico/passeador/(?P<passeador>\d+)/$', views.GetServicosByPasseador.as_view(), name='servico_passeador'),
	url(r'servico/tiposervico/(?P<tiposervico>[\w\-]+)/$', views.GetServicosByTipoServico.as_view(), name='servico_tiposervico'),
	url(r'servico/provedortiposervico/(?P<tiposervico>[\w\-]+)/$', views.GetProvedoresServicosByTipoServico.as_view(), name='servico_tiposervico'),
	
	# jsi18n can be anything you like here
	url(r'^jsi18n/$', JavaScriptCatalog.as_view(), js_info_dict),

]
