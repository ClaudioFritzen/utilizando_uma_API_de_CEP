from django.urls import path
from . import views

urlpatterns = [
    path('', views.Consulta_cep, name="consultar"), 
    path('get_address/', views.get_address_view, name='get_address'),

]
