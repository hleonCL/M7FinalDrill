"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from laboratorio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexView, name='index'),
    path('laboratorios/', views.laboratorios, name='laboratorios'),
    path('editar/<int:id>/', views.editar_laboratorio, name='editar_laboratorio'),
    path('eliminar/<int:id>/', views.eliminar_laboratorio, name='eliminar_laboratorio'),
    path('agregar/', views.agregar_laboratorio, name='agregar_laboratorio'),
    path('confirmar_eliminar/<int:id>/', views.confirmar_eliminar_laboratorio, name='confirmar_eliminar_laboratorio'),
    ]



