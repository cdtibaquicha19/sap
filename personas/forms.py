from django.forms import ModelForm, EmailInput

from personas.models import Persona, Domicilio


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        field = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }
        exclude = []

class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio
        field = '__all__'
        exclude = []