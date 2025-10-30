from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto
from .forms import ContactoForm
from django.db.models import Q

def lista_contactos(request):
    query = request.GET.get('q')
    if query:
        contactos = Contacto.objects.filter(
            Q(nombre__icontains=query) | Q(correo__icontains=query)
        )
    else:
        contactos = Contacto.objects.all()
    return render(request, 'contactos/lista_contactos.html', {'contactos': contactos})

def agregar_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm()
    return render(request, 'contactos/agregar_contacto.html', {'form': form})

def editar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'contactos/editar_contacto.html', {'form': form})

def eliminar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        contacto.delete()
        return redirect('lista_contactos')
    return render(request, 'contactos/eliminar_contacto.html', {'contacto': contacto})