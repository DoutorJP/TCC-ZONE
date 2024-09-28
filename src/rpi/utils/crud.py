import requests
import json
from obj import Carro
from datetime import datetime


link = "https://dbteste-449d5-default-rtdb.firebaseio.com"


def escrever_dados(carro):
    dados = {'Placa': carro.placa, 'Modelo': carro.modelo, 'Dono': carro.dono, 'DataEntrada': carro.dataentrada()}
    requesicao = requests.post(f'{link}/Carros/.json', data=json.dumps(dados))


def ler_dados():
    requisicao = requests.get(f'{link}/.json')
    dic_requisicao = requisicao.json()

    #print(dic_requisicao['Carros'])
    #print(dic_requisicao)
