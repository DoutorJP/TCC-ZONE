from datetime import datetime

class Carro:
    def __init__(self, placa, modelo, dono):
        self.placa = placa
        self.modelo = modelo
        self.dono = dono

    def dataentrada(self):
            return datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
