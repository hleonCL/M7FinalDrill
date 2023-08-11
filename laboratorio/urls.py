from django.urls import include, path

urlpatterns = [
   
    path('laboratorio/', include('laboratorio.urls', namespace='laboratorio')),
    
]
