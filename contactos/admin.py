from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import Contacto

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "telefono", "correo", "direccion")
    search_fields = ("nombre", "correo")
    ordering = ("nombre",)
    list_per_page = 25
    actions = ["exportar_csv"]

    def exportar_csv(self, request, queryset):
        """
        Exporta los contactos seleccionados a un archivo CSV.
        """
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="contactos.csv"'

        writer = csv.writer(response)
        writer.writerow(["Nombre", "Teléfono", "Correo", "Dirección"])

        for contacto in queryset:
            writer.writerow([contacto.nombre, contacto.telefono, contacto.correo, contacto.direccion])

        return response

    exportar_csv.short_description = "Exportar contactos seleccionados a CSV"
