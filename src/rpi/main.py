

from utils.ocr_utils import *
import utils.crud
from obj import Carro
from utils.camera import open_camera



def processar_dados(source):
    find_Roi_Plate(source)
    Pre_Processing_Roi()
    return OCR_Plate()

def main():

    #open_camera()
    #source = "img.png"
    source = "car2.jpg" # retirar mais tarde

    # Processamento de dados
    placa = processar_dados(source)



    # Enviar dados processados
    #carro = Carro.Carro("", "", "")
    #escrever_dados(carro)
    

if __name__ == "__main__":
    main()
