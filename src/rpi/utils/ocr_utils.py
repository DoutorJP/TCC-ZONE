import cv2
import numpy as np
import pytesseract


def adjust_brightness(image, alpha, beta):
    adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted


def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")

    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)


def image_cleaning(img, alpha, beta, gamma, thresh):

    # 1) Converter a imagem para a escala cinza
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 2) Ajustar o brilho da imagem com a função adjust_brightness()
    img_brilho = adjust_brightness(img_gray, alpha, beta)

    # 3) Ajustar o contraste da imagem com a função ajust_gamma()
    imgt = adjust_gamma(img_brilho, gamma)

    # 4) Linearizando a imagem
    _, bin = cv2.threshold(imgt, thresh, 255, cv2.THRESH_BINARY)

    # 5) Desfocar a imagem
    # blur = cv2.GaussianBlur(bin, (5, 5), 0)

    return bin


def find_Roi_Plate(source):
    # Lendo a imagem
    img = cv2.imread(source)

    # imagem sem alterações
    #cv2.imshow('imgagem sem alteracoes', img)

    # Tratamento de imagem
    bin = image_cleaning(img, 0.6, 10, 1.2, 90)

    # Aplicando um contorno a imagem linear (binarizada)
    contorn, hier = cv2.findContours(bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
   # cv2.drawContours(img, contorn, -1, (0, 255, 0), 2)
   # cv2.imshow('cont', img)

    # Procurando contornos que se parecem com retângulos para recorte
    for c in contorn:
        perimeter = cv2.arcLength(c, True)

        # Limpando contornos excessivamente grandes e pequenos (grandes chances de não ser uma placa)
        if perimeter > 150:

            aproxx = cv2.approxPolyDP(c, 0.03 * perimeter, True)

            if len(aproxx) == 4:
                (x, y, comp, lar) = cv2.boundingRect(c)

                # Toda placa brasileira possui as medidas horizontais maiores que as verticais
                # Assim, se a largura for menor que o comprimento, existe uma placa
                if lar < comp:
                    cv2.rectangle(img, (x, y), (x + comp, y + lar), (0, 255, 0), 2)
                    roi = img[y:(y + lar), x:(x + comp)]

                    # Recorta a imagem da placa e para o for
                    cv2.imwrite('Rois/roi.jpg', roi)
                    break

    # imagem contornada
    cv2.imshow('imagem contornada', img)
    cv2.imwrite('roi.jpg', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def Pre_Processing_Roi():
    img_roi = cv2.imread("roi.jpg")
    if img_roi is None:
        return

    img_roi = image_cleaning(img_roi, 0.6, 10, 1.2, 80)
    cv2.imwrite("roi-ocr.jpg", img_roi)

    cv2.imshow("res", img_roi)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def OCR_Plate():
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR'

    img = cv2.imread("roi-ocr.jpg")

    config = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 --psm 6'

    out = pytesseract.image_to_string(img, lang="eng", config=config)

    #print(out)
    #return out

