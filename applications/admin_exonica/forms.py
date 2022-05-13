from django import forms
from django.urls import reverse_lazy
from applications.store_exonica.models import AboutExonica, Payment
from .models import Anuncios, CategoriaArticulos, Articulos


class FormCategoria(forms.ModelForm):

    class Meta:
        
        model = CategoriaArticulos
        fields = (
            'short_name',
            'name',
            
        )
        widgets = {
            'short_name': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingrese el nombre corto de la categoria',
                    'class': 'form__two',
                }
            ),
            'name': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingrese el nombre de la categoria',
                    'class': 'form__two',
                }
            ),
        }
        
     
    def clean_email(self):
        cleaned_data = super(FormCategoria, self).clean()
        email = self.cleaned_data['email']
        if email.is_staff == False(email=email):
            reverse_lazy('app_store:pub_articulos')
        
        return self.cleaned_data


class FormArticulos(forms.ModelForm):


    class Meta:
        
        model = Articulos
        fields = (
            'user',
            'title',
            'precio',
            'precio_inst',
            'precio_inst_fuera',
            'descripcion',
            'categoria',
            'imagen',
            'public',
            'in_home',
        )
        widgets = {
            'title': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingrese el nombre del articulo',
                    'class': 'form__two',
                }
            ),
            'precio': forms.NumberInput(
                attrs= {
                    'class': 'form__two',
                }
            ),
            'precio_inst': forms.NumberInput(
                attrs= {
                    'class': 'form__two',
                }
            ),
            'precio_inst_fuera': forms.NumberInput(
                attrs= {
                    'class': 'form__two',
                }
            ),
            'descripcion': forms.Textarea(
                attrs= {
                    'placeholder': 'Ingrese una descripción',
                    'class': 'form__two form__textarea--articulos',
                }
            ),
            'categoria': forms.Select(
                attrs= {
                    'class': 'form__two',
                }
            ),
            'public': forms.CheckboxInput(
                attrs= {
                    'class': 'detail__check',
                }
            ),
            'in_home': forms.CheckboxInput(
                attrs= {
                    'class': 'detail__check',
                }
            ),
            
        }

class FormAnuncios(forms.ModelForm):


    class Meta:
        
        model = Anuncios
        fields = (
            'user',
            'title',
            'mensaje',
            'imagen',
            'public',
            'portada',
        )
        widgets = {
            'title': forms.TextInput(
                attrs= {
                    'placeholder': 'Ingrese el nombre del articulo',
                    'class': 'form__two',
                }
            ),
            'mensaje': forms.Textarea(
                attrs= {
                    'placeholder': 'Ingrese el nombre del articulo',
                    'class': 'form__two form__textarea--articulos',
                }
            ),
            'public': forms.CheckboxInput(
                attrs= {
                    'class': 'detail__check',
                }
            ),
            'portada': forms.CheckboxInput(
                attrs= {
                    'class': 'detail__check',
                }
            ),
            
        }


class FormAbout(forms.ModelForm):
    class Meta:
        
        model = AboutExonica
        fields = (
            'qsomos',
        )
        widgets = {
            'qsomos': forms.Textarea(
                attrs= {
                    'value': 'Escribe información sobre exonica',
                    'class': 'form__two form__textarea--articulos',
                }
            ),
        }

class FormPaymentEditHome(forms.ModelForm):

    class Meta:
        
        model = Payment
        fields = (
            'status',
        )
        widgets = {
            'status': forms.Select(
                attrs= {
                    'class': 'form__two',
                }
            )
        }
        
