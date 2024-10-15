import requests
import json
from obj import Carro
from datetime import datetime


link = "https://dbteste-449d5-default-rtdb.firebaseio.com"


def escrever_dados(carro):
    dados = {'Placa': carro.placa, 'Modelo': carro.modelo, 'Dono': carro.dono, 'DataEntrada': carro.dataentrada()}
    requesicao = requests.post(f'{link}/Carros/.json', data=json.dumps(dados))


#ainda n funfa direito
def verificar_placa_sistema(carro):
    dict = ler_dados(carro)
    if carro.placa in dict:
        print("placa " + carro.placa + " encontrada no sistema")
        return True
    else:
        print("placa " + carro.placa + " não encontrada no sistema")
        return False

def ler_dados(carro):
    requisicao = requests.get(f'{link}/.json')
    dic_requisicao = requisicao.json()
    return dic_requisicao


    #print(dic_requisicao['Carros'])
    #print(dic_requisicao)
