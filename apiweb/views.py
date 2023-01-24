from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Consulta_cep(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == "POST":
        pass
       
import requests

def get_address(cep:str):

    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    data = response.json()
    return data.get('logradouro',''), data.get('bairro','')

from django.http import JsonResponse

def get_address_view(request):
    cep = request.GET.get('cep')
    rua, bairro = get_address(cep)
    return JsonResponse({'rua': rua, 'bairro': bairro})
