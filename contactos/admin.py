from django.contrib import admin
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "telefono", "correo", "direccion")
    search_fields = ("nombre", "telefono", "correo")
    list_filter = ("correo",)
    ordering = ("nombre",)
    list_per_page = 25