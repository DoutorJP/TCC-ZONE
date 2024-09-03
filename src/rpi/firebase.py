import requests
import json
import carro as Carro
from datetime import datetime
import leitura

link = "https://dbteste-449d5-default-rtdb.firebaseio.com"
#dados = {'Placa': 'BRA2E19', 'Modelo': 'RAV4', 'Dono': 'Joao Pedro'}
#requesicao = requests.post(f'{link}/Carros/.json', data=json.dumps(dados))


# ------------------------- ESCRITA (POST) --------------------------
'''
placa=input("Placa: ")
modelo=input("Modelo: ")
dono=input("Dono: ")
'''
placa, modelo, dono = ("",)*3
c = Carro.Carro(leitura.texto, modelo, dono)

print(c.modelo)

dados = {'Placa': c.placa, 'Modelo': c.modelo, 'Dono': c.dono, 'DataEntrada': c.dataentrada()}
requesicao = requests.post(f'{link}/Carros/.json', data=json.dumps(dados))


# ------------------------- LEITURA (GET)--------------------------

'''
requisicao = requests.get(f'{link}/.json')
dic_requisicao = requisicao.json()
#print(dic_requisicao['Carros'])
print(dic_requisicao)
'''