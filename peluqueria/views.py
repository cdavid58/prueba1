from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from .forms import *
from .models import *
from datetime import datetime

sms = 'Quiero reservar el servicio Tal.'
def meta(request):
	tiempo = datetime.now()
	data = {'obj':Servicios.objects.all(),'carrucel':ImgCarrucel.objects.all(),
		'diseño':diseñoGeneral.objects.all(),'mensaje':sms,'year':tiempo}
	return data

def index(request):
	tiempo = datetime.now()
	hora1 = datetime.strptime("19:00:00", "%X").time()
	hora2 = datetime.strptime("23:59:59", "%X").time()
	hora3 = datetime.strptime("08:00:00", "%X").time()
	hora_act = datetime.now().time()
	if hora_act >= hora1 and hora_act <= hora2:
		disponible = 'Cerrada'
	elif hora_act < hora3:
		disponible = 'Cerrada'
	else:
		disponible = 'Abierto'
	data = {'obj':Servicios.objects.all(),'carrucel':ImgCarrucel.objects.all(),
		'diseño':diseñoGeneral.objects.all(),'mensaje':sms,'year':tiempo,'disponible':disponible}

	return render(request,'index.html',data)

def admin(request):
	if 'david' is request.session:
		return render(request,'Admin/site.html',meta(request))
	return index(request)

def reservacion(request):
	return render(request,'Reservacion/reservacion.html',meta(request))

def Galeria(request):
	return render(request,'Galeria/galeria.html',meta(request))


def register(request):
	if request.method == 'POST':
		form = UserNew(request.POST)
		if form.is_valid():
			new_user = form.save()
			username = form.cleaned_data['username']
			clave = form.cleaned_data['password1']
			request.session['register'] = username
			user =auth.authenticate(username = username, password = clave)
			auth.login(request, user)
			return HttpResponseRedirect('/')
	return render(request,"registration/_register.html",meta(request))

def login(request):
	usr = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username = usr, password = password)
	if user is not None and user.is_active:
		auth.login(request,user)
		request.session['login'] = usr
		return HttpResponseRedirect('/')

	return render(request,'registration/login.html',meta(request))

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

def Servicio(request,pk):
	servi = Servicios.objects.get(pk=pk)
	data = {'diseño':diseñoGeneral.objects.all(),'mensaje':sms,'obj':servi}
	return render(request,'Service/Servicios.html',data)

def cortes(request):
	model = Servicios.objects.filter(nombre__contains='corte')
	data = {'obj':Servicios.objects.all(),'carrucel':ImgCarrucel.objects.all(),
		'diseño':diseñoGeneral.objects.all(),'mensaje':sms,'corte':model}
	return render(request,'Service/Cortes.html',data)

def BotonCambio(request,cambio):
	cambio = cambio
	return render(request,'Reservacion/reservacion.html',{'cambio':cambio})








