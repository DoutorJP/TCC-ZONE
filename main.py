import cv2
webcam = cv2.VideoCapture(0)

if webcam.isOpened():
    validation, frame = webcam.read()
    while validation:
        validation, frame = webcam.read()
        cv2.imshow("MONIT_VPP", frame)
        key = cv2.waitKey(5)
        if key==27:
            break
    cv2.imwrite("teste5.PNG", frame)
webcam.release()
cv2.destroyAllWindows()
