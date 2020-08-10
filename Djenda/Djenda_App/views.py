from django.http import Http404
from django.shortcuts import render, redirect
from .models import Contactos, Empresa, Departamento
from django.contrib import messages
from django.views.generic.list import ListView


def is_valid_queryparam(param):
    return param != '' and param is not None


def home(request):
    try:
        contactos = Contactos.objects.all().order_by('nome')[:0]
        empresas = Empresa.objects.all()
        departamentos = Departamento.objects.all()
        busca = request.GET.get('inputNome')
        empresa_query = request.GET.get('inputEmpresa')
        departamento_query = request.GET.get('inputDepartamento')
        x = ''
        if busca:
            contactos = Contactos.objects.filter(nome__icontains=busca)
            x = Contactos.objects.filter(nome__icontains=busca).count()
            messages.add_message(request, messages.SUCCESS, 'Contacto(s) encontrado(s).')
        elif is_valid_queryparam(departamento_query) and departamento_query != 'Escolher...':
            contactos = Contactos.objects.filter(departamento__departamento__exact=departamento_query)
            x = Contactos.objects.filter(departamento__departamento=departamento_query).count()
            messages.add_message(request, messages.SUCCESS, 'Contacto(s) encontrado(s).')
        elif is_valid_queryparam(empresa_query) and empresa_query != 'Escolher...':
            contactos = Contactos.objects.filter(empresa__empresa__iexact=empresa_query)
            x = Contactos.objects.filter(empresa__empresa__icontains=empresa_query).count()
            messages.add_message(request, messages.SUCCESS, 'Contacto(s) encontrado(s).')
        else:
            messages.add_message(request, messages.INFO, 'Nada para mostrar.')
    except Contactos.DoesNotExist:
        raise Http404('O contacto não existe!')

    context = {
        'contactos': contactos,
        'x': x,
        'empresas': empresas,
        'departamentos': departamentos,
    }
    return render(request, 'index.html', context)


def botao_ver_todos():
    return redirect('ver_todos')


class Contactos_lista(ListView):
    model = Contactos
