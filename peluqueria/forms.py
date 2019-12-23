from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import *

'''
class RegistroCliente(forms.ModelForm):
	class Meta:
		model = Cliente
		fields = ['nombre','apellido','telefono','correo','direccion']


		def clean_nombre(self):
			name = self.cleaned_data.get('nombre')
			if len(name)>3:
				for i in list(name):
					if i.isdigit():
						raise forms.ValidationError('El nombre no debe contener un')
				return name
			else:
				raise forms.ValidationError('El nombre debe tener un minimo de 3 letras y un maximo de 5')


'''

class UserNew(UserCreationForm):
	def clean_username(self):
		name = self.cleaned_data.get('username')
		if name == 'david':
			raise forms.ValidationError('Lo siento pero no se puede registrar')
		return name

