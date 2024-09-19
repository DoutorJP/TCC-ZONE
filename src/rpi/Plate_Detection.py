from util import *


# Lendo a imagem
img = cv2.imread('Car_Images/car_2.png')

# imagem sem alterações
cv2.imshow('imgagem sem alteracoes', img)



# Tratamento da imagem em 3 etapas:

# 1) Converter a imagem para a escala cinza
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# 2) Ajustar o brilho da imagem com a função adjust_brightness()
img_brilho = adjust_brightness(img_gray, 0.6, 10)

# 3) Ajustar o contraste da imagem com a função ajust_gamma()
imgt = adjust_gamma(img_brilho, 1.2)


# Linearizando a imagem
_, bin = cv2.threshold(imgt, 90, 255, cv2.THRESH_BINARY)


# Caso necessário, desfoque a imagem, descomentando a linha abaixo
#blur = cv2.GaussianBlur(bin, (5, 5), 0)

# Aplicando um contorno a imagem linear (binarizada)
contorn, hier = cv2.findContours(bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#cv2.drawContours(img, contorn, -1, (0, 255, 0), 2)
#cv2.imshow('cont', img)

# Procurando contornos que se parecem com retângulos
for c in contorn:
    perimeter = cv2.arcLength(c, True)

    # Limpando contornos excessivamente grandes e pequenos (grandes chances de não ser uma placa)
    if perimeter > 150 and perimeter < 900:

        aproxx = cv2.approxPolyDP(c, 0.03 * perimeter, True)

        if len(aproxx) == 4:
            (x, y, comp, lar) = cv2.boundingRect(c)

            # Toda placa brasileira possui as medidas horizontais maiores que as verticais
            # Assim, se a largura for menor que o comprimento, existe uma placa
            if lar < comp:
                cv2.rectangle(img, (x, y), (x + comp, y + lar), (0, 255, 0), 2)
                roi = img[y:y + lar, x:x + comp]

                # Recorta a imagem da placa e para o for
                cv2.imwrite('roi.jpg', roi)
                break



# imagem tratada
cv2.imshow('imagem tratada', imgt)

# imagem linearizada (binarizada)
cv2.imshow('imagem binarizada', bin)

# imagem contornada
cv2.imshow('imagem contornada', img)



cv2.waitKey(0)
cv2.destroyAllWindows()