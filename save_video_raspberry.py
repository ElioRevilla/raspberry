import cv2
import time

captura = cv2.VideoCapture(-1)

video_inicio=time.strftime("%H-%M-%S")
nombre_video=str(video_inicio)+'.avi'
salida = cv2.VideoWriter(nombre_video,cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))
        
while (captura.isOpened()):
  ret, imagen = captura.read()
  if ret == True:
    cv2.imshow('video', imagen)
    salida.write(imagen)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
  else: break
captura.release()
salida.release()
cv2.destroyAllWindows()