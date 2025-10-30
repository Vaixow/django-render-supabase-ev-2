from django import forms
from .models import Contacto
import re

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'telefono', 'correo', 'direccion']

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono'].replace(" ", "")
        # Permitir +56 o nada al inicio
        if telefono.startswith("+56"):
            telefono = telefono[3:]
        if telefono.startswith("9") and len(telefono) == 9 and telefono.isdigit():
            return self.cleaned_data['telefono']
        elif len(telefono) == 9 and telefono.isdigit():
            return self.cleaned_data['telefono']
        raise forms.ValidationError("El teléfono debe ser chileno, empezar con 9 y tener 9 dígitos (Ej: 912345678 o +56 912345678).")