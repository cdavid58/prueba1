from django.conf.urls import url
from .views import *

urlpatterns = [
		url(r'^$',index,name='home'),
		url(r'^Register/$',register,name="register"),
		url(r'^LogIn/$',login,name="login"),
		url(r'^LogOut/$',logout,name="logout"),
		url(r'^Corte/$',cortes,name='corte'),
		url(r'^Servi/(?P<pk>\d)/$',Servicio,name='servicio'),
		url(r'^Root/$',admin,name='admin'),
		url(r'^Galeria/$',Galeria,name='galeria'),
		url(r'^Reservar/$',reservacion,name='reservacion'),
		url(r'^Reservar/(?P<cambio>\d+)/$',BotonCambio,name='boton'),

	]

