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



def mayo(request):
    tareasmayo = Tarea_mayo.objects.all()

    form = FormTarea_mayo()
    if request.method == 'POST':
        form = FormTarea_mayo(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/mayo/')

    context = {'tareas': tareasmayo, 'form': form}
    return render(request, 'tareas/mayo.html', context)

def editar_tarea_mayo(request, pk):
    tarea = Tarea_mayo.objects.get(id=pk)

    form = FormTarea(instance=tarea)

    if request.method == "POST":
        form = FormTarea_mayo(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('/mayo/')

    context = {'form': form}
    return render(request, 'tareas/editar_tarea_mayo.html', context)


def eliminar_tarea_mayo(request, pk):
    tarea = Tarea_mayo.objects.get(id=pk)

    if request.method == "POST":
        tarea.delete()
        return redirect('/mayo')

    context = {'tarea': tarea}
    return render(request, 'tareas/eliminar_tarea_mayo.html', context)

def marzo(request):
    tareasmarzo = Tarea_marzo.objects.all()

    form = FormTarea_marzo()
    if request.method == 'POST':
        form = FormTarea_marzo(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/marzo/')

    context = {'tareas': tareasmarzo, 'form': form}
    return render(request, 'tareas/marzo.html', context)

def editar_tarea_marzo(request, pk):
    tarea = Tarea_marzo.objects.get(id=pk)

    form = FormTarea(instance=tarea)

    if request.method == "POST":
        form = FormTarea_marzo(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('/marzo/')

    context = {'form': form}
    return render(request, 'tareas/editar_tarea_marzo.html', context)


def eliminar_tarea_marzo(request, pk):
    tarea = Tarea_marzo.objects.get(id=pk)

    if request.method == "POST":
        tarea.delete()
        return redirect('/marzo')

    context = {'tarea': tarea}
    return render(request, 'tareas/eliminar_tarea_marzo.html', context)

def abril(request):
    tareasabril = Tarea_abril.objects.all()

    form = FormTarea_abril()
    if request.method == 'POST':
        form = FormTarea_abril(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/abril/')

    context = {'tareas': tareasabril, 'form': form}
    return render(request, 'tareas/abril.html', context)

def editar_tarea_abril(request, pk):
    tarea = Tarea_abril.objects.get(id=pk)

    form = FormTarea(instance=tarea)

    if request.method == "POST":
        form = FormTarea_abril(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('/abril/')

    context = {'form': form}
    return render(request, 'tareas/editar_tarea_abril.html', context)


def eliminar_tarea_abril(request, pk):
    tarea = Tarea_abril.objects.get(id=pk)

    if request.method == "POST":
        tarea.delete()
        return redirect('/abril')

    context = {'tarea': tarea}
    return render(request, 'tareas/eliminar_tarea_abril.html', context)

def junio(request):
    tareasjunio = Tarea_junio.objects.all()

    form = FormTarea_junio()
    if request.method == 'POST':
        form = FormTarea_junio(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/junio/')

    context = {'tareas': tareasjunio, 'form': form}
    return render(request, 'tareas/junio.html', context)

def editar_tarea_junio(request, pk):
    tarea = Tarea_junio.objects.get(id=pk)

    form = FormTarea(instance=tarea)

    if request.method == "POST":
        form = FormTarea_junio(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('/junio/')

    context = {'form': form}
    return render(request, 'tareas/editar_tarea_junio.html', context)


def eliminar_tarea_junio(request, pk):
    tarea = Tarea_junio.objects.get(id=pk)

    if request.method == "POST":
        tarea.delete()
        return redirect('/junio')

    context = {'tarea': tarea}
    return render(request, 'tareas/eliminar_tarea_junio.html', context)

def julio(request):
    tareasjulio = Tarea_julio.objects.all()

    form = FormTarea_julio()
    if request.method == 'POST':
        form = FormTarea_julio(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/julio/')

    context = {'tareas': tareasjulio, 'form': form}
    return render(request, 'tareas/julio.html', context)

def editar_tarea_julio(request, pk):
    tarea = Tarea_julio.objects.get(id=pk)

    form = FormTarea(instance=tarea)

    if request.method == "POST":
        form = FormTarea_julio(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('/julio/')

    context = {'form': form}
    return render(request, 'tareas/editar_tarea_julio.html', context)


def eliminar_tarea_julio(request, pk):
    tarea = Tarea_julio.objects.get(id=pk)

    if request.method == "POST":
        tarea.delete()
        return redirect('/julio')

    context = {'tarea': tarea}
    return render(request, 'tareas/eliminar_tarea_julio.html', context)

def agosto(request):
    tareasagosto = Tarea_agosto.objects.all()

    form = FormTarea_agosto()
    if request.method == 'POST':
        form = FormTarea_agosto(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/agosto/')

    context = {'tareas': tareasagosto, 'form': form}
    return render(request, 'tareas/agosto.html', context)

def editar_tarea_agosto(request, pk):
    tarea = Tarea_agosto.objects.get(id=pk)

    form = FormTarea(instance=tarea)

    if request.method == "POST":
        form = FormTarea_agosto(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('/agosto/')

    context = {'form': form}
    return render(request, 'tareas/editar_tarea_agosto.html', context)


def eliminar_tarea_agosto(request, pk):
    tarea = Tarea_agosto.objects.get(id=pk)

    if request.method == "POST":
        tarea.delete()
        return redirect('/agosto')

    context = {'tarea': tarea}
    return render(request, 'tareas/eliminar_tarea_agosto.html', context)

def septiembre(request):
    tareasseptiembre = Tarea_septiembre.objects.all()

    form = FormTarea_septiembre()
    if request.method == 'POST':
        form = FormTarea_septiembre(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/septiembre/')

    context = {'tareas': tareasseptiembre, 'form': form}
    return render(request, 'tareas/septiembre.html', context)

def editar_tarea_septiembre(request, pk):
    tarea = Tarea_septiembre.objects.get(id=pk)

    form = FormTarea(instance=tarea)

    if request.method == "POST":
        form = FormTarea_septiembre(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('/septiembre/')

    context = {'form': form}
    return render(request, 'tareas/editar_tarea_septiembre.html', context)


def eliminar_tarea_septiembre(request, pk):
    tarea = Tarea_septiembre.objects.get(id=pk)

    if request.method == "POST":
        tarea.delete()
        return redirect('/septiembre')

    context = {'tarea': tarea}
    return render(request, 'tareas/eliminar_tarea_septiembre.html', context)

def octubre(request):
    tareasoctubre = Tarea_octubre.objects.all()

    form = FormTarea_octubre()
    if request.method == 'POST':
        form = FormTarea_octubre(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/octubre/')

    context = {'tareas': tareasoctubre, 'form': form}
    return render(request, 'tareas/octubre.html', context)

def editar_tarea_octubre(request, pk):
    tarea = Tarea_octubre.objects.get(id=pk)

    form = FormTarea(instance=tarea)

    if request.method == "POST":
        form = FormTarea_octubre(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('/octubre/')

    context = {'form': form}
    return render(request, 'tareas/editar_tarea_octubre.html', context)


def eliminar_tarea_octubre(request, pk):
    tarea = Tarea_octubre.objects.get(id=pk)

    if request.method == "POST":
        tarea.delete()
        return redirect('/octubre')

    context = {'tarea': tarea}
    return render(request, 'tareas/eliminar_tarea_octubre.html', context)

def noviembre(request):
    tareasnoviembre = Tarea_noviembre.objects.all()

    form = FormTarea_noviembre()
    if request.method == 'POST':
        form = FormTarea_noviembre(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/noviembre/')

    context = {'tareas': tareasnoviembre, 'form': form}
    return render(request, 'tareas/noviembre.html', context)

def editar_tarea_noviembre(request, pk):
    tarea = Tarea_noviembre.objects.get(id=pk)

    form = FormTarea(instance=tarea)

    if request.method == "POST":
        form = FormTarea_noviembre(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('/noviembre/')

    context = {'form': form}
    return render(request, 'tareas/editar_tarea_noviembre.html', context)


def eliminar_tarea_noviembre(request, pk):
    tarea = Tarea_noviembre.objects.get(id=pk)

    if request.method == "POST":
        tarea.delete()
        return redirect('/noviembre')

    context = {'tarea': tarea}
    return render(request, 'tareas/eliminar_tarea_noviembre.html', context)

def diciembre(request):
    tareasdiciembre = Tarea_diciembre.objects.all()

    form = FormTarea_diciembre()
    if request.method == 'POST':
        form = FormTarea_diciembre(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/diciembre/')

    context = {'tareas': tareasdiciembre, 'form': form}
    return render(request, 'tareas/diciembre.html', context)

def editar_tarea_diciembre(request, pk):
    tarea = Tarea_diciembre.objects.get(id=pk)

    form = FormTarea(instance=tarea)

    if request.method == "POST":
        form = FormTarea_diciembre(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('/diciembre/')

    context = {'form': form}
    return render(request, 'tareas/editar_tarea_diciembre.html', context)


def eliminar_tarea_diciembre(request, pk):
    tarea = Tarea_diciembre.objects.get(id=pk)

    if request.method == "POST":
        tarea.delete()
        return redirect('/diciembre')

    context = {'tarea': tarea}
    return render(request, 'tareas/eliminar_tarea_diciembre.html', context)