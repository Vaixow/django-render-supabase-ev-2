from django.db import models
from django.core.validators import RegexValidator, EmailValidator

telefono_validator = RegexValidator(
    regex=r'^(\+56\s?)?9\d{8}$',
    message='Ingrese un número de teléfono chileno válido. Ejemplo: +56 912345678 o 912345678'
)

email_validator = EmailValidator(
    message='Ingrese un correo electrónico válido.'
)

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(
        max_length=15,
        validators=[telefono_validator]
    )
    correo = models.EmailField(
        validators=[email_validator]
    )
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre