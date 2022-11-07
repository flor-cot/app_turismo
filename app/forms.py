from django import forms
from django.forms import ValidationError

import re

def solo_caracteres(value):
    if any(char.isdigit() for char in value ):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                            params={'valor':value})
        #raise ValidationError('El nombre no puede contener números.')

def mail_valido(mail):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,mail):
      return True
   return False

def validar_mail(mail):
        if mail_valido(mail):
                raise ValidationError('El email ingresado no es válido. %(valor)s',
                            params={'valor':mail})

def validar_contrasena(contrasena):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!#%*?&]{6,20}$"
      
    # compilando regex
    pat = re.compile(reg)
      
    # buscando regex                 
    mat = re.search(pat, contrasena)

    if not mat:
        raise ValidationError('Ingrese una contraseña válida. Debe contener de 6 a 20 caracteres, al menos un número, una mayúscula, una minúscula y un caracter especial. '
                            )


class RegistroForm(forms.Form):
    nombre = forms.CharField(
            label='Nombre',
            validators=(solo_caracteres,),
            widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su nombre'})
            )
    apellido = forms.CharField(
            label='Apellido',
            validators=(solo_caracteres,),
            widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su apellido'})
            )
    email = forms.EmailField(
            label='Email',
            max_length=50,
            validators=(validar_mail,),
            error_messages={
                    'required': 'Por favor ingrese un correo electrónico',                    
                },
            widget= forms.TextInput(attrs={'class':'form-control','type':'email','placeholder':'Ingrese su correro electrónico'})
            )
    usuario = forms.CharField(
            label='Usuario',
            required=False,
            validators=(solo_caracteres,),
            widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Elija un nombre de usuario'})
            )
    contraseña = forms.CharField(
            validators=(validar_contrasena,),
            widget= forms.PasswordInput(attrs={'class':'form-control','placeholder':'Elija una contraseña'})
            )


class LoginForm(forms.Form):
     usuario = forms.CharField(
            label='Usuario',
            required=False,
            validators=(solo_caracteres,),
            widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Elija un nombre de usuario'})
            )
     contraseña = forms.CharField(
            validators=(validar_contrasena,),
            widget= forms.PasswordInput(attrs={'class':'form-control','placeholder':'Elija una contraseña'})
            )