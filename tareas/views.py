from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "tareas/home.html" )

def febrero(request):
    tareas = Tarea.objects.all()

    form = FormTarea()
    if request.method == 'POST':
        form = FormTarea(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/febrero')

    context = {'tareas': tareas, 'form': form}
    return render(request, "tareas/febrero.html", context)


def editar_tarea(request, pk):
    tarea = Tarea.objects.get(id=pk)

    form = FormTarea(instance=tarea)

    if request.method == "POST":
        form = FormTarea(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('/febrero')

    context = {'form': form}
    return render(request, 'tareas/editar_tarea.html', context)


def eliminar_tarea(request, pk):
    tarea = Tarea.objects.get(id=pk)

    if request.method == "POST":
        tarea.delete()
        return redirect('/febrero')

    context = {'tarea': tarea}
    return render(request, 'tareas/eliminar_tarea.html', context)


def enero(request):
    tareas1 = Tarea1.objects.all()

    form = FormTarea1()
    if request.method == 'POST':
        form = FormTarea1(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/enero/')

    context = {'tareas': tareas1, 'form': form}
    return render(request, 'tareas/enero.html', context)

def editar_tarea1(request, pk):
    tarea = Tarea1.objects.get(id=pk)

    form = FormTarea(instance=tarea)

    if request.method == "POST":
        form = FormTarea1(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('/enero/')

    context = {'form': form}
    return render(request, 'tareas/editar_tarea1.html', context)


def eliminar_tarea1(request, pk):
    tarea = Tarea1.objects.get(id=pk)

    if request.method == "POST":
        tarea.delete()
        return redirect('/enero')

    context = {'tarea': tarea}
    return render(request, 'tareas/eliminar_tarea1.html', context)
