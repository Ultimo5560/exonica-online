from django.contrib.auth import authenticate
from django import forms
from .models import User

class UserRegisterForm(forms.ModelForm):

    password_1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form__two',
                'placeholder': 'Contraseña'
            }
        )
    )
    password_2 = forms.CharField(
        label='Confirmar contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form__two',
                'placeholder': 'Repetir Contraseña'
            }
        )
    )

    class Meta:
        model = User
        fields = (
            'nombre',
            'apellidos',
            'fecha_nacimiento',
            'email',
            'celular',
            'genero',
            'ciudad',
            'estado',
            'direccion_envio',
            'cpostal'
        )
        widgets = {
            'nombre': forms.TextInput(
                attrs= {
                    'class': 'form__two',
                }
            ),
            'apellidos': forms.TextInput(
                attrs= {
                    'class': 'form__two',
                }
            ),
            'fecha_nacimiento': forms.DateInput(
                format='%Y-%m-%d',
                attrs= {
                    'type': 'date',
                    'class': 'form__two',
                }
            ),
            'email': forms.EmailInput(
                attrs= {
                    'class': 'form__two',
                }
            ),
            'celular': forms.TextInput(
                attrs= {
                    'class': 'form__two',
                }
            ),
            'genero': forms.Select(
                attrs= {
                    'class': 'form__two',
                }
            ),
            'ciudad': forms.TextInput(
                attrs= {
                    'class': 'form__two',
                }
            ),
            'estado': forms.Select(
                attrs= {
                    'class': 'form__two',
                }
            ),
            'direccion_envio': forms.TextInput(
                attrs= {
                    'class': 'form__two',
                }
            ),
            'cpostal': forms.TextInput(
                attrs= {
                    'class': 'form__two',
                }
            ),
        }

    def clean_password_2(self):
        if self.cleaned_data['password_2'] != self.cleaned_data['password_1']:
            self.add_error('password_2', 'Las contraseñas no coinciden')
        elif len(self.cleaned_data['password_1']) < 5:
            self.add_error('password_1', 'La contraseña no debe ser menor a 5 digitos')
        

class UserLoginForm(forms.Form):

    email = forms.EmailField(
        required=True,
    )

    password = forms.CharField(
        label=False,
    )

    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Correo y/o contraseña incorrectos')

        return self.cleaned_data


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'ocupations',
            'is_superuser',
        )
        widgets = {
            'ocupations': forms.Select(
                attrs= {
                    'class': 'form__two',
                    
                }
            ),
            'is_superuser': forms.CheckboxInput(
                attrs= {
                    'class': 'detail__check',
                }
            ),
        }

class UserUpdatePerfilForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'nombre',
            'apellidos',
            'fecha_nacimiento',
            'email',
            'celular',
            'genero',
            'ciudad',
            'estado',
            'direccion_envio',
            'cpostal'
        )
        widgets = {
            'nombre': forms.TextInput(
                attrs= {
                    'class': 'form__two',
                }
            ),
            'apellidos': forms.TextInput(
                attrs= {
                    'class': 'form__two',
                }
            ),
            'fecha_nacimiento': forms.DateInput(
                format='%Y-%m-%d',
                attrs= {
                    'type': 'date',
                    'class': 'form__two',
                }
            ),
            'email': forms.EmailInput(
                attrs= {
                    'class': 'form__two',
                }
            ),
            'celular': forms.TextInput(
                attrs= {
                    'class': 'form__two',
                }
            ),
            'genero': forms.Select(
                attrs= {
                    'class': 'form__two',
                }
            ),
            'ciudad': forms.TextInput(
                attrs= {
                    'class': 'form__two',
                }
            ),
            'estado': forms.Select(
                attrs= {
                    'class': 'form__two',
                }
            ),
            'direccion_envio': forms.TextInput(
                attrs= {
                    'class': 'form__two',
                }
            ),
            'cpostal': forms.TextInput(
                attrs= {
                    'class': 'form__two',
                }
            ),
        }
