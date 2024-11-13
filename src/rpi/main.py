from utils.ocr_utils import *
from utils.crud import *
from obj import Carro
from utils.camera import open_camera
import os



def processar_dados(source):
    find_Roi_Plate(source)
    Pre_Processing_Roi()
    return OCR_Plate()

def main():

    open_camera()
    #source = "img.png"
    source = "car2.jpg" # retirar mais tarde

    # Processamento de dados
    placa = processar_dados(source)
    carro = Carro.Carro(placa, "", "")


    # Enviar dados processados (ainda n funfa direito)
    if(verificar_placa_sistema(carro) == False):
        escrever_dados(carro)



if __name__ == "__main__":
    main()
