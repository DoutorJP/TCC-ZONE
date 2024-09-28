import cv2
import imutils
import numpy as np


def open_camera():
    webcam = cv2.VideoCapture(0)
    if webcam.isOpened():
        validation, frame = webcam.read()
        while validation:
            validation, frame = webcam.read()
            #mostra o frame na tela, deletar mais tarde
            cv2.imshow("MONIT_VPP", frame)
            
            #tira a foto quando ESC é pressionado. trocar pela leitura do sensor ultrassônico quando estiver pronto
            key = cv2.waitKey(5)
            if key==27:
                break

        frame = cv2.resize(frame, (620,480) )
        cv2.imwrite("img.PNG", frame)

webcam.release()
#deletar quando não for mais preciso o frame...
cv2.destroyAllWindows()
