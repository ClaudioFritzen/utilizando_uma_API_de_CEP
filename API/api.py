import requests

cep = '938.068-32'
cpf1 = '93821248'

cep = cep.replace('-','').replace('.','').replace(' ', '')
print(cep)

if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(link)

    #print(requisicao)

    json_cep = requisicao.json()
    print(json_cep)

    uf = json_cep['uf']
    rua = json_cep['logradouro']
    bairro = json_cep['bairro']
    cidade = json_cep['localidade']
    print(uf, rua, bairro)

else:
    print('CEP invalido')

# busca do CPF a partir do Endereço


