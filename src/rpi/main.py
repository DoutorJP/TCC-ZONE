import cv2

from utils.ocr_utils import *
import utils.crud
from obj import Carro
def main():

    # Processamento de dados
    source = "car1.jpg"

    find_Roi_Plate(source)
    Pre_Processing_Roi()
    placa = OCR_Plate()
    
    # Enviar dados processados
    #carro = Carro.Carro("", "", "")
    #escrever_dados(carro)
    

if __name__ == "__main__":
    main()
