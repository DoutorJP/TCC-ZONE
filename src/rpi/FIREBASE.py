import requests
import json
from datetime import datetime

link = "https://dbteste-449d5-default-rtdb.firebaseio.com"
#dados = {'Placa': 'BRA2E19', 'Modelo': 'RAV4', 'Dono': 'Joao Pedro'}
#requesicao = requests.post(f'{link}/Carros/.json', data=json.dumps(dados))


class Carro:
    def __init__(self, placa, modelo, dono):
        self.placa = placa
        self.modelo = modelo
        self.dono = dono

    def dataentrada(self):
            return datetime.now().strftime("%m/%d/%Y, %H:%M:%S")



placa=input("Placa: ")
modelo=input("Modelo: ")
dono=input("Dono: ")
c = Carro(placa, modelo, dono)




dados = {'Placa': c.placa, 'Modelo': c.modelo, 'Dono': c.dono, 'DataEntrada': c.dataentrada()}
requesicao = requests.post(f'{link}/Carros/.json', data=json.dumps(dados))


