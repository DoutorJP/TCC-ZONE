import pytesseract
import cv2

img = cv2.imread("img.png")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\Tesseract.exe"
texto=''
try:
    texto = pytesseract.image_to_string(img, config='--psm 7')
    print(texto)
except pytesseract.TesseractError as e:
    print(f"An error occurred during OCR: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

