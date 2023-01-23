from django.urls import path
from . import views

urlpatterns = [
    path('', views.Consulta_cep, name="consultar"), 
]
