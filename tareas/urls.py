from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('editar_tarea/<str:pk>', views.editar_tarea, name="editar_tarea"),
    path('eliminar_tarea/<str:pk>', views.eliminar_tarea, name="eliminar_tarea"),
    path('enero/', views.enero, name="enero"),
    path('febrero/', views.febrero, name="febrero"),
    path('editar_tarea1/<str:pk>', views.editar_tarea1, name="editar_tarea1"),
    path('eliminar_tarea1/<str:pk>', views.eliminar_tarea1, name="eliminar_tarea1")
]