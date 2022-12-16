import requests
import pandas as pd

uf = 'rj'
cidade = 'Rio de Janeiro'
endereco = 'Rio Branco'


link = f'https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/'

requisicao = requests.get(link)
print(requisicao)

dic_requisicao = requisicao.json()
print(dic_requisicao)

tabela = pd.DataFrame(dic_requisicao)
print(tabela)