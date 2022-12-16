import requests

cpf = '93806832'
cpf1 = '93821248'

link = f'https://viacep.com.br/ws/{cpf1}/json/'

requisicao = requests.get(link)

#print(requisicao)

json_cep = requisicao.json()
print(json_cep)

uf = json_cep['uf']
rua = json_cep['logradouro']
bairro = json_cep['bairro']
cidade = json_cep['localidade']
print(uf, rua, bairro)