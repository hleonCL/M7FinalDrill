from django.shortcuts import render, redirect
from .models import Laboratorio


def indexView(request):
    template_name = 'index.html'
    return render(request, template_name)


def laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorios.html', {'laboratorios': laboratorios})

def editar_laboratorio(request, id):
    laboratorio = Laboratorio.objects.get(id=id)
    if request.method == 'POST':
        laboratorio.nombre = request.POST['nombre']
        laboratorio.ciudad = request.POST['ciudad']
        laboratorio.pais = request.POST['pais']
        laboratorio.save()
        return redirect('laboratorios')
    return render(request, 'editar_laboratorio.html', {'laboratorio': laboratorio})

def eliminar_laboratorio(request, id):
    return redirect('confirmar_eliminar_laboratorio', id=id)



def agregar_laboratorio(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad']
        pais = request.POST['pais']
        laboratorio = Laboratorio(nombre=nombre, ciudad=ciudad, pais=pais)
        laboratorio.save()
        return redirect('laboratorios')
    return render(request, 'agregar_laboratorio.html')



def confirmar_eliminar_laboratorio(request, id):
    laboratorio = Laboratorio.objects.get(id=id)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('laboratorios')
    return render(request, 'confirmar_eliminar_laboratorio.html', {'laboratorio': laboratorio})