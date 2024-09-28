from utils import ocr_utils
from utils import crud
from obj import Carro
def main():

    # Processamento de dados
    # source = "Car_Images/car_1.jpg"
    #find_Roi_Plate(source)
    #Pre_Processing_Roi()
    #OCR_Plate()
    
    # Enviar dados processados
    carro = Carro.Carro("", "", "")
    print(carro.dataEntradavar)
    #escrever_dados(carro)
    

if __name__ == "__main__":
    main()
