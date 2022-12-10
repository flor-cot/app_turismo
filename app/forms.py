from django.contrib.auth.models import User
from django import forms
from django.forms import ValidationError

from django.contrib.auth.forms import UserCreationForm

import re

def solo_caracteres(value):
    if any(char.isdigit() for char in value ):
        raise ValidationError('No puede contener números. %(valor)s',
                            params={'valor':value})


def validar_nombre_usuario(usuario):
    reg = "^[a-zA-Z0-9]+([_ -]?[a-zA-Z0-9])*$"
      
    # compilando regex
    pat = re.compile(reg)
      
    # buscando regex                 
    mat = re.search(pat, usuario)

    if not mat:
        raise ValidationError('Elige un nombre de usuario válido.'
                            )
        #raise ValidationError('El nombre no puede contener números.')

# def mail_valido(mail):
#    pat = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
#    if re.match(pat,mail):
#       return True
#    return False

# def validar_mail(mail):
        if mail_valido(mail):
                raise ValidationError('El email ingresado no es válido. %(valor)s',
                            params={'valor':mail})

def validar_contrasena(contrasena):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!#_%*?&]{6,20}$"
      
    # compilando regex
    pat = re.compile(reg)
      
    # buscando regex                 
    mat = re.search(pat, contrasena)

    if not mat:
        raise ValidationError('La contraseña debe contener: de 6 a 20 caracteres, al menos un número, una mayúscula, una minúscula y un caracter especial. '
                            )


# class RegistroForm(forms.Form):
#     nombre = forms.CharField(
#             label='Nombre',
#             validators=(solo_caracteres,),
#             widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su nombre'})
#             )
#     apellido = forms.CharField(
#             label='Apellido',
#             validators=(solo_caracteres,),
#             widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su apellido'})
#             )
#     email = forms.EmailField(
#             label='Email',
#             max_length=50,
#             validators=(validar_mail,),
#             error_messages={
#                     'required': 'Por favor ingrese un correo electrónico',                    
#                 },
#             widget= forms.TextInput(attrs={'class':'form-control','type':'email','placeholder':'Ingrese su correro electrónico'})
#             )
#     usuario = forms.CharField(
#             label='Usuario',
#             required=False,
#             validators=(solo_caracteres,),
#             widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Elija un nombre de usuario'})
#             )
#     contraseña = forms.CharField(
#             validators=(validar_contrasena,),
#             widget= forms.PasswordInput(attrs={'class':'form-control','placeholder':'Elija una contraseña'})
#             )

class RegistroForm(UserCreationForm):
        username = forms.CharField(
            label=('Nombre de Usuario'),
            max_length=50,
            help_text=('Requerido!'),
             validators=[validar_nombre_usuario],
            error_messages={'unique': ("Ya existe!"),'required':("El campo no puede estar vacío.")},
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
        first_name = forms.CharField(
            label=('Nombre'),
            max_length=50,
            help_text=('Requerido!'),
            validators=[solo_caracteres],
            error_messages={'required':("El campo no puede estar vacío.")},
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
        last_name = forms.CharField(
            label=('Apellido'),
            max_length=50,
            help_text=('Requerido!'),
            validators=[solo_caracteres],
            error_messages={'required':("El campo no puede estar vacío.")},
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
        email = forms.EmailField(max_length=50, help_text='Requerido!',
            error_messages={'required':("El campo no puede estar vacío.")},
            widget=(forms.TextInput(attrs={'class': 'form-control'})))
        password1 = forms.CharField(
            label=('Contraseña'),
            validators=[validar_contrasena],
            error_messages={'required':("El campo no puede estar vacío.")},
            widget=(forms.PasswordInput(attrs={'class': 'form-control'}))
            )
        password2 = forms.CharField(label=('Ingrese de nuevo la contraseña'),
            error_messages={'required':("El campo no puede estar vacío.")}, 
            widget=forms.PasswordInput(attrs={'class': 'form-control'}),
            help_text=('Misma contraseña!'))
        class Meta:
            model = User
            fields = ['first_name','last_name','username', 'email', 'password1', 'password2']        


# class LoginForm(forms.Form):
#      usuario = forms.CharField(
#             label='Usuario',
#             required=False,
#         #     validators=(solo_caracteres,),
#             widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Elija un nombre de usuario'})
#             )
#      contraseña = forms.CharField(
#         #     validators=(validar_contrasena,),
#             widget= forms.PasswordInput(attrs={'class':'form-control','placeholder':'Elija una contraseña'})
#             )