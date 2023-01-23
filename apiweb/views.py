from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Consulta_cep(request):
    if request.method == 'GET':
        return HttpResponse ('Digite seu Cep <input value="seu cep">')
