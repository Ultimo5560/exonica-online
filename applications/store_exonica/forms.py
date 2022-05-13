from django import forms
from .models import FormContact, Payment


class Form_contact(forms.ModelForm):

    class Meta:
        
        model = FormContact
        fields = (
            'full_name',
            'email',
            'celphone',
            'message',
        )
        widgets = {
            'full_name': forms.TextInput(
                attrs= {
                    'placeholder': 'Escribe tu nombre completo',
                    'class': 'form__two',
                }
            ),
            'email': forms.EmailInput(
                attrs= {
                    'placeholder': 'usuario@email.com',
                    'class': 'form__two',
                }
            ),
            'celphone': forms.TextInput(
                attrs= {
                    'placeholder': '555-555-5555',
                    'class': 'form__two',
                }
            ),
            'message': forms.Textarea(
                attrs= {
                    'placeholder': 'Escribe tu mensaje',
                    'class': 'form__two form__two--textarea',
                }
            ),
            
        }


class VentaForm(forms.Form):
    count = forms.IntegerField(
        label='Cantidad',
        min_value=1,
        widget=forms.NumberInput(
            attrs = {
                'value': '1',
                'class': 'uk-input',
            }
        )
    )
    instalacion = forms.BooleanField(
        label='Deseo contratar la instalación',
        required=False,
        widget=forms.CheckboxInput(
            attrs = {
                'class': 'detail__check',
            }
        )
    )

    #
    def clean_count(self):
        count = self.cleaned_data['count']
        if count < 1:
            raise forms.ValidationError('Ingrese una cantidad mayor a cero')

        return count


class Form_payment_trans(forms.ModelForm):
    
    class Meta:
        
        model = Payment
        fields = (
            'comprobante_pago',
        )
