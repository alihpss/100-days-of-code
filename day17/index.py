import cv2 as cv

camera = cv.VideoCapture(0)

rodando = True
while rodando:
    status, frame = camera.read()
    
    if not status or cv.waitKey(1) & 0xff == ord('q'):
        rodando = False
    
    cv.imshow("Camera", frame)