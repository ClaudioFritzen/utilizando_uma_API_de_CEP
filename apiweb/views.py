from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Consulta_cep(request):
    if request.method == 'GET':
        return HttpResponse ("""<form>
  <label for="cep">CEP:</label>
  <input type="text" id="cep" name="cep">
  <br>
  <label for="rua">Rua:</label>
  <input type="text" id="rua" name="rua" disabled>
  <br>
  <label for="bairro">Bairro:</label>
  <input type="text" id="bairro" name="bairro" disabled>
</form>
""")
    elif request.method == "POST":
        pass
       
    
